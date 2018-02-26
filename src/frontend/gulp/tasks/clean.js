'use strict';

var gulp = require('gulp'),
    del = require('del'),
    config = require('../config');


gulp.task('clean', function () {
  // clean task
  return del([
    config.paths.css + '*.css',
    config.paths.vendor,
    '!' + config.paths.css + 'user-styles.css'
  ]);
});
