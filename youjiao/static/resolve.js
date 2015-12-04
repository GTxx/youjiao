var path = require('path');
var vendorjs = path.resolve(__dirname, 'vendor/js');
var vendorcss = path.resolve(__dirname, 'vendor/css');
var cssdir = path.resolve(__dirname, 'src/css');
var node_module_path = path.resolve(__dirname, 'node_modules');

var resolve = {
    alias: {
        main_css: path.resolve(cssdir, 'main.sass'),
        normalize_css: path.resolve(vendorcss, 'normalize.css'),
        slides_js: path.resolve(vendorjs, 'responsiveslides.js'),
        area_js: path.resolve(vendorjs, 'area.js'),
        birthday_js: path.resolve(vendorjs, 'bday-picker.min.js'),
        lightbox_css: path.resolve('vendor/lightbox/css/lightbox.css'),
        lightbox_js: path.resolve('vendor/lightbox/js/lightbox.js'),
        taidii_slides_js: path.resolve('vendor/taidii-slides/slides.js'),
        taidii_slides_css: path.resolve('vendor/taidii-slides/style.css'),
        jsoneditor_js: path.resolve('vendor/js/jsoneditor.js'),
        //plupload_js: path.resolve(vendorjs, 'plupload/plupload.dev.js'),
        //moxie_js: path.resolve(vendorjs, 'plupload/moxie.js'),
        //qiniu_js: path.resolve(vendorjs, 'qiniu.js'),
    }
};

module.exports = resolve;