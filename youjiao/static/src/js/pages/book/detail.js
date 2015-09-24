import 'normalize_css';
import 'main_css';
import favor from '../../modules/favor.js';

$(function () {
    $(".p-s-imglist").click(function () {
        $(".s-img-active").removeClass("s-img-active");
        $(this).addClass("s-img-active");
        $('#samples-imgs-active').attr('src', $(this).children('img').attr('src'));
    });

    var firstImg = $('.p-s-imglist').eq(0).children('img').attr('src');
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
                    console.log(data)
                    alert(data)
                },
                fail: (data) => {
                    console.log(data)
                    alert(data)
                }
            })
        }
    });
});
