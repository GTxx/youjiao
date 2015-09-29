(function ($) {
    $.fn.not_login_pop = function () {

        let cancelB = function (e) {
            if (e && e.stopPropagation)
                e.stopPropagation();
            else
                window.event.cancelBubble = true;
        };

        let add_mask_layer = function () {
            $('<div />').appendTo('body')
                .addClass('mask-layer');
        };

        $(this).click(function (e) {
            cancelB(e);

            add_mask_layer();

            if ($('.not-login-message').length)
                return false;

            let scrollTop = $(window).scrollTop();
            $("<div />").appendTo('body')
                .addClass('not-login-message')
                .css('top', -(scrollTop + $(this).height()) + 'px')
                .animate({'top': scrollTop + 100 + 'px'}, 600);

            $('<h4 />').appendTo('.not-login-message')
                .text('您还未登陆，是否现在登陆');

            $('<a />').appendTo('.not-login-message')
                .addClass('pop-to-login')
                .attr({'href': '/login', 'target': '_blank'})
                .text('是');

            $('<a />').appendTo('.not-login-message')
                .addClass('pop-to-cancel')
                .attr('href', 'javascript:;')
                .text('否');
        });

        let cancelPop = function () {
            $('.not-login-message').animate({'top': -$('.not-login-message').height() + 'px'}, 300, function () {
                $(".not-login-message").remove();
                $(".mask-layer").remove();
            });
        };

        $(document).click(cancelPop);
        $('body').delegate('.pop-to-cancel', 'click', cancelPop);

        $('body').delegate('.not-login-message', 'click', function (e) {
            cancelB(e);
        });

        $(window).scroll(function () {
            let scrollTop = $(window).scrollTop();
            $(".not-login-message").animate({'top': scrollTop + 100 + 'px'}, 100);
        });
    };
})(jQuery);
