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
  requireDir = require('require-dir'),
  runSequence = require('run-sequence');


// Import all tasks
requireDir('./frontend/gulp/tasks', {recurse: true});

// Define default task
gulp.task('default', function(cb) {
  runSequence('clean', ['vendor', 'imagemin', 'sass'], cb);
});
