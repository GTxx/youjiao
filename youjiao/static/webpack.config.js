var path = require('path');
var webpack = require('webpack');
var entry = require('./entry');
var resolve = require('./resolve.js');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var AssetsPlugin = require('assets-webpack-plugin');

var plugins = [
    new webpack.ProvidePlugin({
        $: "jquery",
        jQuery: "jquery",
        "window.jQuery": "jquery",
        "root.jQuery": "jquery"
    }),
    new webpack.optimize.CommonsChunkPlugin('commons', 'commons.js'),
    new ExtractTextPlugin('../css/[name].css'),
    new webpack.optimize.DedupePlugin(),
    new AssetsPlugin({filename: 'assets.json.py'})
];

module.exports = {
    entry: entry,
    resolve: resolve,
    plugins: plugins,
    output: {
        path: path.resolve(__dirname, 'build/js'),
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
            {test: /\.jpg$/, loader: "file-loader"}
        ]
    }
};
