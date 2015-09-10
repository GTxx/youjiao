var path = require('path');
var dirname = path.resolve(__dirname, 'vendor/js');
var cssdir = path.resolve(__dirname, 'src/css');

var resolve = {
    alias: {
        maincss: path.resolve(cssdir, 'main.sass'),
        slides: path.resolve(dirname, 'responsiveslides.js')
    }
};

module.exports = resolve;