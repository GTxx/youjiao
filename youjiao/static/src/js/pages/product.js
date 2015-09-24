import 'normalize_css';
import 'main_css';
import 'slides_js';
import '../modules/add_slides_itemhover';
import favor from '../modules/favor.js';

$(function () {
    $('.product-collection').click(function () {
        var obj_id = location.href.split('/').slice(-1)[0];
        var obj_type = 'book';
        favor(obj_id, obj_type);
    });
});



