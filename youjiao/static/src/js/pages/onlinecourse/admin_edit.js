$(function () {
    JSONEditor.defaults.options.theme = 'bootstrap3';
    JSONEditor.defaults.language = "zh_CN";

    var DOM_json_textarea = $('.json_field');
    DOM_json_textarea.css({visibility: "hidden", display: "none"})
    $('<div id="json_editor"></div>').insertAfter(DOM_json_textarea);
    if (DOM_json_textarea.text()) {
        var init_value = JSON.parse(DOM_json_textarea.text())
    } else {
        var init_value = {full_video: "", short_video: ""};
    }
    var json_editor = new JSONEditor(document.getElementById('json_editor'), {
        schema: {
            type: "object",
            title: " ",
            options: {
              disable_collapse: true,
              disable_edit_json: true,
              disable_properties: true
            },
            properties: {
                full_video: {type: 'string'},
                short_video: {type: 'string'}
            },
            required_by_default: true,
            disable_collapse: true
        },
        startval: init_value,
    });
    // set changed json data on content
    json_editor.on('change', function () {
                console.log(this);
                $('#content').val(JSON.stringify(json_editor.getValue()))
            }
    )
});
