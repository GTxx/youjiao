import 'normalize_css';
import 'main_css';
import 'body_css';
var $ = require('jquery');

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
//function validate_length(min, max) {
//  return (str) => {
//    if (5 < str.length && str.length < 15) {
//      return [true, '']
//    } else {
//      return [false, `长度在${min}到${max}之间`];
//    }
//
//  }
//}
//
//class ResetPassword extends React.Component {
//
//  constructor(props) {
//    super(props);
//    this.state = {
//      old_password: {valid: false, validate_fn: validate_length(5, 15), errors: '', value: ''},
//      password: {valid: false, validate_fn: validate_length(5, 15), errors: '', value: ''},
//      password_confirm: {valid: false, validate_fn: validate_length(5, 15), errors: '', value: ''},
//      error: ''
//    }
//    this.handleSubmit = this.handleSubmit.bind(this)
//  }
//
//  validate() {
//    // validate all fields
//    if (this.state.old_password.valid && this.state.password.valid && this.state.password_confirm.valid) {
//      if (this.state.password.value != this.state.password_confirm.value) {
//        this.setState({can_submit: false, 'error': '两次输入密码不一致'})
//        return false
//      }
//      else if (this.state.password.value == this.state.old_password.value) {
//        this.setState({'can_submit': false, error: '修改后密码跟原密码一样'})
//        return false
//      }
//      else {
//        this.setState({'can_submit': true, error: ''})
//        return true
//      }
//    } else {
//      console.log(1231)
//      this.setState({can_submit: false, error: ''})
//      return false
//    }
//  }
//
//
//  handleSubmit(e) {
//    e.preventDefault();
//    let old_password = this.state.old_password.value
//    let password = this.state.password.value
//    let password_confirm = this.state.password_confirm.value
//
//    $.ajax({
//      url: '/api/user/reset_password',
//      type: 'POST',
//      data: JSON.stringify({old_password: old_password, password: password, password_confirm: password_confirm}),
//      dataType: 'json',
//      contentType: 'application/json'
//    })
//      .done(function (msg) {
//        // TODO: add a success info
//        alert('密码修改成功，下次登陆请使用新的密码')
//      }.bind(this))
//      .fail(function (jqXHR) {
//        this.setState({error: jqXHR.responseJSON._schema[0]})
//      }.bind(this))
//  }
//
//  changed(field) {
//    return (evt) => {
//      // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer
//      // computed property names(ES6)
//      let obj = this.state[field];
//      obj.value = evt.target.value;
//      [obj.valid, obj.errors] = obj.validate_fn(obj.value)
//      this.setState({[field]: obj})
//      this.validate()
//    }
//  }
//
//  render() {
//    return (
//      <div>
//        <ul>
//          <li>
//            <span>当前密码:</span><input type="password" value={this.state.old_password.value}
//                                     onChange={this.changed('old_password')}/>
//            <span>{this.state.old_password.errors}</span>
//          </li>
//          <li><span>新密码:</span><input type="password" value={this.state.password.value}
//                                      onChange={this.changed('password') }/>
//            <span>{this.state.password.errors}</span>
//          </li>
//          <li><span>确认密码:</span><input type="password" value={this.state.password_confirm.value}
//                                       onChange={this.changed('password_confirm')}/>
//            <span>{this.state.password_confirm.errors}</span>
//          </li>
//        </ul>
//        <span>{this.state.error}</span>
//        <button disabled={this.state.error.length != 0} onClick={this.handleSubmit}>修改密码</button>
//      </div>
//    )
//  }
//}
//
//class UserProfile extends React.Component {
//  constructor(props) {
//    super(props);
//    this.state = {
//      profile: {},
//      name: {valid: false, validate_fn: validate_length(5, 15), errors: '', value: ''},
//      password: {valid: false, validate_fn: validate_length(5, 15), errors: '', value: ''},
//      password_confirm: {valid: false, validate_fn: validate_length(5, 15), errors: '', value: ''},
//      error: ''
//    }
//  }
//  componentDidMount(){
//    $.ajax({
//      url: '/api/user_info'
//    })
//      .done((res) => {
//        console.log(res)
//        console.log(this)
//        this.setState({profile: res.profile})
//      })
//  }
//  render() {
//    return (
//      <div>
//        <ul>
//          <li><span>生日:</span><input type="text" value={this.state.profile.birthday}/></li>
//          <li><span>职业:</span><input type="text" value={this.state.profile.career}/></li>
//          <li><span>工作单位:</span><input type="text" value={this.state.profile.work_place_name}/></li>
//          <li><span>性别:</span><input type="text" value={this.state.profile.gender}/></li>
//        </ul>
//        <button disabled={this.state.error.length != 0} onClick={this.handleSubmit}>修改密码</button>
//      </div>
//    )
//  }
//}
//React.render(<ResetPassword />, document.getElementById('right_body_password'));
//React.render(<UserProfile />, document.getElementById('right_body'))
