'use strict';

var gulp = require('gulp'),
    copy = require('gulp-copy'),
    merge = require('merge-stream'),
    config = require('../config');


gulp.task('vendor', function (cb) {
  // Create streams for all copy tasks
  var streams = config.copy_files.map(function(item){
    for(let src of item.src) {
      src = src.substring(src.lastIndexOf('/') + 1);
      console.log("vendor: create " + item.dest + src)
    }
    return gulp.src(item.src).pipe(gulp.dest(item.dest));
  });

  // Return a merged stream to handle both `end` events
  return merge.apply(streams);
});
