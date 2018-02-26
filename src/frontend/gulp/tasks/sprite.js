'use strict';

var gulp = require('gulp'),
    plumber = require('gulp-plumber'),
    merge = require('merge-stream'),
    config = require('../config');


var spritesmith_options = {
  spritesmith: function (options, sprite, icons) {
    // Define the options for this sprite dynamically.
    options.imgPath = '../images/sprites/' + options.imgName;
    options.imgName = 'sprites/' + options.imgName;
    options.cssName = 'sprites/_' + sprite + ".scss";
    options.cssSpritesheetName = 'sp-' + sprite;
    options.cssVarMap = function (icon) {
      icon.name = sprite + '-' + icon.name;
    };
    options.cssOpts = {
      'functions': false,
    };

    if (options.retinaImgName) {
      options.retinaImgPath = '../images/sprites/' + options.retinaImgName;
      options.retinaImgName = 'sprites/' + options.retinaImgName;
      options.cssRetinaSpritesheetName = 'sp-' + sprite + '-retina';
    }

    delete options.cssTemplate;
  }
  //padding: 1,
  //retinaSrcFilter: ['*@2x.png']
};


gulp.task('sprite', function () {
  // Sprite task
  // https://github.com/twolfson/gulp.spritesmith
  // https://github.com/reducejs/gulp.spritesmith-multi
  var spritesmith = require('gulp.spritesmith-multi');
  var sprites =
    gulp.src(config.paths.spriteInput)
      .pipe(plumber())
      .pipe(spritesmith(spritesmith_options));

  // Continue in separate streams (also allows adding imagemin to the img pipe)
  var imgStream = sprites.img.pipe(gulp.dest(config.paths.images));
  var cssStream = sprites.css.pipe(gulp.dest(config.paths.sass));

  // Return a merged stream to handle both `end` events
  return merge(imgStream, cssStream)
});
