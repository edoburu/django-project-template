'use strict';

const autoprefixer = require('autoprefixer'),
  mqpacker = require('css-mqpacker'),
  cssnano = require('cssnano'),
  flexbugsFixes = require('postcss-flexbugs-fixes'),
  removeSelectors = require("postcss-remove-selectors");

const bootstrap = 'node_modules/bootstrap/js/dist/';
const vendor = './frontend/static/frontend/vendor/';

const NODE_ENV = process.env.NODE_ENV;

let postcss_plugins = [
  // All post-processing happens in one batch, no reparsing of CSS is done here.
  removeSelectors({
    selectors: [
      ".accordion",
      //".card",  // only used to extend existing .well
      ".btn-outline",
      ".card-group",  // card-deck makes more sense
      ".card-columns",  // card-deck makes more sense
      ".card-deck .well",  // Fix @extends .card
      ".well > .list-group",  // fix @extends
      ".custom-control-input",
      ".custom-file-input",
      ".custom-select",
      ".invalid-tooltip",
      ".display-1",
      ".display-2",
      ".display-3",
      ".display-4",
      ".form-control-file",
      ".form-control-plaintext",
      ".form-control-sm",
      ".form-control-lg",
      ".form-control.is-valid",
      ".form-check-input.is-valid",
      ".nav-pills",
      ".nav-tabs",
      ".show > .btn",
      ".navbar-dark",
      ".navbar-expand ", // only md
      ".pagination-lg",
      ".pagination-sm",
      ".table .thead-dark",
      ".table .thead-light",
      ".table-active",
      ".table-bordered",
      ".table-borderless",
      ".table-danger",
      ".table-dark",
      ".table-hover",
      ".table-light",
      ".table-info",
      ".table-primary",
      ".table-success",
      ".table-responsive",
      ".table-secondary",
      ".table-striped",
      ".table-warning",
      ".order-",
      ".valid-feedback",
      ".valid-tooltip",
      ".was-validated",
    ]
  }),
  flexbugsFixes(),
  autoprefixer({
    cascade: false
  }),
  mqpacker({sort: true})  // combine media queries
];

if(NODE_ENV === 'production') {
  postcss_plugins.push(cssnano());
}


module.exports = {
  paths: {
    sass: './frontend/sass/',
    sass_glob: './frontend/sass/**/*.scss',
    css: './frontend/static/frontend/css/',
    images: './frontend/static/frontend/images/',
    vendor: vendor
  },

  copy_files: [
    {
      src: [
        'node_modules/jquery/dist/jquery.min.js',
        'node_modules/popper.js/dist/umd/popper.min.js'
      ],
      dest: vendor
    },
    {
      src: [
        bootstrap + 'util.js',
        bootstrap + 'collapse.js',  // mobile menu
        bootstrap + 'dropdown.js'  // menu
      ],
      dest: vendor,
      concat: "bootstrap.min.js",
      minify: true
    }
  ],

  sass_options: {
    // See https://github.com/sass/node-sass
    outputStyle: NODE_ENV === 'production' ? 'compressed' : 'expanded',
    includePaths: [
      './frontend/sass-vendor/',
      './node_modules/'
    ],
    precision: 5
  },

  postcss_plugins: postcss_plugins,

  livereload_options: {
    host: '127.0.0.1',
    port: 35729
  },

  mozjpeg_options: {
    quality: 80,
    progressive: true
  },

  pngquant_options: {
    quality: '40-100',
    verbose: true
  }
};
