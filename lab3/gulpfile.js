const gulp = require("gulp");
const browserSync = require("browser-sync").create();
const watch = require("gulp-watch");

function task1(cb) {
  setTimeout(cb, 2000);
}

function task2(cb) {
  setTimeout(cb, 1000);
}

gulp.task("serve", function () {
  browserSync.init({
    server: {
      baseDir: "./",
    },
    injectChanges: true,
  });

  gulp.watch("**/*.html").on("change", browserSync.reload);
  gulp.watch("**/*.css").on("change", browserSync.reload);
  gulp.watch("**/*.js").on("change", browserSync.reload);
  gulp.watch("**/*.php").on("change", browserSync.reload);
});

// exports.default = gulp.parallel(task1, task2);
// exports.default = gulp.series(task1, task2);
