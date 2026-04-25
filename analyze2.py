import re

src = r'C:\Users\dian\.openclaw\media\qqbot\downloads\drone-defense-system-v3_1777135238184_8d6f5d.html'
f = open(src, 'r', encoding='utf-8')
c = f.read()
f.close()

# Find all slide titles (h2 with class="slide-title")
titles = re.findall(r'<h2 class="slide-title">(.*?)</h2>', c)
print(f"Found {len(titles)} slide titles:")
for i, t in enumerate(titles):
    print(f"  {i+1}. {t}")

# Find slide structure: <!-- 第X页 -->
slides = re.findall(r'<!-- (\u7b2c\d+\u9875.*?) -->', c)
print(f"\nSlide markers: {len(slides)}")
for s in slides:
    print(f"  {s}")

# Total <div class="slide"s
divs = len(re.findall(r'<div class="slide', c))
print(f"\nTotal slide divs: {divs}")

# Find id attributes
ids = re.findall(r'id="slide-(\d+)"', c)
print(f"Slide IDs: {ids}")
