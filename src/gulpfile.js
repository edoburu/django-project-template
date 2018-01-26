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

var gulp = require('gulp'),
    sass = require('gulp-sass'),
    sourcemaps = require('gulp-sourcemaps'),
    livereload = require('gulp-livereload'),
    del = require('del'),
    notify = require('gulp-notify');

var paths = {
  sass: './frontend/sass/',
  css: './frontend/static/frontend/css/',
  img: './frontend/static/frontend/img/',
  spriteInput: './frontend/static/frontend/img/sprite/*.png',
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

var spritesmith_options = {
  imgName: 'sprite.png',
  imgPath: '../img/sprite.png',  // for relative CSS URL
  cssName: '_sprites.scss',
  //groupBy: foldername
  //padding: 1,
  //retinaSrcFilter: ['*@2x.png'],
  //retinaImgName: 'sprite@2x.png',
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

gulp.task('sprite', function () {
  // Sprite task
  // https://github.com/twolfson/gulp.spritesmith
  var spritesmith = require('gulp.spritesmith');
  var sprites =
  gulp.src(paths.spriteInput)
    .pipe(spritesmith(spritesmith_options));

  // Continue in separate streams (also allows adding imagemin to the img pipe)
  sprites.img.pipe(gulp.dest(paths.img));
  sprites.css.pipe(gulp.dest(paths.sass));
});

gulp.task('clean', function (cb) {
  // clean task
  del([paths.css + '*.css', '!' + paths.css + 'user-styles.css'], cb);
});

// Default actions
gulp.task('default', ['sass:watch']);


function handleErrors(){
  var args = Array.prototype.slice.call(arguments);

  // Send error to notification center with gulp-notify
  notify.onError({
    title: "Compile Error",
    message: "<%= error.message %>"
  }).apply(this, args);

  this.emit('end');
}
