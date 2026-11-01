"""Pré-passe de nettoyage des icônes, avant svgo (configuration : outils/svgo.config.mjs).

Usage, depuis la racine du dépôt (Node.js pour svgo) :
    python outils/nettoyer_svg.py <dossier_source> <dossier_sortie> [--viewbox] [--sans-ombre] [--figer]
    npx svgo@4.1.0 --config outils/svgo.config.mjs -q -f <dossier_sortie> -o <dossier_sortie>

Toujours : préfixes CSS morts (-webkit-, -moz-, -ms-, -o-) retirés, @keyframes et règles de classe
inutilisées retirées (la feuille d'amCharts embarque les animations de toutes les icônes).
--viewbox    : « viewbox » en minuscules est ignoré (le XML est sensible à la casse) et sa valeur est parfois
               fausse (0 0 17 17 pour un dessin de 64 px) ; on pose viewBox="0 0 largeur hauteur", qui garde
               le rendu actuel et laisse l'icône se mettre à l'échelle dans tous les navigateurs.
--sans-ombre : retire le filtre « blur » (ombre à 5 % d'opacité, recalculée à chaque image des animées).
--figer      : jeu fixe, plus aucune animation ; chaque élément animé garde sa position de l'image 0.

Vérifier ensuite le rendu au pixel : outils/comparer_rendu.py.
"""
import re
import sys
from pathlib import Path


def blocs(css):
    """Découpe le CSS en blocs de premier niveau (sélecteur, corps), accolades imbriquées comprises."""
    i, out = 0, []
    while i < len(css):
        j = css.find("{", i)
        if j < 0:
            break
        tete = css[i:j].strip()
        prof, k = 1, j + 1
        while prof and k < len(css):
            prof += {"{": 1, "}": -1}.get(css[k], 0)
            k += 1
        out.append((tete, css[j + 1:k - 1]))
        i = k
    return out


def nettoyer_css(css, classes_utilisees):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    # Propriétés préfixées : toutes doublées par la version standard.
    css = re.sub(r"(?<=[{;\s])-(webkit|moz|ms|o)-[\w-]+\s*:[^;{}]*;", "", css)
    garde, anims_utiles = [], set()
    regles = blocs(css)
    for tete, corps in regles:
        if tete.startswith("@"):
            continue
        noms = re.findall(r"\.([\w-]+)", tete)
        if noms and not any(n in classes_utilisees for n in noms):
            continue
        garde.append((tete, corps))
        for m in re.findall(r"animation(?:-name)?\s*:\s*([^;]+)", corps):
            anims_utiles.update(re.findall(r"[\w-]+", m))
    for tete, corps in regles:
        m = re.match(r"@(?:-\w+-)?keyframes\s+([\w-]+)", tete)
        if m and m.group(1) in anims_utiles and not tete.startswith("@-"):
            garde.append((tete, corps))
    return "\n".join(f"{t}{{{c}}}" for t, c in garde)


def attribut(attrs, nom):
    m = re.search(rf'\s{nom}="([^"]+)"', attrs)
    if not m:
        raise ValueError(f"attribut {nom} absent de la balise <svg>")
    return m.group(1)


def figer(css):
    debut = {}
    for nom, corps in re.findall(r"@keyframes\s+([\w-]+)\s*\{((?:[^{}]*\{[^{}]*\})*)\s*\}", css):
        m0 = re.search(r"(?:^|\})\s*(?:0%|from)\s*\{([^}]*)\}", corps)
        debut[nom] = m0.group(1).strip() if m0 else ""
    css = re.sub(r"@keyframes\s+[\w-]+\s*\{(?:[^{}]*\{[^{}]*\})*\s*\}", "", css)
    return re.sub(r"([^{}]+)\{\s*animation\s*:\s*([\w-]+)[^}]*\}",
                  lambda m: f"{m.group(1).strip()}{{{debut.get(m.group(2), '')}}}", css)


def traiter(txt, viewbox, sans_ombre, figer_anim):
    def racine(m):
        attrs = m.group(1)
        if re.search(r'\sviewbox="', attrs):
            nouveau = ""
            if viewbox:
                nouveau = f' viewBox="0 0 {attribut(attrs, "width")} {attribut(attrs, "height")}"'
            attrs = re.sub(r'\sviewbox="[^"]*"', nouveau, attrs)
        return f"<svg{attrs}>"

    txt = re.sub(r"<svg\b(.*?)>", racine, txt, count=1, flags=re.S)
    classes = set()
    for m in re.findall(r'class="([^"]+)"', txt):
        classes.update(m.split())
    txt = re.sub(r"(<style[^>]*>\s*(?:<!\[CDATA\[)?)(.*?)((?:\]\]>)?\s*</style>)",
                 lambda m: m.group(1) + nettoyer_css(m.group(2), classes) + m.group(3), txt, flags=re.S)
    if figer_anim:
        txt = re.sub(r"(<style[^>]*>)(.*?)(</style>)", lambda m: m.group(1) + figer(m.group(2)) + m.group(3),
                     txt, flags=re.S)
    if sans_ombre:
        txt = re.sub(r'\s+filter="url\(#blur\)"', "", txt)
        txt = re.sub(r"<filter\b[^>]*\bid=\"blur\".*?</filter>", "", txt, flags=re.S)
    return txt


def main():
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.mkdir(parents=True, exist_ok=True)
    for f in sorted(src.glob("*.svg")):
        txt = traiter(f.read_text(encoding="utf-8"), "--viewbox" in sys.argv, "--sans-ombre" in sys.argv,
                      "--figer" in sys.argv)
        (dst / f.name).write_text(txt, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
