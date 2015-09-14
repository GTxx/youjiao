var path = require('path');
var dirname = path.resolve(__dirname, 'src/js/pages');

var entry = {
    home: path.resolve(dirname, 'home.js'),
    security: path.resolve(dirname, 'security.js'),
    activity: path.resolve(dirname, 'activity.js'),
    courseware: path.resolve(dirname, 'courseware.js'),
    pages: path.resolve(dirname, 'pages.js'),
    product: path.resolve(dirname, 'product.js'),
    research: path.resolve(dirname, 'research.js'),
    school: path.resolve(dirname, 'school.js'),
    userinfo: path.resolve(dirname, 'userinfo.js')
};

module.exports = entry;