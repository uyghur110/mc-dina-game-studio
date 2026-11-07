"""Usage: python configure.py https://USERNAME.github.io/REPOSITORY/"""
from pathlib import Path
from urllib.parse import urlparse
from html import escape
import re, sys
base = sys.argv[1].rstrip('/') + '/' if len(sys.argv) == 2 else ''
u = urlparse(base)
if u.scheme != 'https' or not u.netloc or u.query or u.fragment:
    raise SystemExit('Supply your approved HTTPS website base URL, without query or fragment.')
p = Path(__file__).resolve().parent
s = (p/'index.html').read_text(encoding='utf-8')
s = re.sub(r'<link rel="canonical"[^>]*>|<meta property="og:url"[^>]*>', '', s)
s = s.replace('</head>', f'<link rel="canonical" href="{escape(base, quote=True)}"><meta property="og:url" content="{escape(base, quote=True)}"></head>')
(p/'index.html').write_text(s, encoding='utf-8')
(p/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n', encoding='utf-8')
(p/'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{escape(base)}</loc></url></urlset>\n', encoding='utf-8')
print('Configured canonical URL, Open Graph URL, robots.txt, and sitemap.xml.')
