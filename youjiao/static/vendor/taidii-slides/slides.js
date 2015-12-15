(function ($) {
    $.fn.taidiiSlides = function (options) {
        var settings = {
            backgroundColor: 'black',
            frameColor: '#232323'
        };
        $.extend(settings, options);

        var init = function (self) {
            self.img_list_length = $(self).find('img').length;

            $(self).addClass('t-slides-frame')
                .append('<div class="t-frame-control"><span class="t-slide-index"><span class="t-current">1</span>/' + self.img_list_length + '</span></div>');

            $('.t-frame-control').css({'backgroundColor': settings.frameColor});

            $('<a />').appendTo($(self).children('.t-frame-control'))
                .attr('href', 'javascript:;')
                .addClass('t-inner-prev');

            $('<a />').appendTo($(self).children('.t-frame-control'))
                .attr('href', 'javascript:;')
                .addClass('t-inner-next');

            $('<a />').appendTo($(self).children('.t-frame-control'))
                .attr('href', 'javascript:;')
                .addClass('t-fullscreen');

            $(self).find('img').wrapAll('<div class="t-wrap"></div>')
                .addClass('t-display-none');
            $(self).find('img').eq(0).removeClass('t-display-none');
        };

        var initFullscreen = function () {
            var screenWidth = $(window).width();
            var screenHeight = $(window).height();
            $('<div />').appendTo('body')
                .addClass('t-fullscreen-wrap')
                .css('backgroundColor', settings.backgroundColor)
                .width(screenWidth)
                .height(screenHeight);
        };

        var cancelFullscreen = function (self) {
            $('.t-fullscreen-wrap').remove();
            $('.t-isfullscreen').remove();
            self.cloneSlides = null;
        };

        $(window).resize(function () {
            var screenWidth = $(window).width();
            var screenHeight = $(window).height();
            $('.t-fullscreen-wrap').width(screenWidth).height(screenHeight);
        });

        $(window).scroll(function () {
            var scrollTop = $(document).scrollTop();
            $('.t-isfullscreen').css({top: scrollTop + 'px'});
        });

        $(document).delegate('.t-isfullscreen', 'click', function (e) {
            e.stopPropagation();
        });

        $(this).each(function (i, self) {
            init(self);

            self.current = 0;
            self.cloneSlides = null;

            $(self).find(".t-inner-next").click(function () {
                if (!self.cloneSlides) {
                    self.current++;
                    self.current = self.current >= self.img_list_length ? self.img_list_length - 1 : self.current;
                    $(self).find('.t-current').text(self.current + 1);
                    var img_wrap = $(this).parentsUntil('.t-slides-frame')
                        .siblings('.t-wrap');
                    img_wrap.find('img').addClass('t-display-none');
                    img_wrap.find('img').eq(self.current)
                        .removeClass('t-display-none');
                }
            });

            $(self).find(".t-inner-prev").click(function () {
                if (!self.cloneSlides) {
                    self.current--;
                    self.current = self.current <= 0 ? 0 : self.current;
                    $(self).find('.t-current').text(self.current + 1);
                    var img_wrap = $(this).parentsUntil('.t-slides-frame').siblings('.t-wrap');
                    img_wrap.find('img').addClass('t-display-none');
                    img_wrap.find('img').eq(self.current).removeClass('t-display-none');
                }
            });

            $(document).delegate('.t-inner-next', 'click', function () {
                if (self.cloneSlides) {
                    self.fullCurrent++;
                    self.fullCurrent = self.fullCurrent >= self.img_list_length ? self.img_list_length - 1 : self.fullCurrent;
                    self.cloneSlides.find('.t-current').text(self.fullCurrent + 1);
                    var img_wrap = $(this).parentsUntil('.t-slides-frame')
                        .siblings('.t-wrap');
                    img_wrap.find('img').addClass('t-display-none');
                    img_wrap.find('img').eq(self.fullCurrent)
                        .removeClass('t-display-none');
                }
            });

            $(document).delegate('.t-inner-prev', 'click', function () {
                if (self.cloneSlides) {
                    self.fullCurrent--;
                    self.fullCurrent = self.fullCurrent <= 0 ? 0 : self.fullCurrent;
                    self.cloneSlides.find('.t-current').text(self.fullCurrent + 1);
                    var img_wrap = $(this).parentsUntil('.t-slides-frame')
                        .siblings('.t-wrap');
                    img_wrap.find('img').addClass('t-display-none');
                    img_wrap.find('img').eq(self.fullCurrent)
                        .removeClass('t-display-none');
                }
            });

            $(self).find(".t-fullscreen").click(function () {
                var frame = $(this).parentsUntil('.t-slides-frame').parent();
                if (!frame.hasClass('t-isfullscreen')) {
                    self.cloneSlides = frame.clone(true);
                    self.fullCurrent = self.current;
                    initFullscreen();
                    self.cloneSlides.insertAfter('.t-fullscreen-wrap')
                        .addClass('t-isfullscreen');
                    $('.t-isfullscreen').height($(window).height());
                    var leftWidth = ($(window).width() - $('.t-isfullscreen').width()) / 2;
                    var scrollTop = $(window).scrollTop();
                    $('.t-isfullscreen').css({left: leftWidth + 'px', top: scrollTop + 'px'});
                    $('.t-frame-control').css({left:  ($(window).width() - 800) / 2 + 'px'});
                } else {
                    cancelFullscreen(self);
                }
            });

            $(document).keyup(function (e) {
                if (e.keyCode == 27) {
                    cancelFullscreen(self);
                }
            });
        });
    }
})(jQuery);