var gulp = require('gulp');
var sass = require('gulp-sass');
var minifyCss = require('gulp-minify-css');
var uglify = require('gulp-uglify');

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

gulp.task('uglify', function(){
    return gulp.src('src/js/*.js')
                .pipe(uglify())
                .pipe(gulp.dest('build/js'))
});

gulp.task('file:watch', function () {
    gulp.watch('src/css/**/*.sass', ['sass']);
    gulp.watch('src/js/*.js', ['uglify']);
});

gulp.task('default', ['minify-css', 'uglify']);