# Lovelace Météo France weather-card - Icones X 4

Complément pour la carte https://github.com/hacf-fr/lovelace-meteofrance-weather-card, proposer par ![Home Assistant Communauté Francophone](https://hacf.fr/).


- Ajout de nouveaux jeux d'icônes en complément de l'original sur HACF.
- Différentiation des icônes sur certains arguments sur tous les jeux pour la compatibilitée de la carte météo france (Brouillard, Orage pluvieux, Pluie-neige, venteux).
- Icones fixes, améliore la compatibilitée sur Google Nest et moins gourments en ressources.
- Icônes allégées (novembre 2026) : environ 70 % plus légères, sans l'ombre floutée qui faisait recalculer les icônes animées à chaque image, et le brouillard des jeux fixes ne bouge plus. Nettoyage fait avec l'aide d'une IA, rendu comparé au pixel dans Chromium ; la recette est dans `outils/`.
- Nouveau jeu `icons_5` (novembre 2026) : les icônes fixes blanches redessinées pour remplir tout le cadre, plus lisibles en petit. Ce sont aussi les dessins des icônes météo de mes écrans ESPHome / LVGL ([police et doc](https://github.com/Axellum/M5-Tab5-ESPHome-LVGL/tree/main/Tab5/fonts/icone_meteo)).


## Installation:

1/ Ajouter les dossiers avec les nouvelles icones disponible dans le dossier "dist" dans le dossier "/config/www/community/lovelace-meteofrance-weather-card/" de votre Home Assitant par ftp.

2/ Choisissez votre jeux d'icones:

Icônes animées bleus: 
```yaml
/local/community/lovelace-meteofrance-weather-card/icons/ 
```

Icônes fixes bleus: 
```yaml
/local/community/lovelace-meteofrance-weather-card/icons_1/ 
```

Icônes animées blancs: 
```yaml
/local/community/lovelace-meteofrance-weather-card/icons_2/ 
```

Icônes fixe blancs: 
```yaml
/local/community/lovelace-meteofrance-weather-card/icons_3/ 
```

Icônes fixes blancs (variation 01): 
```yaml
/local/community/lovelace-meteofrance-weather-card/icons_4/ 
```

Icônes fixes blancs, agrandis (variation 02): 
```yaml
/local/community/lovelace-meteofrance-weather-card/icons_5/ 
```


### Icones animés bleus:
![](/dist/icons/day.svg)
![](/dist/icons/night.svg)

![](/dist/icons/windy-night.svg)
![](/dist/icons/windy.svg)
![](/dist/icons/fog.svg)


![](/dist/icons/cloudy.svg)
![](/dist/icons/cloudy-day-3.svg)

![](/dist/icons/cloudy-night-3.svg)
![](/dist/icons/lightning-rainy.svg)
![](/dist/icons/rainy-5.svg)
![](/dist/icons/rainy-6.svg)


![](/dist/icons/rainy-7.svg)
![](/dist/icons/snowy-6.svg)
![](/dist/icons/snowy-rainy.svg)
![](/dist/icons/thunder.svg)


### Icones fixes bleus:
![](/dist/icons_1/day.svg)
![](/dist/icons_1/night.svg)
![](/dist/icons_1/windy-night.svg)
![](/dist/icons_1/windy.svg)

![](/dist/icons_1/fog.svg)
![](/dist/icons_1/cloudy.svg)
![](/dist/icons_1/cloudy-day-3.svg)
![](/dist/icons_1/cloudy-night-3.svg)

![](/dist/icons_1/lightning-rainy.svg)
![](/dist/icons_1/rainy-5.svg)
![](/dist/icons_1/rainy-6.svg)
![](/dist/icons_1/rainy-7.svg)

![](/dist/icons_1/snowy-6.svg)
![](/dist/icons_1/snowy-rainy.svg)
![](/dist/icons_1/thunder.svg)


### Icones animées blancs:
![](/dist/icons_2/day.svg)
![](/dist/icons_2/night.svg)
![](/dist/icons_2/windy-night.svg)
![](/dist/icons_2/windy.svg)

![](/dist/icons_2/fog.svg)
![](/dist/icons_2/cloudy.svg)
![](/dist/icons_2/cloudy-day-3.svg)
![](/dist/icons_2/cloudy-night-3.svg)

![](/dist/icons_2/lightning-rainy.svg)
![](/dist/icons_2/rainy-5.svg)
![](/dist/icons_2/rainy-6.svg)
![](/dist/icons_2/rainy-7.svg)

![](/dist/icons_2/snowy-6.svg)
![](/dist/icons_2/snowy-rainy.svg)
![](/dist/icons_2/thunder.svg)


### Icones fixes blancs:
![](/dist/icons_3/day.svg)
![](/dist/icons_3/night.svg)
![](/dist/icons_3/windy-night.svg)
![](/dist/icons_3/windy.svg)

![](/dist/icons_3/fog.svg)
![](/dist/icons_3/cloudy.svg)
![](/dist/icons_3/cloudy-day-3.svg)
![](/dist/icons_3/cloudy-night-3.svg)

![](/dist/icons_3/lightning-rainy.svg)
![](/dist/icons_3/rainy-5.svg)
![](/dist/icons_3/rainy-6.svg)
![](/dist/icons_3/rainy-7.svg)

![](/dist/icons_3/snowy-6.svg)
![](/dist/icons_3/snowy-rainy.svg)
![](/dist/icons_3/thunder.svg)


### Icones fixe blancs (variation 1):
![](/dist/icons_4/day.svg)
![](/dist/icons_4/night.svg)
![](/dist/icons_4/windy-night.svg)
![](/dist/icons_4/windy.svg)

![](/dist/icons_4/fog.svg)
![](/dist/icons_4/cloudy.svg)
![](/dist/icons_4/cloudy-day-3.svg)
![](/dist/icons_4/cloudy-night-3.svg)

![](/dist/icons_4/lightning-rainy.svg)
![](/dist/icons_4/rainy-5.svg)
![](/dist/icons_4/rainy-6.svg)
![](/dist/icons_4/rainy-7.svg)

![](/dist/icons_4/snowy-6.svg)
![](/dist/icons_4/snowy-rainy.svg)
![](/dist/icons_4/thunder.svg)


### Icones fixes blancs agrandis (variation 2):
![](/dist/icons_5/day.svg)
![](/dist/icons_5/night.svg)
![](/dist/icons_5/windy-night.svg)
![](/dist/icons_5/windy.svg)

![](/dist/icons_5/fog.svg)
![](/dist/icons_5/cloudy.svg)
![](/dist/icons_5/cloudy-day-3.svg)
![](/dist/icons_5/cloudy-night-3.svg)

![](/dist/icons_5/lightning-rainy.svg)
![](/dist/icons_5/rainy-5.svg)
![](/dist/icons_5/rainy-6.svg)
![](/dist/icons_5/rainy-7.svg)

![](/dist/icons_5/snowy-6.svg)
![](/dist/icons_5/snowy-rainy.svg)
![](/dist/icons_5/thunder.svg)



Les icônes fixe viennent de https://icon-icons.com/fr/pack/The-Weather-is-Nice-Today/1370, création de Laura Reen. J'ai parfois apporté de légère modifications. Le jeu `icons_5` reprend `icons_4`, agrandi en 2026 ; il n'avait pas `cloudy-night-3`, `rainy-6` ni `windy-night` : ces trois-là ont été agrandies comme leurs voisines (`cloudy-day-3`, `rainy-5`, `cloudy-night-2`), avec l'aide d'une IA.
Les icônes animés bleus sont issus de https://www.amcharts.com/free-animated-svg-weather-icons/, avec modifications sur certain pour les compléter.
Les icônes animés blancs arrivent de https://github.com/fineemb/lovelace-colorfulclouds-weather-card, avec modifications de positionnement.
