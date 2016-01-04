import 'normalize_css';
import 'main_css';
import 'slides_js';
import '../modules/add_slides_itemhover';

$(function(){
    $(".submit-message").click(function(e){
        e.preventDefault();
        let content = $('#message-content').val();
        $.ajax({
            type: "POST",
            url: "/api/leavemessage/",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({ 'content': content }),
            success: function (jsonResult) {
                alert("留言已发送");
            }
        });
    });
});
