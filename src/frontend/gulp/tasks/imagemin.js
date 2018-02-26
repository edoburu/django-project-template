const gulp = require('gulp'),
      plumber = require('gulp-plumber'),
      imagemin = require('gulp-imagemin'),
      imageminPngquant = require('imagemin-pngquant'),
      imageminMozjpeg = require('imagemin-mozjpeg'),
      config = require('../config');


gulp.task('imagemin', function () {
  return gulp.src(config.paths.images + '**/*.{png,jpg,jpeg}')
    .pipe(plumber())
    .pipe(imagemin({
      use: [
        imageminPngquant(config.pngquant_options),
        imageminMozjpeg(config.mozjpeg_options)
      ]
    }))
    .pipe(gulp.dest(config.paths.images));
});
