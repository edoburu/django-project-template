'use strict';

const gulp = require('gulp'),
  filesExist = require('files-exist'),
  plumber = require('gulp-plumber'),
  size = require('gulp-size'),
  sourcemaps = require('gulp-sourcemaps'),
  merge = require('merge-stream'),
  uglify = require('gulp-uglify'),
  concat = require('gulp-concat'),
  livereload = require('gulp-livereload');


function vendor() {
  // Create streams for all copy tasks
  var config = require('../config');  // reloaded if needed
  var streams = config.copy_files.map(function(item){
    var pipes = [
      gulp.src(filesExist(item.src)),
      plumber()
    ];

    if(item.concat || item.minify) {
      pipes.push(sourcemaps.init());
      if(item.concat) {
        pipes.push(concat(item.concat));
      }
      if(item.minify) {
        // https://github.com/mishoo/UglifyJS2#minify-options
        const options = item.minify instanceof Object ? item.minify : {};
        pipes.push(uglify(options));
      }
      pipes.push(sourcemaps.write());
    }

    pipes.push(
      size({showFiles: true}),
      gulp.dest(item.dest),
      livereload()
    );

    // Merge all pipes
    return pipes.reduce(function (from, to) { return from.pipe(to); });
  });

  // Return a merged stream to handle both `end` events
  return merge(streams);
}


function vendorWatch() {
  // Watch and recompile on changes
  var configfile = require.resolve('../config');
  return gulp.watch(configfile, vendor)
    .on('all', function (event, path, stats) {
      console.log('[watcher] File config.js was ' + event + ', reloading...');
      delete require.cache[configfile];
    });
}

gulp.task('vendor', vendor);
gulp.task('vendor:watch', gulp.series(vendor, vendorWatch));
