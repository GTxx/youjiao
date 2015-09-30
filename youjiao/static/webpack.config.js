var path = require('path');
var webpack = require('webpack');
var entry = require('./entry');
var resolve = require('./resolve.js');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var AssetsPlugin = require('assets-webpack-plugin');
var process = require('child_process');

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
        filename: 'commons.js',
        chunks: ['home', 'security', 'pages', 'activity', 'courseware', 'product', 'research', 'school', 'user_info']
    }),
    new ExtractTextPlugin('../css/[name].css'),
    new webpack.optimize.DedupePlugin(),
    new AssetsPlugin({filename: 'assets.json.py'}),
    new Vendor2BuildPlugin()
];

module.exports = {
    entry: entry,
    resolve: resolve,
    plugins: plugins,
    output: {
        path: path.resolve(__dirname, 'build/js'),
        // TODO: add dir
        filename: '[name].js'
    },
    module: {
        loaders: [
            {
                test: /\.sass$/,
                loader: ExtractTextPlugin.extract('style-loader', 'css-loader!sass-loader?indentedSyntax')
            },
            {
                test: /\.css$/,
                loader: ExtractTextPlugin.extract('style-loader', 'css-loader')
            },
            {test: /\.js$/, loader: 'babel'},
            {test: /\.png$/, loader: "url-loader"},
            {test: /\.jpg$/, loader: "file-loader"},
            {test: /\.woff$/, loader: "url-loader?prefix=font/&limit=5000&mimetype=application/font-woff"},
            {test: /\.ttf$/, loader: "file-loader"},
            {test: /\.eot$/, loader: "file-loader"},
            {test: /\.svg$/, loader: "file-loader"}
        ]
    }
};
