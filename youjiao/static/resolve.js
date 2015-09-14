var path = require('path');
var vendorjs = path.resolve(__dirname, 'vendor/js');
var vendorcss = path.resolve(__dirname, 'vendor/css');
var cssdir = path.resolve(__dirname, 'src/css');

var resolve = {
    alias: {
        maincss: path.resolve(cssdir, 'main.sass'),
        normalize: path.resolve(vendorcss, 'normalize.css'),
        slides: path.resolve(vendorjs, 'responsiveslides.js'),
        body: path.resolve(vendorcss, 'body.css')
    }
};

module.exports = resolve;