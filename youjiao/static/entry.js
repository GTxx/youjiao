var path = require('path');
var dirname = path.resolve(__dirname, 'src/js/pages');

var entry = {
    home: path.resolve(dirname, 'home.js'),
    account: path.resolve(dirname, 'account.js')
};

module.exports = entry;