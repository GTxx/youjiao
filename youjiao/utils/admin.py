from wtforms.widgets import TextArea
from wtforms import TextAreaField
import json

class JSONEditorTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' json_field'
        else:
            kwargs.setdefault('class', 'json_field')
        return super(JSONEditorTextAreaWidget, self).__call__(field, **kwargs)


class JSONEditorTextAreaField(TextAreaField):
    widget = JSONEditorTextAreaWidget()


class JsonField(TextAreaField):
    widget = JSONEditorTextAreaWidget()

    def _value(self):
        if self.data:
            return json.dumps(self.data, ensure_ascii=False)
            # return json.dumps(self.data).encode('utf8')
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist[0]:
            try:
                self.data = json.loads(valuelist[0].replace('\r\n', ''))
            except Exception as e:
                raise ValueError(str(e))
        else:
            self.data = {}
