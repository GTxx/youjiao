$(function () {
    $(".rslides").responsiveSlides({
        auto: true,
        pager: true
    });

    function mouseOverAndOut(target, activeClass) {
        $(target).mouseenter(function () {
            $(this).addClass(activeClass);
            $(this).find(".v-image-hover-layer").animate({'opacity': 0.5});
            $(this).find(".nv-image-hover-layer").animate({'opacity': 0.9});
        }).mouseleave(function () {
            $(this).removeClass(activeClass);
            $(this).find(".v-image-hover-layer").animate({'opacity': 0});
            $(this).find(".nv-image-hover-layer").animate({'opacity': 0});
        });
    }

    mouseOverAndOut(".video-section-list li", "video-s-active");
    mouseOverAndOut(".n-v-section-list li", "n-v-active");
});