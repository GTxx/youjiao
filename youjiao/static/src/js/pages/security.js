import 'normalize';
import 'maincss';
import 'jquery-validation';

$(function () {
    $("#register-form").validate({
        errorElement: 'span',
        success: function(label){
            label.parent().empty();
        },
        errorPlacement: function (error, element) {
            let container = element.nextAll('span')[0];
            $(container).text('');
            error.appendTo(container);
        },
        rules: {
            email: {
                required: true,
                email: true
            },
            name: {
                required: true,
                rangelength: [4, 30]
            },
            password: {
                required: true,
                rangelength: [6, 30]
            },
            password_confirm: {
                required: true,
                equalTo: "#password"
            },
            captcha: {
                required: true
            }
        },
        messages: {
            email: "邮箱格式不正确！",
            name: "请输入4-30位用户名",
            password: "请输入6-30位密码",
            password_confirm: "两次输入不一致",
            captcha: "请输入验证码"
        },
        submitHandler: function (form) {
            form.submit();
        }
    });


    $("#login-form").validate({
        errorElement: 'div',
        success: function(label){
            label.parent().empty();
        },
        errorPlacement: function (error, element) {
            let container = element.nextAll('div')[0];
            $(container).text('');
            error.appendTo(container);
        },
        rules: {
            email_or_name: {
                required: true
            },
            password: {
                required: true,
                rangelength: [6, 30]
            },
            captcha: {
                required: true
            }
        },
        messages: {
            email_or_name: "请填写用户名或邮箱",
            password: "请输入6-30位密码",
            captcha: "请输入验证码"
        },
        submitHandler: function (form) {
            form.submit();
        }
    });

    $(".captcha").find('img').click(function(){
        let self = $(this);
        $.ajax({
            type: 'GET',
            url: '/refresh_captcha/',
            success: function(data) {
                let res = $.parseJSON(data);
                self.attr('src', res.url);
            }
        });
    });
});
