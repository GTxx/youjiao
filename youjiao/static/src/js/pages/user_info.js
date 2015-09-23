import 'normalize_css';
import 'main_css';
var $ = require('jquery');

$(function(){
    $('.userinfo-right-top').find('a').click(function(){
        $('.userinfo-right-top').find('.active').removeClass('active');
        $(this).addClass('active');
        let index = $(this).parent('li').index();
        $('.userinfo-content-tab').addClass('display-none');
        $('.userinfo-content-tab').eq(index).removeClass('display-none');
    });
});
