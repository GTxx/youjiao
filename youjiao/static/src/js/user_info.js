function validate_length(min, max){
    return (str) =>{
      if ( 5 < str.length && str.length < 15){
        return [true, '']
      }else{
        return [false, `长度在${min}到${max}之间`];
      }

    }
}

class ResetPassword extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      old_password: {valid: false, validate_fn: validate_length(5, 15), errors: '', value: ''},
      password: {valid: false, validate_fn: validate_length(5, 15), errors: '', value: ''},
      password_confirm: {valid: false, validate_fn: validate_length(5, 15), errors: '', value: ''},
      error: ''
    }
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  validate () {
    // validate all fields
    if (this.state.old_password.valid && this.state.password.valid && this.state.password_confirm.valid){
      if (this.state.password.value != this.state.password_confirm.value) {
        this.setState({can_submit: false, 'error': '两次输入密码不一致'})
        return false
      }
      else if (this.state.password.value == this.state.old_password.value){
        this.setState({'can_submit':  false, error: '修改后密码跟原密码一样'})
        return false
      }
      else{
        this.setState({'can_submit':  true, error: ''})
        return true
      }
    }else{
      console.log(1231)
      this.setState({can_submit: false, error: ''})
      return false
    }
  }


  handleSubmit(e) {
    e.preventDefault();
    let old_password = this.state.old_password.value
    let password = this.state.password.value
    let password_confirm = this.state.password_confirm.value

    $.ajax({
      url: '/api/user/reset_password',
      type: 'POST',
      data: JSON.stringify({old_password: old_password, password: password, password_confirm: password_confirm}),
      dataType: 'json',
      contentType: 'application/json'
      //success: (data)=>{
      //  console.log(data)
      //},
      //failure: (errMsg)=>{
      //  alert(errMsg)
      //}
    })
    .done(function(msg){
        // TODO: add a success info
        alert('密码修改成功，下次登陆请使用新的密码')
      }.bind(this))
    .fail(function(jqXHR){
        this.setState({error: jqXHR.responseJSON._schema[0]})
      }.bind(this))
  }

  changed(field){
    return (evt) => {
      // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer
      // computed property names(ES6)
      let obj = this.state[field];
      obj.value = evt.target.value;
      [obj.valid, obj.errors] = obj.validate_fn(obj.value)
      this.setState({[field]: obj})
      this.validate()
    }
  }

  render() {
    return (
      <div>
        <ul>
          <li>
            <span>当前密码:</span><input type="password"  value={this.state.old_password.value} onChange={this.changed('old_password')} />
            <span>{this.state.old_password.errors}</span>
          </li>
          <li><span>新密码:</span><input type="password" value={this.state.password.value} onChange={this.changed('password') }/>
            <span>{this.state.password.errors}</span>
          </li>
          <li><span>确认密码:</span><input type="password" value={this.state.password_confirm.value} onChange={this.changed('password_confirm')} />
            <span>{this.state.password_confirm.errors}</span>
          </li>
        </ul>
        <span>{this.state.error}</span>
        <button disabled={this.state.error.length != 0} onClick={this.handleSubmit}>修改密码</button>
      </div>
    )
  }
}

React.render(<ResetPassword />, document.getElementById('right_body_password'));