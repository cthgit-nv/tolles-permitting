import sys,os,re
from lxml import etree
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; ns={'w':W}; q=lambda t:'{%s}%s'%(W,t)
d=sys.argv[1]
tree=etree.parse(d+'/word/document.xml'); root=tree.getroot()
for tr in root.xpath('//w:tr[w:trPr/w:del]',namespaces=ns): tr.getparent().remove(tr)
for m in root.xpath('//w:pPr/w:rPr/w:del',namespaces=ns):
    p=m.getparent().getparent().getparent(); m.getparent().remove(m)
    nxt=p.getnext(); runs=[c for c in p if c.tag not in (q('pPr'),q('del'))]
    if nxt is not None and nxt.tag==q('p'):
        pPr=nxt.find(q('pPr')); pos=(list(nxt).index(pPr)+1) if pPr is not None else 0
        for i,ch in enumerate(runs): nxt.insert(pos+i,ch)
    p.getparent().remove(p)
for el in root.xpath('//w:del',namespaces=ns): el.getparent().remove(el)
for el in root.xpath('//w:pPr/w:rPr/w:ins|//w:trPr/w:ins',namespaces=ns): el.getparent().remove(el)
for el in root.xpath('//w:ins',namespaces=ns):
    par=el.getparent(); i=list(par).index(el)
    for j,ch in enumerate(list(el)): par.insert(i+j,ch)
    par.remove(el)
for t in ['commentRangeStart','commentRangeEnd']:
    for el in root.xpath('//w:%s'%t,namespaces=ns): el.getparent().remove(el)
for el in root.xpath('//w:r[w:commentReference]',namespaces=ns): el.getparent().remove(el)
tree.write(d+'/word/document.xml',xml_declaration=True,encoding='UTF-8',standalone=True)
if os.path.exists(d+'/word/comments.xml'): os.remove(d+'/word/comments.xml')
r=open(d+'/word/_rels/document.xml.rels').read(); open(d+'/word/_rels/document.xml.rels','w').write(re.sub(r'<Relationship [^>]*Target="comments.xml"[^>]*/>','',r))
c=open(d+'/[Content_Types].xml').read(); open(d+'/[Content_Types].xml','w').write(re.sub(r'<Override [^>]*comments.xml"[^>]*/>','',c))
