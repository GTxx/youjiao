import 'normalize_css';
import 'main_css';
import '../../modules/not_login_pop';
import 'lightbox_css';
import 'lightbox_js';
import 'taidii_slides_css';
import 'taidii_slides_js';

$(function () {
    $('.document-img').taidiiSlides();

    $('#not-login-pop').not_login_pop();

    $('.book-switch').click(function () {
        let index = $(this).index();
        $('.active').removeClass('active');
        $(this).addClass('active');
        $('.detail-comment-content').addClass('display-none');
        $('.detail-comment-content').eq(index).removeClass('display-none');
    });

    $('#book-publish-comment').click(function () {
        let content = $('#comment-textarea').val();
        // TODO: put csrf_token get in a module
        let csrf_token = $('meta[name=csrf-token]').attr('content');
        let book_id = window.location.pathname.split('/').reverse()[0];
        if (content.length == 0) {
            alert('请输入评论再提交');
        } else if (content.length > 140) {
            alert('评论超过了140个字')
        } else {
            $.ajax({
                type: 'POST',
                url: `/api/book/${book_id}/comment`,
                beforeSend: (request) => {
                    request.setRequestHeader("X-CSRFToken", csrf_token);
                },
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify({content: content}),
                success: (data) => {
                    let username = $('.header-login-name').eq(0).text();
                    let content = data.content;
                    let commentString = '<li>' +
                        '<div>' +
                        '<img src="" alt="">' +
                        '<h6>' + username + '</h6>' +
                        '</div>' +
                        '<span>' + content + '</span>' +
                        '</li>';
                    $('#book-content-list').append(commentString);
                    $('#comment-textarea').val('');
                },
                fail: (data) => {
                    alert('评论失败，请稍候再试');
                }
            })
        }
    });

    var cancelBubble = function (e) {
        if (e && e.stopPropagation)
            e.stopPropagation();
        else
            window.event.cancelBubble = true;
    };

    $("#click-to-download").click(function (e) {
        cancelBubble(e);
        let scrollTop = $(window).scrollTop();
        $("#download-box").removeClass('display-none');
        $("#download-box").css('top', -(scrollTop + $(this).height()) + 'px');
        $("#download-box").animate({'top': scrollTop + 100 + 'px'}, 300);
    });

    $(document).click(function () {
        $("#download-box").animate({'top': - $("#download-box").height() + 'px'}, 300, function(){
            $("#download-box").addClass('display-none');
        });
    });

    $("#download-box").click(function (e) {
        cancelBubble(e);
    });
});
