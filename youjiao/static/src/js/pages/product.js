import 'normalize_css';
import 'main_css';
import 'slides_js';
import '../modules/add_slides_itemhover';

$(function () {
    $(".p-s-imglist").click(function () {
        $(".s-img-active").removeClass("s-img-active");
        $(this).addClass("s-img-active");
        $('#samples-imgs-active').attr('src', $(this).children('img').attr('src'));
    });
    //
    //$("#simple-img-next").click(function () {
    //    let current = $(".s-img-active").index();
    //    $(".s-img-active").removeClass("s-img-active");
    //    let next = current < $(".p-s-imglist").length - 1 ? current + 1 : 0;
    //    $(".p-s-imglist").eq(next).addClass("s-img-active");
    //    $('#samples-imgs-active').attr('src', $('.p-s-imglist').eq(next).children('img').attr('src'));
    //});

    var firstImg = $('.p-s-imglist').eq(0).children('img').attr('src');
    $('#samples-imgs-active').attr('src', firstImg);
    $(".p-s-imglist").eq(0).addClass("s-img-active");
});
