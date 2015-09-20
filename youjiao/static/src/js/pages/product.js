import 'normalize';
import 'maincss';
import 'slides';
import '../modules/add_slides_itemhover';
var $ = require('jquery');
import favor from '../modules/favor.js';

$('.product-collection').click(function () {
  var obj_id = location.href.split('/').slice(-1)[0];
  var obj_type = 'book';
  favor(obj_id, obj_type);
})