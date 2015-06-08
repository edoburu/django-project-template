/*
 * This is an experiment to compass Sass files using Gulp + libsass
 * instead of the standard Ruby + Sass + Compass.
 *
 * - install nodejs  (OSX: brew install node)
 * - run: npm install
 * - run: ./node_modules/.bin/gulp or npm run gulp
 *
 * Install livereload to enjoy auto-updating the browser on changes:
 * http://livereload.com/extensions/
 *
 */
'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var livereload = require('gulp-livereload');
var del = require('del');

var paths = {
  sass: './frontend/sass/',
  css: './frontend/static/frontend/css/',
}

paths.sass_glob = paths.sass + '**/*.scss';

var sass_options = {
  // See https://github.com/sass/node-sass
  outputStyle: 'expanded',
  includePaths: [
    './frontend/sass-vendor/',
    './node_modules/bootstrap-sass/assets/stylesheets/',
  ],
  precision: 5,
};

var livereload_options = {
  host: '127.0.0.1',
};

gulp.task('sass', function () {
  // Task to compile sass
  gulp.src(paths.sass_glob)
    .pipe(sourcemaps.init())
    .pipe(sass(sass_options).on('error', sass.logError))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(paths.css))
    .pipe(livereload());
});

gulp.task('sass:watch', ['sass'], function () {
  // Watch and recompile on changes
  livereload.listen(livereload_options);
  gulp.watch(paths.sass_glob, ['sass'])
    .on('change', function(evt) {
        console.log('[watcher] File ' + evt.path.replace(/.*(?=sass)/,'') + ' was ' + evt.type + ', compiling...');
    });
});

gulp.task('clean', function (cb) {
  // clean task
  del([paths.css + '*.css', '!' + paths.css + 'user-styles.css'], cb);
});

// Default actions
gulp.task('default', ['sass:watch']);
