$(function () {
    var cancelB = function (e) {
        if (e && e.stopPropagation)
            e.stopPropagation();
        else
            window.event.cancelBubble = true;
    };

    $('.not-login-pop').click(function (e) {
        cancelB(e);

        if ($('.not-login-message').length)
            return false;

        let scrollTop = $(window).scrollTop();
        $("<div />").appendTo('body')
            .addClass('not-login-message')
            .css('top', -(scrollTop + $(this).height()) + 'px')
            .animate({'top': scrollTop + 100 + 'px'}, 600);

        $('<h4 />').appendTo('.not-login-message')
            .text('登陆61幼教网');

        $('<a />').appendTo('.not-login-message')
            .addClass('pop-to-login')
            .attr({'href': '/login', 'target': '_blank'})
            .text('是');

        $('<a />').appendTo('.not-login-message')
            .addClass('pop-to-cancel')
            .attr('href', 'javascript:;')
            .text('否');
    });

    function cancelPop() {
        $('.not-login-message').animate({'top': -$('.not-login-message').height() + 'px'}, 300, function () {
            $(".not-login-message").remove();
        });
    }

    $(document).click(cancelPop);
    $('body').delegate('.pop-to-cancel', 'click', cancelPop);

    $('body').delegate('.not-login-message', 'click', function (e) {
        cancelB(e);
    });
});
