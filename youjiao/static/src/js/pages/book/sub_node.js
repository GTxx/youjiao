import 'normalize_css';
import 'main_css';
import 'slides_js';
import '../../modules/add_slides_itemhover';

$(function () {
    $('.classes-select').change(function () {
        let w_location = window.location;
        w_location.href = w_location.origin + w_location.pathname + $('.classes-select option:selected').val();
    });
});