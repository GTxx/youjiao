
$(function() {
    personal('.right_second:eq(0) h4:eq(0)','.right_second:eq(0) h4:eq(0)','.right_second:eq(0) h4:eq(1)','.right_second:eq(0) span','#right_body_image','#right_body','#right_body_password');
    personal('.right_second:eq(0) h4:eq(1)','.right_second:eq(0) h4:eq(1)','.right_second:eq(0) h4:eq(0)','.right_second:eq(0) span','#right_body_password','#right_body','#right_body_image');
    personal('.right_second:eq(0) span','.right_second:eq(0) span','.right_second:eq(0) h4:eq(1)','.right_second:eq(0) h4:eq(0)','#right_body','#right_body_password','#right_body_image');
    personal('.right_second:eq(3) span','.right_second:eq(3) span','.right_second:eq(3) h4:eq(1)','.right_second:eq(3) h4:eq(0)','.MyCollection2','.study_record:eq(1)');
    personal('.right_second:eq(3) h4:eq(1)','.right_second:eq(3) h4:eq(1)','.right_second:eq(3) span','.right_second:eq(3) h4:eq(0)','.study_record:eq(1)','.MyCollection2');
    personal('.right_second:eq(3) h4:eq(0)','.right_second:eq(3) h4:eq(0)','.right_second:eq(3) h4:eq(1)','.right_second:eq(3) span','.MyCollection2','.study_record:eq(1)');
    dj('#left ul li span:eq(1)','.right:eq(1)','.right:eq(2)','.right:eq(0)','.right:eq(3)','.right:eq(4)','#left>ul>li'); //左边5个点击事件
    dj('#left ul li span:eq(0)','.right:eq(0)','.right:eq(2)','.right:eq(1)','.right:eq(3)','.right:eq(4)','#left>ul>li');
    dj('#left ul li span:eq(2)','.right:eq(2)','.right:eq(0)','.right:eq(1)','.right:eq(3)','.right:eq(4)','#left>ul>li');
    dj('#left ul li span:eq(3)','.right:eq(3)','.right:eq(0)','.right:eq(1)','.right:eq(2)','.right:eq(4)','#left>ul>li');
    dj('#left ul li span:eq(4)','.right:eq(4)','.right:eq(0)','.right:eq(1)','.right:eq(2)','.right:eq(3)','#left>ul>li');
    dj('.right:eq(2) .right_second span','.right:eq(2) .research .keyword:eq(0)','.right:eq(2) .research .keyword:eq(1)');
    dj('.right:eq(2) .right_second h4','.right:eq(2) .research .keyword:eq(1)','.right:eq(2) .research .keyword:eq(0)');
    dj('.right:eq(3) .right_second>span','.right:eq(3) #MyCollection2','.right:eq(3) .study_record');//我的收藏点击事件
    dj('.right:eq(3) .right_second>h4:eq(0)','.right:eq(3) #MyCollection2','.right:eq(3) .study_record');
    dj('.right:eq(3) .right_second>h4:eq(1)','.right:eq(3) .study_record','.right:eq(3) #MyCollection2');
    $('.button5').click(function () {
        $(this).attr('class', 'button4'); //改变class名字
    });
});
function personal(classname,childname1,childname2,childname3,childname4,childname5,childname6){
        $(classname).click(function(){
        $(childname3).css("borderBottom", 'none');
        $(childname2).css("borderBottom", 'none');
        $(childname1).css("borderBottom", '3px solid deeppink');
       $(childname5).css('display', 'none');
        $(childname4).css('display', 'block');
        $(childname6).css('display', 'none');
    });
}
function dj(classname,childname1,childname2,childname3,childname4,childname5,childname6){
         $(classname).click(function(){
        $(childname6).css('background', 'none');
        $(this).closest('li').css('background', 'white');
        $(childname1).css('display','block');
        $(childname2).css('display','none');
        $(childname3).css('display','none');
        $(childname4).css('display','none');
        $(childname5).css('display','none');
    });

}

