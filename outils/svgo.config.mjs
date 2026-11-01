// Configuration svgo 4.1 des icônes, réglée au pixel contre le rendu Chromium des originaux :
// - on garde les classes (animations CSS), les id référencés, les <line> (la CSS cible « .am-weather-sun-shiny line »)
//   et les transform des groupes animés ;
// - nombres à 6 décimales : à 3-4, une ligne de pluie pointillée change de longueur d'un cheveu et un point
//   apparaît ou disparaît au bout ;
// - tracés à 6 décimales, transform à 8, sans y appliquer les transform (sinon le contour des traits de vent bouge).
export default {
  multipass: true,
  floatPrecision: 4,
  plugins: [
    {
      name: "preset-default",
      params: {
        overrides: {
          inlineStyles: false,
          minifyStyles: { usage: true },
          convertShapeToPath: false,
          collapseGroups: false,
          moveGroupAttrsToElems: false,
          moveElemsAttrsToGroup: false,
          convertTransform: { transformPrecision: 8 },
          cleanupNumericValues: { floatPrecision: 6 },
          convertPathData: { applyTransforms: false, floatPrecision: 6 },
        },
      },
    },
  ],
};
