var path = require('path');
var dirname = path.resolve(__dirname, 'src/js/pages');

var entry = {
    home: path.resolve(dirname, 'home.js'),
    security: path.resolve(dirname, 'security.js'),
    activity: path.resolve(dirname, 'activity.js'),
    pages: path.resolve(dirname, 'pages.js'),
    research: path.resolve(dirname, 'research.js'),
    user_info: path.resolve(dirname, 'user_info.js'),

    //  book
    'book.detail': path.resolve(dirname, 'book/detail.js'),
    'book.home': path.resolve(dirname, 'book/home.js'),
    'book.sub_node': path.resolve(dirname, 'book/sub_node.js'),

    // courseware
    'courseware.detail': path.resolve(dirname, 'courseware/detail.js'),
    'courseware.home': path.resolve(dirname, 'courseware/home.js'),
    'courseware.sub_node': path.resolve(dirname, 'courseware/sub_node.js'),

    // school
    'school.detail': path.resolve(dirname, 'school/detail.js'),
    'school.home': path.resolve(dirname, 'school/home.js'),
    'school.sub_node': path.resolve(dirname, 'school/sub_node.js'),
};

module.exports = entry;