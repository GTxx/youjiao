var path = require('path');
var dirname = path.resolve(__dirname, 'src/js/pages');

var entry = {
    home: path.resolve(dirname, 'home.js'),
    security: path.resolve(dirname, 'security.js'),
    activity: path.resolve(dirname, 'activity.js'),
    courseware: path.resolve(dirname, 'courseware.js'),
    pages: path.resolve(dirname, 'pages.js'),
    research: path.resolve(dirname, 'research.js'),
    school: path.resolve(dirname, 'school.js'),
    user_info: path.resolve(dirname, 'user_info.js'),
    video_detail: path.resolve(dirname, 'video_detail.js'),

    //  book 
    'book.detail': path.resolve(dirname, 'book/detail.js'),
    'book.home': path.resolve(dirname, 'book/home.js'),
    'book.sub_node': path.resolve(dirname, 'book/sub_node.js'),

    book_upload: path.resolve(dirname, 'book/upload.js')
};

module.exports = entry;