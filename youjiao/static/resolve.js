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
        videojs_ie8_js: path.resolve(node_module_path, 'videojs-ie8/dist/videojs-ie8.min.js'),
        area_js: path.resolve(vendorjs, 'area.js'),
        //plupload_js: path.resolve(vendorjs, 'plupload/plupload.dev.js'),
        //moxie_js: path.resolve(vendorjs, 'plupload/moxie.js'),
        //qiniu_js: path.resolve(vendorjs, 'qiniu.js'),
    }
};

module.exports = resolve;