"""Static site generator: python3 tools/build.py  ->  writes public/*.html"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import home, type_ratings, academy, careers, prep, about

OUT = os.path.join(os.path.dirname(__file__), "..", "public")
PAGES = {"index.html": home, "type-ratings.html": type_ratings, "academy.html": academy,
         "careers.html": careers, "prep.html": prep, "about.html": about}

for name, mod in PAGES.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(mod.build())
    print("wrote", name)
