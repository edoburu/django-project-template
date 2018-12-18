const gulp = require('gulp'),
  livereload = require('gulp-livereload'),
  config = require('../config');


gulp.task('watch', function watchFactory(done) {
  // Start livereload server first, so compile actions are also caught.
  // Dynamically look for all tasks ending in :watch, like sass:watch
  livereload.listen(config.livereload_options);
  const watchTasks = gulp.tree().nodes.filter(name => name.endsWith(':watch')).sort();
  if(watchTasks.length == 0) {
    const up = new Error("No '...:watch' tasks found");
    up.showStack = false;
    throw up;
  }
  console.log("Starting watchers " + watchTasks.join(', '));
  return gulp.parallel(watchTasks)(done);
});
