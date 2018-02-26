'use strict';

var gulp = require('gulp'),
    filesExist = require('files-exist'),
    plumber = require('gulp-plumber'),
    sass = require('gulp-sass'),
    sourcemaps = require('gulp-sourcemaps'),
    livereload = require('gulp-livereload'),
    postcss = require('gulp-postcss'),
    notify = require('gulp-notify'),
    autoprefixer = require('autoprefixer'),
    mqpacker = require('css-mqpacker'),
    pump = require('pump'),   config = require('../config');


function handleErrors() {
  var args = Array.prototype.slice.call(arguments);

  // Alternative instead of default sass.logError
  // Send error to Mac notification center with gulp-notify:
  notify.onError({
    title: "Compile Error",
    message: "<%= error.message %>"
  }).apply(this, args);

  this.emit('end');
}


gulp.task('sass', function () {
  // Task to compile sass
  return gulp.src(filesExist(config.paths.sass_glob))
    .pipe(plumber({errorHandler: handleErrors}))
    .pipe(sourcemaps.init())
    .pipe(sass(config.sass_options))
    .pipe(postcss([
      // All postcss processing once, no reparsing of CSS is done here.
      autoprefixer(config.autoprefixer_options),
      mqpacker({sort: true})  // combine media queries
    ]))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(config.paths.css))
    .pipe(livereload())
});


gulp.task('sass:watch', ['sass'], function () {
  // Watch and recompile on changes
  return gulp.watch(config.paths.sass_glob, ['sass'])
    .on('change', function (evt) {
      console.log('[watcher] File ' + evt.path.replace(/.*(?=sass)/, '') + ' was ' + evt.type + ', compiling...');
    });
});
