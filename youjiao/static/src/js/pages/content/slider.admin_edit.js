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
            type: "array",
            format: "table",
            title: "  ",
            items: {
                type: "object",
                properties: {
                    image: {type: "string"},
                    link: {type: "string"}
                }
            }
        },
        required_by_default: true,
        startval: init_value,
        disable_collapse: true
    });
    // set changed json data on content
    json_editor.on('change', function () {
                console.log(this);
                let value = JSON.stringify(json_editor.getValue())
                console.log(value);
                $('#image_list').val(JSON.stringify(json_editor.getValue()))
            }
    )
});
