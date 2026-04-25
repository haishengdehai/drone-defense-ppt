"""Generate V8 slides HTML content (append to existing CSS)"""
import sys

sl = []

# Helper: wrap slide div
def slide(content, active=False):
    cls = ' slide active' if active else ''
    return '<div class="slide' + cls + '">' + content + '</div>\n'

# S1: COVER
sl.append(slide('
<div class="sc" style="height:100%">
<div class="rw">
<div class="rc"></div><div class="rc"></div><div class="rc"></div><div class="rc"></div>
<div class="rs"></div>
<div class="rd" style="top:22%;left:54%"></div><div class="rd" style="top:48%;left:30%;animation-delay:.7s"></div>
<div class="rd" style="top:38%;left:65%;animation-delay:1.4s"></div><div class="rd" style="top:52%;left:46%;animation-delay:.3s"></div>
<div class="sp"></div><div class="sp sp2"></div><div class="sp sp3"></div>
</div>
<div class="h1" style="margin-bottom:3px">\u65e0\u4eba\u673a\u7efc\u5408\u9632\u63a7\u7cfb\u7edf</div>
<div class="sub" style="font-size:.9rem;margin-bottom:14px">\u5168\u57df\u611f\u77e5 \u00b7 \u667a\u80fd\u8bc6\u522b \u00b7 \u7cbe\u51c6\u53cd\u5236</div>
<div style="display:flex;gap:25px;justify-content:center;flex-wrap:wrap;margin-bottom:10px">
<div style="text-align:center"><div class="kpi">5\u201315km</div><div style="font-size:.7rem;color:var(--fg2);margin-top:2px">\u63a2\u6d4b\u8ddd\u79bb</div></div>
<div style="text-align:center"><div class="kpi">\u226595%</div><div style="font-size:.7rem;color:var(--fg2);margin-top:2px">\u8bc6\u522b\u51c6\u786e\u7387</div></div>
<div style="text-align:center"><div class="kpi">&lt;60s</div><div style="font-size:.7rem;color:var(--fg2);margin-top:2px">\u5168\u6d41\u7a0b\u54cd\u5e94</div></div>
<div style="text-align:center"><div class="kpi kpi-o">4+1</div><div style="font-size:.7rem;color:var(--fg2);margin-top:2px">\u5b50\u7cfb\u7edf\u67b6\u6784</div></div>
</div>
<div><span class="tag">\u76f8\u63a7\u9635\u96f7\u8fbe</span><span class="tag">\u53cc\u6ce2\u6bb5\u5149\u7535</span><span class="to">\u7a7a\u7ba1\u878d\u5408</span><span class="tr">\u591a\u624b\u6bb5\u53cd\u5236</span><span class="tg">AI\u51b3\u7b56</span></div>
</div>
''', active=True)

# S2: BACKGROUND
sl.append(slide('''
<div class="sl">BACKGROUND</div>
<div class="h2">\u80cc\u666f\u4ecb\u7ecd</div>
<div class="sub">\u4f4e\u7a7a\u5b89\u5168\u5a01\u80c1\u6001\u52bf\u4e0e\u9632\u5fa1\u9700\u6c42</div>
<div class="g2" style="flex:1;min-height:0">
<div class="col">
<div class="card" style="flex:1">
<div class="ct" style="text-align:center">\u4f4e\u7a7a\u5b89\u5168\u5a01\u80c1\u8d8b\u52bf</div>
<svg viewBox="0 0 380 160" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">
<defs><linearGradient id="tg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="rgba(0,153,204,.15)"/><stop offset="100%" stop-color="rgba(0,153,204,.02)"/></linearGradient></defs>
<polyline points="30,130 55,118 85,108 110,88 140,72 170,58 200,45 230,32" fill="none" stroke="var(--ac)" stroke-width="1.5" opacity=".7"/>
<polyline points="30,130 55,118 85,108 110,88 140,72 170,58 200,45 230,32" fill="url(#tg1)"/>
<text x="30" y="148" fill="var(--fg3)" font-size="7">2018</text><text x="230" y="148" fill="var(--fg3)" font-size="7">2025</text>
<text x="235" y="26" fill="var(--ac2)" font-size="7" opacity=".8">+423%</text>
<circle cx="230" cy="32" r="2.5" fill="var(--ac2)"/>
<line x1="230" y1="32" x2="290" y2="22" stroke="var(--fg3)" stroke-width=".5" stroke-dasharray="2,2"/>
<text x="295" y="26" fill="var(--fg2)" font-size="6.5">300+\u4e07\u67b6\u4f4e\u6162\u5c0f\u76ee\u6807</text>
<text x="30" y="18" fill="var(--fg2)" font-size="6.5">\u6d88\u8d39\u7ea7\u65e0\u4eba\u673a\u4fdd\u6709\u91cf\u5e74\u589e>30%</text>
</svg>
</div>
<div class="card"><div class="ct">\u5a01\u80c1\u4e8b\u4ef6</div>
<ul class="ul">
<li><span class="hlo">\u673a\u573a\u4fb5\u5165</span> \u2014 2017\u6210\u90fd\u53cc\u6d4158\u67b6\u5907\u964d</li>
<li><span class="hlo">\u519b\u4e8b\u4fa6\u5bdf</span> \u2014 \u65e0\u4eba\u673a\u975e\u6cd5\u822a\u62cd\u57fa\u5730</li>
<li><span class="hlo">\u96c6\u7fa4\u9971\u548c</span> \u2014 \u6570\u5341\u67b6\u540c\u65f6\u7a81\u9632</li>
<li><span class="hlo">\u8702\u7fa4\u534f\u540c</span> \u2014 \u591a\u673a\u7ec4\u7f51\u52a8\u6001\u89c4\u907f</li>
</ul></div>
</div>
<div class="col">
<div class="card" style="flex:1">
<div class="ct" style="text-align:center">\u4f4e\u6162\u5c0f\u76ee\u6807\u7279\u5f81</div>
<svg viewBox="0 0 380 160" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">
<rect x="10" y="10" width="170" height="50" rx="2" fill="rgba(0,153,204,.06)" stroke="rgba(0,153,204,.2)" stroke-width=".5"/>
<text x="95" y="32" text-anchor="middle" fill="var(--ac)" font-size="8" font-weight="600">RCS</text>
<text x="95" y="48" text-anchor="middle" fill="var(--fg)" font-size="11" font-weight="700">0.001\u20130.1m\u00b2</text>
<rect x="195" y="10" width="175" height="50" rx="2" fill="rgba(0,153,204,.06)" stroke="rgba(0,153,204,.2)" stroke-width=".5"/>
<text x="282" y="32" text-anchor="middle" fill="var(--ac)" font-size="8" font-weight="600">\u98de\u884c\u9ad8\u5ea6</text>
<text x="282" y="48" text-anchor="middle" fill="var(--fg)" font-size="11" font-weight="700">&lt;1000m</text>
<rect x="10" y="72" width="170" height="50" rx="2" fill="rgba(204,85,34,.06)" stroke="rgba(204,85,34,.2)" stroke-width=".5"/>
<text x="95" y="94" text-anchor="middle" fill="var(--ac2)" font-size="8" font-weight="600">\u901f\u5ea6\u8303\u56f4</text>
<text x="95" y="110" text-anchor="middle" fill="var(--fg)" font-size="11" font-weight="700">10\u2013150km/h</text>
<rect x="195" y="72" width="175" height="50" rx="2" fill="rgba(204,85,34,.06)" stroke="rgba(204,85,34,.2)" stroke-width=".5"/>
<text x="282" y="94" text-anchor="middle" fill="var(--ac2)" font-size="8" font-weight="600">FPV\u6210\u672c</text>
<text x="282" y="110" text-anchor="middle" fill="var(--fg)" font-size="11" font-weight="700">&lt;500\u5143</text>
</svg>
</div>
<div class="card"><div class="ct">\u6cd5\u89c4\u4e0e\u4ea7\u4e1a\u9700\u6c42</div>
<ul class="ul">
<li>\u300a\u65e0\u4eba\u9a7e\u9a76\u822a\u7a7a\u5668\u98de\u884c\u7ba1\u7406\u6682\u884c\u6761\u4f8b\u300b2024\u65bd\u884c</li>
<li>\u6c11\u822a\u5c40\u8981\u6c42\u91cd\u70b9\u573a\u6240\u914d\u5907\u53cd\u65e0\u4eba\u673a\u7cfb\u7edf</li>
<li>\u4f4e\u7a7a\u7a7a\u57df\u7ba1\u7406\u6539\u9769\u50ac\u751f\u76d1\u7ba1\u521a\u9700</li>
</ul></div>
</div>
</div>
'''))

print("S1+S2 generated")
print("SLIDES:", len(sl))
print("TOTAL CHARS:", sum(len(s) for s in sl))

# Output as chunks
out = ''.join(sl)
# Write to a temp file
with open(r'C:\Users\dian\.openclaw\workspace\drone-defense-ppt\_slides1.html', 'w', encoding='utf-8') as f:
    f.write(out)
print("Written to _slides1.html")
