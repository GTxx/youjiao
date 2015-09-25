$(function () {
    $(".rslides").responsiveSlides({
        auto: true,
        pager: true
    });

    $(".rslides").find("img").each(function(){
        let ratio = $(".rslides").parent().width() / $(".rslides").parent().height();
        if ($(this).width()/$(this).height() < ratio)
            $(this).height($(".rslides").parent().height() + 'px');
        else
            $(this).width($(".rslides").parent().width() + 'px');

        if($(this).height() < $(".rslides").parent().height()) {
            let marginTop = ($(".rslides").parent().height() - $(this).height()) / 2;
            $(this).css('marginTop', marginTop);
        }
    });

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
});
