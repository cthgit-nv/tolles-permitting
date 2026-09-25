"""Tracked-change helpers for editing an unpacked .docx with lxml."""
import copy, difflib, re
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W}
AUTHOR = 'Permitting Desk'
DATE = '2026-09-25T09:00:00Z'
XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'


def q(t):
    return '{%s}%s' % (W, t)


class Redliner:
    def __init__(self, doc_path):
        self.doc_path = doc_path
        self.tree = etree.parse(doc_path)
        self.root = self.tree.getroot()
        self.paras = self.root.xpath('//w:body//w:p', namespaces=NS)
        self.next_id = 90000
        self.comments = []  # (id, text)
        self.log = []

    # ---- ids and marks -------------------------------------------------
    def nid(self):
        self.next_id += 1
        return str(self.next_id)

    def mark(self, tag):
        el = etree.Element(q(tag))
        el.set(q('id'), self.nid()); el.set(q('author'), AUTHOR); el.set(q('date'), DATE)
        return el

    # ---- run construction ------------------------------------------------
    @staticmethod
    def _run(rpr, text, deleted=False):
        r = etree.Element(q('r'))
        if rpr is not None:
            r.append(copy.deepcopy(rpr))
        parts = re.split(r'(\t)', text)
        for part in parts:
            if part == '':
                continue
            if part == '\t':
                r.append(etree.Element(q('tab')))
            else:
                t = etree.SubElement(r, q('delText' if deleted else 't'))
                t.text = part
                t.set(XML_SPACE, 'preserve')
        return r

    def _chars(self, p):
        """List of (char, rPr) for the paragraph's direct runs."""
        out = []
        for r in p.findall(q('r')):
            rpr = r.find(q('rPr'))
            for c in r:
                tag = etree.QName(c).localname
                if tag == 't':
                    out += [(ch, rpr) for ch in (c.text or '')]
                elif tag == 'tab':
                    out.append(('\t', rpr))
        return out

    def text(self, i):
        return ''.join(ch for ch, _ in self._chars(self.paras[i]))

    # ---- comments --------------------------------------------------------
    def _attach_comment(self, p, first_el, last_el, text):
        cid = str(len(self.comments))
        self.comments.append((cid, text))
        s = etree.Element(q('commentRangeStart')); s.set(q('id'), cid)
        e = etree.Element(q('commentRangeEnd')); e.set(q('id'), cid)
        ref_run = etree.Element(q('r'))
        rpr = etree.SubElement(ref_run, q('rPr'))
        rs = etree.SubElement(rpr, q('rStyle')); rs.set(q('val'), 'CommentReference')
        cr = etree.SubElement(ref_run, q('commentReference')); cr.set(q('id'), cid)
        first_el.addprevious(s)
        last_el.addnext(e)
        e.addnext(ref_run)

    # ---- paragraph edits -------------------------------------------------
    def edit(self, i, new_text, comment=None):
        """Word-level tracked diff of paragraph i to new_text."""
        p = self.paras[i]
        old = self._chars(p)
        old_text = ''.join(c for c, _ in old)
        assert old_text != new_text, f'no change at {i}'
        runs = p.findall(q('r'))
        assert runs, f'no runs at {i}'
        for r in runs:
            for c in r:
                assert etree.QName(c).localname in ('rPr', 't', 'tab', 'lastRenderedPageBreak'), (i, etree.QName(c).localname)
        anchor = etree.Element(q('r'))
        runs[0].addprevious(anchor)
        for r in runs:
            p.remove(r)
        for pe in p.findall(q('proofErr')):
            p.remove(pe)
        tok = lambda s: re.findall(r'\s+|[^\s]+', s)
        a, b = tok(old_text), tok(new_text)
        # map token index -> char offset in old
        offs, o = [], 0
        for t in a:
            offs.append(o); o += len(t)
        default_rpr = old[0][1] if old else None
        new_nodes = []

        def emit_equal(ci, cj):
            seg, cur, buf = old[ci:cj], None, ''
            for ch, rpr in seg:
                if rpr is not cur and buf:
                    new_nodes.append(self._run(cur, buf)); buf = ''
                cur = rpr; buf += ch
            if buf:
                new_nodes.append(self._run(cur, buf))

        def emit_del(ci, cj):
            d = self.mark('del')
            seg, cur, buf = old[ci:cj], None, ''
            for ch, rpr in seg:
                if rpr is not cur and buf:
                    d.append(self._run(cur, buf, deleted=True)); buf = ''
                cur = rpr; buf += ch
            if buf:
                d.append(self._run(cur, buf, deleted=True))
            new_nodes.append(d)

        def emit_ins(text, rpr):
            ins = self.mark('ins')
            ins.append(self._run(rpr, text))
            new_nodes.append(ins)

        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            c1 = offs[i1] if i1 < len(a) else len(old_text)
            c2 = offs[i2] if i2 < len(a) else len(old_text)
            near = old[c1 - 1][1] if c1 > 0 else default_rpr
            if op == 'equal':
                emit_equal(c1, c2)
            elif op == 'delete':
                emit_del(c1, c2)
            elif op == 'insert':
                emit_ins(''.join(b[j1:j2]), near)
            else:
                emit_del(c1, c2)
                emit_ins(''.join(b[j1:j2]), old[c1][1])
        for n in new_nodes:
            anchor.addprevious(n)
        p.remove(anchor)
        if comment:
            changed = [n for n in new_nodes if etree.QName(n).localname in ('ins', 'del')]
            self._attach_comment(p, changed[0], changed[-1], comment)
        self.log.append(('edit', i, old_text[:80]))

    def delete_para(self, i, comment=None):
        p = self.paras[i]
        runs = p.findall(q('r'))
        d = self.mark('del')
        runs[0].addprevious(d)
        for r in runs:
            for t in r.findall(q('t')):
                t.tag = q('delText')
            d.append(r)
        ppr = p.find(q('pPr'))
        if ppr is None:
            ppr = etree.Element(q('pPr')); p.insert(0, ppr)
        rpr = ppr.find(q('rPr'))
        if rpr is None:
            rpr = etree.SubElement(ppr, q('rPr'))
        rpr.insert(0, self.mark('del'))
        if comment:
            self._attach_comment(p, d, d, comment)
        self.log.append(('delete', i, ''))

    def insert_after(self, i, text, comment=None, like=None):
        """Insert a new paragraph after paragraph i, formatted like paragraph `like` (default i)."""
        ref = self.paras[i]
        tmpl = self.paras[like if like is not None else i]
        p = etree.Element(q('p'))
        tppr = tmpl.find(q('pPr'))
        ppr = copy.deepcopy(tppr) if tppr is not None else etree.Element(q('pPr'))
        for old in ppr.findall(q('rPr')):
            ppr.remove(old)
        rpr = etree.SubElement(ppr, q('rPr'))
        rpr.append(self.mark('ins'))
        p.append(ppr)
        first = tmpl.find(q('r'))
        run_rpr = first.find(q('rPr')) if first is not None else None
        ins = self.mark('ins')
        ins.append(self._run(run_rpr, text))
        p.append(ins)
        # insert after the last inserted sibling that follows ref
        anchor = ref
        while anchor.getnext() is not None and anchor.getnext().get('data-new') == '1':
            anchor = anchor.getnext()
        anchor.addnext(p)
        p.set('data-new', '1')
        if comment:
            self._attach_comment(p, ins, ins, comment)
        self.log.append(('insert', i, text[:80]))
        return p

    # ---- table rows ----------------------------------------------------
    def row_of(self, i):
        return self.paras[i].xpath('ancestor::w:tr[1]', namespaces=NS)[0]

    def delete_row(self, tr, comment=None):
        trpr = tr.find(q('trPr'))
        if trpr is None:
            trpr = etree.Element(q('trPr'))
            tcs = tr.findall(q('tc'))
            tcs[0].addprevious(trpr)
        trpr.append(self.mark('del'))
        first = None
        for p in tr.iter(q('p')):
            runs = p.findall(q('r'))
            if runs:
                d = self.mark('del')
                runs[0].addprevious(d)
                for r in runs:
                    for t in r.findall(q('t')):
                        t.tag = q('delText')
                    d.append(r)
                first = first if first is not None else (p, d)
            ppr = p.find(q('pPr'))
            if ppr is None:
                ppr = etree.Element(q('pPr')); p.insert(0, ppr)
            rpr = ppr.find(q('rPr'))
            if rpr is None:
                rpr = etree.SubElement(ppr, q('rPr'))
            rpr.insert(0, self.mark('del'))
        if comment and first:
            self._attach_comment(first[0], first[1], first[1], comment)
        self.log.append(('delete_row', '', ''))

    def insert_row_after(self, tr_ref, tr_template, cell_texts, comment=None):
        new = copy.deepcopy(tr_template)
        for el in new.iter():
            if el.tag in (q('ins'), q('del')) and el.getparent() is not None and el.getparent().tag == q('trPr'):
                el.getparent().remove(el)
        trpr = new.find(q('trPr'))
        if trpr is None:
            trpr = etree.Element(q('trPr')); new.findall(q('tc'))[0].addprevious(trpr)
        trpr.append(self.mark('ins'))
        tcs = new.findall(q('tc'))
        assert len(tcs) == len(cell_texts), (len(tcs), cell_texts)
        first = None
        for tc, txt in zip(tcs, cell_texts):
            paras = tc.findall(q('p'))
            for extra in paras[1:]:
                tc.remove(extra)
            p = paras[0]
            r0 = p.find(q('r'))
            rpr = copy.deepcopy(r0.find(q('rPr'))) if r0 is not None and r0.find(q('rPr')) is not None else None
            for c in list(p):
                if c.tag != q('pPr'):
                    p.remove(c)
            ppr = p.find(q('pPr'))
            if ppr is None:
                ppr = etree.Element(q('pPr')); p.insert(0, ppr)
            for old in ppr.findall(q('rPr')):
                ppr.remove(old)
            prpr = etree.SubElement(ppr, q('rPr')); prpr.append(self.mark('ins'))
            ins = self.mark('ins'); ins.append(self._run(rpr, txt)); p.append(ins)
            first = first if first is not None else (p, ins)
        tr_ref.addnext(new)
        if comment:
            self._attach_comment(first[0], first[1], first[1], comment)
        self.log.append(('insert_row', '', cell_texts[0]))
        return new

    # ---- save ------------------------------------------------------------
    def save(self, unpacked_dir):
        for p in self.root.iter(q('p')):
            if 'data-new' in p.attrib:
                del p.attrib['data-new']
        self.tree.write(self.doc_path, xml_declaration=True, encoding='UTF-8', standalone=True)
        if not self.comments:
            return
        cx = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
              '<w:comments xmlns:w="%s">' % W]
        from xml.sax.saxutils import escape
        for cid, text in self.comments:
            paras = ''.join('<w:p><w:pPr><w:pStyle w:val="CommentText"/></w:pPr><w:r><w:t xml:space="preserve">%s</w:t></w:r></w:p>' % escape(line)
                            for line in text.split('\n'))
            cx.append('<w:comment w:id="%s" w:author="%s" w:date="%s" w:initials="PD">%s</w:comment>' % (cid, AUTHOR, DATE, paras))
        cx.append('</w:comments>')
        open(unpacked_dir + '/word/comments.xml', 'w', encoding='utf8').write(''.join(cx))
        rels_p = unpacked_dir + '/word/_rels/document.xml.rels'
        rels = open(rels_p, encoding='utf8').read()
        if 'comments.xml' not in rels:
            rels = rels.replace('</Relationships>', '<Relationship Id="rIdPDcomments" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments" Target="comments.xml"/></Relationships>')
            open(rels_p, 'w', encoding='utf8').write(rels)
        ct_p = unpacked_dir + '/[Content_Types].xml'
        ct = open(ct_p, encoding='utf8').read()
        if '/word/comments.xml' not in ct:
            ct = ct.replace('</Types>', '<Override PartName="/word/comments.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/></Types>')
            open(ct_p, 'w', encoding='utf8').write(ct)
