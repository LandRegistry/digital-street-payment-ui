const path = require('path')
const spawn = require('child_process').spawn

module.exports = (gulp, config) => {
  gulp.task('jquery', () => {
    try {
      return gulp
        .src(require.resolve('jquery/dist/jquery.min.js'))
        .pipe(gulp.dest(path.join(config.destinationPath, 'javascripts')))
    } catch (e) {
      // jQuery not installed, just continue
      return Promise.resolve()
    }
  })

  gulp.task('js-vendor', () =>
    gulp
      .src(path.join(config.sourcePath, 'javascripts/vendor/*'))
      .pipe(gulp.dest(path.join(config.destinationPath, 'javascripts/vendor')))
  )

  gulp.task('js', () => {
    var webpackArgs
    var webpack

    if (process.argv.includes('watch')) {
      webpackArgs = ['--watch', '--info-verbosity', 'verbose']
    } else {
      // If we're not running in dev mode, make webpack be quiet
      webpackArgs = ['--display', 'errors-only']
    }

    if (!/^win/.test(process.platform)) { // linux or mac
      webpack = spawn('webpack', webpackArgs)
    } else { // windows
      webpackArgs.unshift('/s', '/c', 'webpack')
      webpack = spawn('cmd', webpackArgs)
    }

    webpack.stdout.on('data', data => {
      console.log(data.toString())
    })

    webpack.stderr.on('data', data => {
      console.log(data.toString())
    })

    return webpack
  })
}
