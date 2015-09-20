var $ = require('jquery');

function favor(obj_id, obj_type, callback) {
  var csrf_token = $('meta[name=csrf-token]').attr('content');
  var data = {
    'obj_id': obj_id, obj_type: obj_type
  };
  $.ajax({
    type: "POST",
    beforeSend: function (request) {
      request.setRequestHeader("X-CSRFToken", csrf_token);
    },
    url: "/api/favor",
    dataType: 'json',
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(data),
    success: function (msg) {
      alert('ok');
      callback()
    }
  });
}

export default favor;

