import 'normalize_css';
import 'main_css';
import 'body_css';
var $ = require('jquery');

$(function(){
    $('.userinfo-right-top').find('a').click(function(){
        $('.userinfo-right-top').find('.active').removeClass('active');
        $(this).addClass('active');
        let index = $(this).parent('li').index();
        $('.userinfo-content-tab').removeClass('display-block').addClass('display-none');
        $('.userinfo-content-tab').eq(index).removeClass('display-none').addClass('display-block');
    });
});
