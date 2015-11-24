var path = require('path');
var process = require('child_process');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var AssetsPlugin = require('assets-webpack-plugin');
var webpack = require('webpack');
var config = require('./webpack.config');

//copy vendor to build without package
function Vendor2BuildPlugin() {
};
Vendor2BuildPlugin.prototype.apply = function (compiler) {
    compiler.plugin('compile', function (params) {
        process.exec('mkdir build', function () {
            process.exec('cp -r vendor build', function () {
                console.log('copy vendor to build');
            });
        });
    });
};


var plugins = [
    new webpack.optimize.CommonsChunkPlugin({
        name: 'commons',
        filename: 'commons.[hash].js',
        chunks: ['home', 'security', 'pages', 'activity', 'courseware', 'product', 'research', 'school', 'userinfo']
    }),
    new ExtractTextPlugin('../css/[name].[hash].css'),
    new webpack.optimize.DedupePlugin(),
    new AssetsPlugin({filename: 'assets.json.py'}),
    new webpack.optimize.UglifyJsPlugin({
        compress: {
            warnings: false
        },
        sourceMap: false
    }),
    new Vendor2BuildPlugin()
];

config.plugins = plugins;
config.output = {
    path: path.resolve(__dirname, 'build/js'),
    filename: '[name].[hash].js'
}

module.exports = config;
