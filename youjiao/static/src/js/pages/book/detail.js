import 'normalize_css';
import 'main_css';
import favor from '../../modules/favor.js';
import '../../modules/not_login_pop.js';

$(function () {
    $('.product-collection').click(function () {
        var obj_id = location.href.split('/').slice(-1)[0];
        var obj_type = 'book';
        favor(obj_id, obj_type);
    });

    $(".p-s-imglist").click(function () {
        $(".s-img-active").removeClass("s-img-active");
        $(this).addClass("s-img-active");
        $('#samples-imgs-active').attr('src', $(this).children('img').attr('src'));
    });

    let firstImg = $('.p-s-imglist').eq(0).children('img').attr('src');
    $('#samples-imgs-active').attr('src', firstImg);
    $(".p-s-imglist").eq(0).addClass("s-img-active");

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
        console.log('123123123')
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
});
