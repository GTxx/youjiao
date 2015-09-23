import 'normalize_css';
import 'main_css';
import 'slides_js';
import '../modules/add_slides_itemhover.js';

$(function(){
    $('.research-tab-s').click(function(){
        let index = $(this).index();
        $('.active').removeClass('active');
        $(this).addClass('active');
        $('.research-introduce-tab').addClass('display-none');
        $('.research-introduce-tab').eq(index).removeClass('display-none');
    });
});
