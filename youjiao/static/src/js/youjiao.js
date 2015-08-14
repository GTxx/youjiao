$(function () {
    $(".rslides").responsiveSlides({
        auto: true,
        pager: true
    });

    function mouseOverAndOut(target, activeClass) {
        $(target).mouseover(function () {
            $(this).addClass(activeClass);
        }).mouseout(function () {
            $(this).removeClass(activeClass);
        });
    }

    mouseOverAndOut(".textbook-advice-list li", "textbook-active");
    mouseOverAndOut(".book-advice-list li", "book-active");
    mouseOverAndOut(".good-lectures-list li", "lectures-active");


});