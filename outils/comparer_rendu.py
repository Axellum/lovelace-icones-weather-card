"""Compare au pixel le rendu Chromium de deux dossiers d'icônes, à plusieurs instants de l'animation.

Usage : python outils/comparer_rendu.py <dossier_avant> <dossier_apres>
Besoin : pip install playwright pillow numpy, puis python -m playwright install chromium.

Chaque icône est rendue seule (64 px, densité 4), animations figées au même instant.
Écart = part des pixels dont un canal change de plus de 8/255. Référence : un dossier contre lui-même donne 0.
"""
import io
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

INSTANTS = [0, 700, 1900, 3300, 5100]  # ms


def capture(page, chemin):
    page.goto(chemin.resolve().as_uri())
    page.wait_for_timeout(50)
    images = []
    for t in INSTANTS:
        page.evaluate("t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; })", t)
        page.wait_for_timeout(30)
        png = page.screenshot(omit_background=True)
        images.append(np.asarray(Image.open(io.BytesIO(png)).convert("RGBA"), dtype=np.int16))
    return images, page.evaluate("document.getAnimations().length")


def main():
    avant, apres = Path(sys.argv[1]), Path(sys.argv[2])
    with sync_playwright() as p:
        nav = p.chromium.launch()
        page = nav.new_page(viewport={"width": 64, "height": 64}, device_scale_factor=4)
        pire = 0.0
        for f in sorted(avant.glob("*.svg")):
            a, na = capture(page, f)
            b, nb = capture(page, apres / f.name)
            part = max(float((np.abs(x - y).max(axis=2) > 8).mean()) for x, y in zip(a, b))
            pire = max(pire, part)
            print(f"{f.name:<24} animations {na:>2} -> {nb:<2} pixels différents {100 * part:5.2f} %")
        nav.close()
        print(f"pire : {100 * pire:.2f} %")


if __name__ == "__main__":
    main()
