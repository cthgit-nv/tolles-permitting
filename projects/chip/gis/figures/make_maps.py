import json, math, re, sys, zipfile
from lxml import etree
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MPoly

G = sys.argv[1]; OUT = sys.argv[2]
kml = etree.fromstring(zipfile.ZipFile(G + '/CHIP_App1_Crossings_HartLane_DRAFT_2026-09-25.kmz').read('doc.kml'))
ns = {'k': 'http://www.opengis.net/kml/2.2'}
lat0 = 39.545; mx = 111320 * math.cos(math.radians(lat0)) * 3.28084; my = 110574 * 3.28084  # feet per degree
def xy(lon, lat): return ((lon + 119.04) * mx, (lat - lat0) * my)
def coords(el):
    return [xy(*map(float, c.split(',')[:2])) for c in el.text.split()]
layers = {}
for fol in kml.iter('{%s}Folder' % ns['k']):
    name = fol.find('k:name', ns).text
    feats = []
    for pm in fol.findall('k:Placemark', ns):
        n = pm.find('k:name', ns).text
        for ring in pm.iter('{%s}coordinates' % ns['k']):
            feats.append((n, coords(ring)))
    layers[name] = feats
print({k: len(v) for k, v in layers.items()})

wings = json.load(open(G + '/wings.json'))
def wing500(w):
    pts = [xy(*p) for p in w['geom']['coordinates'][0][:3]]
    # corner = vertex with angle closest to 90 deg
    def ang(i):
        a, b, c = pts[i], pts[i - 1], pts[(i + 1) % 3]
        v1 = (b[0]-a[0], b[1]-a[1]); v2 = (c[0]-a[0], c[1]-a[1])
        return abs(math.degrees(math.acos((v1[0]*v2[0]+v1[1]*v2[1])/(math.hypot(*v1)*math.hypot(*v2)))) - 90)
    ci = min(range(3), key=ang); c = pts[ci]
    others = [pts[j] for j in range(3) if j != ci]
    leg = 500 / math.sqrt(2)
    new = [c] + [(c[0] + (o[0]-c[0]) / math.hypot(o[0]-c[0], o[1]-c[1]) * leg, c[1] + (o[1]-c[1]) / math.hypot(o[0]-c[0], o[1]-c[1]) * leg) for o in others]
    a = abs((new[1][0]-new[0][0])*(new[2][1]-new[0][1]) - (new[2][0]-new[0][0])*(new[1][1]-new[0][1])) / 2 / 43560
    return new, a
W5 = [(w['crossing'], w['section'], *wing500(w)) for w in wings]
print('total ac', round(sum(x[3] for x in W5), 2), [round(x[3], 3) for x in W5])

def base(ax, labels=True):
    for n, ring in layers.get('Reference: Reclamation land (master map)', []):
        ax.add_patch(MPoly(ring, closed=True, fc='#f3e3b3', ec='#b8963c', lw=0.6, zorder=1))
    for n, ring in layers.get('Reference: CHIP LLC parcels', []):
        ax.add_patch(MPoly(ring, closed=True, fc='#cfe3f7', ec='#2b6cb0', lw=0.8, zorder=2))
    for n, ring in layers.get('Reference: PLSS sections (BLM CadNSDI)', []):
        ax.add_patch(MPoly(ring, closed=True, fc='none', ec='#777777', lw=0.5, ls=':', zorder=3))
        if labels:
            cx = sum(p[0] for p in ring)/len(ring); cy = sum(p[1] for p in ring)/len(ring)
            m = re.match(r'Sec\. (\d+), (T\d+N)', n)
            ax.text(cx, cy, f'{m.group(1)}\n{m.group(2)}', ha='center', va='center', fontsize=7, color='#555555', zorder=4, clip_on=True)

# ---- Figure 1: overview ----
fig, ax = plt.subplots(figsize=(10, 9))
base(ax)
for cr, sec, pts, a in W5:
    ax.add_patch(MPoly(pts, closed=True, fc='#d62828', ec='#8b0000', lw=1, zorder=6))
done = set()
for cr, sec, pts, a in W5:
    if cr in done: continue
    done.add(cr)
    c = pts[0]
    ax.annotate(cr.replace('Corner ', ''), c, xytext=(c[0]+900, c[1]+700), fontsize=9, fontweight='bold', color='#8b0000',
                arrowprops=dict(arrowstyle='-', color='#8b0000', lw=0.8), zorder=7)
for n, ring in layers.get('Application 1: Hart Lane road segment (candidate)', []):
    if 'centerline' in n:
        ax.plot([p[0] for p in ring], [p[1] for p in ring], color='#2a9d8f', lw=2.5, ls='--', zorder=6)
        e = ring[0]; ax.text(e[0]-300, e[1], 'Hart Lane access\n(future application,\nalignment candidate)', fontsize=8, color='#1d6f65', ha='right', va='top', zorder=7)
allpts = [p for _, ring in layers.get('Reference: CHIP LLC parcels', []) for p in ring] + [p for x in W5 for p in x[2]]
xs = [p[0] for p in allpts]; ys = [p[1] for p in allpts]
pad = 2500
ax.set_xlim(min(xs)-pad, max(xs)+pad); ax.set_ylim(min(ys)-pad, max(ys)+pad)
ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
ax.legend(handles=[Patch(fc='#cfe3f7', ec='#2b6cb0', label='CHIP LLC parcels (private)'),
                   Patch(fc='#f3e3b3', ec='#b8963c', label='Reclamation land (Newlands Project)'),
                   Patch(fc='#d62828', ec='#8b0000', label='Corner crossing wings, 500 ft (this application)'),
                   Line2D([0], [0], color='#2a9d8f', lw=2.5, ls='--', label='Hart Lane access (future application)'),
                   Line2D([0], [0], color='#777777', lw=0.8, ls=':', label='Section lines')], loc='lower left', fontsize=8, framealpha=0.95)
x0, y0 = ax.get_xlim()[1]-pad*0.4-5280, ax.get_ylim()[0]+pad*0.4
ax.plot([x0, x0+5280], [y0, y0], color='k', lw=2); ax.text(x0+2640, y0+250, '1 mile', ha='center', fontsize=8)
ax.annotate('N', xy=(ax.get_xlim()[1]-pad*0.4, ax.get_ylim()[1]-pad*0.3), xytext=(ax.get_xlim()[1]-pad*0.4, ax.get_ylim()[1]-pad*0.9),
            ha='center', fontsize=10, fontweight='bold', arrowprops=dict(arrowstyle='-|>', color='k'))
ax.set_title('Figure 1. CHIP corner crossings on Reclamation land (T.19-20N., R.26E., MDM)', fontsize=11)
fig.text(0.5, 0.02, 'Schematic for discussion. Parcels and Reclamation land from CHIP master map; sections from BLM CadNSDI; wings redrawn at 500 ft by Permitting Desk. Not survey grade.', ha='center', fontsize=7, color='#555555')
fig.savefig(OUT + '/Fig1_CHIP_crossings_overview.png', dpi=200, bbox_inches='tight'); plt.close(fig)

# ---- Figure 2: one crossing detail ----
fig, ax = plt.subplots(figsize=(7, 7))
base(ax, labels=False)
cw = [x for x in W5 if x[0] == 'Corner Crossing 1']
for cr, sec, pts, a in cw:
    ax.add_patch(MPoly(pts, closed=True, fc='#d62828', ec='#8b0000', lw=1.2, alpha=0.85, zorder=6))
    cx = sum(p[0] for p in pts)/3; cy = sum(p[1] for p in pts)/3
    ax.text(cx, cy, f'{a:.2f} ac', ha='center', va='center', fontsize=8, color='white', fontweight='bold', zorder=7)
c = cw[0][2][0]
# draw corridor centerline and width marker across the corner, perpendicular to the diagonal through the wings
p1 = cw[0][2]; p2 = cw[1][2]
ax.plot(*c, 'ko', ms=4, zorder=8); ax.text(c[0]+40, c[1]+40, 'section corner', fontsize=8, zorder=8)
ax.text(c[0], c[1]-560, 'Each wing: legs ~354 ft on the section lines, ~1.43 ac\nTwo wings per crossing: ~2.87 ac\nCorridor ~500 ft wide measured across the corner\nSeven wings in four crossings: ~10.0 ac', ha='center', va='top', fontsize=8,
        bbox=dict(fc='white', ec='#999999'), zorder=9)
ax.set_xlim(c[0]-900, c[0]+900); ax.set_ylim(c[1]-1100, c[1]+700)
ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
ax.plot([c[0]+450, c[0]+750], [c[1]+600, c[1]+600], 'k', lw=2); ax.text(c[0]+600, c[1]+620, '300 ft', ha='center', fontsize=7)
ax.set_title('Figure 2. Typical corner crossing (Crossing 1), 500-ft configuration', fontsize=11)
ax.legend(handles=[Patch(fc='#cfe3f7', ec='#2b6cb0', label='CHIP LLC parcel (private)'), Patch(fc='#f3e3b3', ec='#b8963c', label='Reclamation land'),
                   Patch(fc='#d62828', ec='#8b0000', label='Requested crossing wing')], loc='upper left', fontsize=8)
fig.savefig(OUT + '/Fig2_crossing_detail.png', dpi=200, bbox_inches='tight'); plt.close(fig)
