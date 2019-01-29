const path = require('path')

module.exports = (gulp, config) => {
  gulp.task('appImages', () =>
    gulp
      .src('images/**', {cwd: config.sourcePath})
      .pipe(gulp.dest('images/app', {cwd: config.destinationPath}))
  )

  gulp.task('images', gulp.parallel(['appImages']))
}
