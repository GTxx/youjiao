var gulp = require('gulp');
var sass = require('gulp-sass');
var minifyCss = require('gulp-minify-css');

gulp.task('sass', function () {
    return gulp.src('src/css/*.sass')
                .pipe(sass.sync().on('error', sass.logError))
                .pipe(gulp.dest('build/css'));
});

gulp.task('minify-css', ['sass'], function () {
    return gulp.src('build/css/*.css')
                .pipe(minifyCss({compatibility: 'ie8'}))
                .pipe(gulp.dest('build/css'));
});

gulp.task('sass:watch', function () {
    gulp.watch('src/css/*.sass', ['sass'])
});

gulp.task('default', ['minify-css']);