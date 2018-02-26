var gulp = require('gulp'),
  livereload = require('gulp-livereload'),
  runSequence = require('run-sequence'),
  config = require('../config');


gulp.task('watch', function(cb) {
  // Start livereload server first, so compile actions are also caught.
  // Dynamically look for all tasks ending in :watch, like sass:watch
  livereload.listen(config.livereload_options);
  const watchTasks = Object.keys(gulp.tasks).filter(name => name.endsWith(':watch'));
  runSequence(watchTasks, cb);
});
