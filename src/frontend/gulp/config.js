'use strict';

var bootstrap = 'node_modules/bootstrap-sass/assets/javascripts/';
var vendor = './frontend/static/frontend/vendor/';

var NODE_ENV = process.env.NODE_ENV;

module.exports = {
  paths: {
    sass: './frontend/sass/',
    sass_glob: './frontend/sass/**/*.scss',
    css: './frontend/static/frontend/css/',
    images: './frontend/static/frontend/images/',
    spriteInput: './frontend/static/frontend/images/sprites/*/*.png',
    vendor: vendor
  },

  copy_files: [
    {
      src: [
        'node_modules/jquery/dist/jquery.min.js'
      ],
      dest: vendor
    },
    {
      src: [
        bootstrap + 'bootstrap/collapse.js',
        bootstrap + 'bootstrap/transition.js'
      ],
      dest: vendor + "bootstrap/"
    }
  ],

  sass_options: {
    // See https://github.com/sass/node-sass
    outputStyle: NODE_ENV === 'production' ? 'compressed' : 'expanded',
    includePaths: [
      './frontend/sass-vendor/',
      './node_modules/bootstrap-sass/assets/stylesheets/',
    ],
    precision: 5
  },

  autoprefixer_options: {
    browsers: ['last 2 versions'],
    cascade: false
  },

  livereload_options: {
    host: '127.0.0.1'
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
