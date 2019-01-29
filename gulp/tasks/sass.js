const path = require('path')
const sourcemaps = require('gulp-sourcemaps')
const sass = require('gulp-sass')
const postcss = require('gulp-postcss')
const cssnano = require('cssnano')
const autoprefixer = require('autoprefixer')

module.exports = (gulp, config) => {
  var sassOptions = {
    outputStyle: 'compressed',
    includePaths: config.sassIncludePaths ? config.sassIncludePaths : []
  }

  gulp.task('sass', () =>
    gulp.src(config.sassPath, {cwd: config.sourcePath})
      .pipe(sourcemaps.init())
      .pipe(sass(sassOptions).on('error', sass.logError))
      .pipe(postcss([
        autoprefixer(),
        cssnano()
      ]))
      .pipe(sourcemaps.write('.'))
      .pipe(gulp.dest('stylesheets', {cwd: config.destinationPath}))
  )
}
