$(function () {
    try {
        $(".rslides").responsiveSlides({
            auto: true,
            pager: true
        });
    } catch(e){}

    function mouseOverAndOut(target, activeClass) {
        $(target).mouseenter(function () {
            $(this).addClass(activeClass);
            $(this).find(".v-image-hover-layer").animate({'opacity': 0.3});
        }).mouseleave(function () {
            $(this).removeClass(activeClass);
            $(this).find(".v-image-hover-layer").animate({'opacity': 0});
        });
    }

    mouseOverAndOut(".video-section-list li", "video-s-active");
    mouseOverAndOut(".n-v-section-list li", "n-v-active");


    $(".p-s-imglist").click(function () {
        $(".s-img-active").removeClass("s-img-active");
        $(this).addClass("s-img-active");
    });

    $("#simple-img-next").click(function(){
        var current = $(".s-img-active").index();
        $(".s-img-active").removeClass("s-img-active");
        var next = current < $(".p-s-imglist").length-1 ? current + 1 : 0;
        $(".p-s-imglist").eq(next).addClass("s-img-active");
    });
});