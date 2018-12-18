'use strict';

const gulp = require('gulp'),
  del = require('del'),
  config = require('../config');

function clean() {
  // clean task
  return del([
    config.paths.css + '*.css',
    config.paths.vendor,
    '!' + config.paths.css + 'user-styles.css'
  ]);
}

gulp.task('clean', clean);
