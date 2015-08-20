from flask import Blueprint, render_template
from flask_security.decorators import anonymous_user_required


user_bp = Blueprint("user_view", __name__)


@anonymous_user_required
def register():
    """View function which handles a registration request."""

    if _security.confirmable or request.json:
        form_class = _security.confirm_register_form
    else:
        form_class = _security.register_form

    if request.json:
        form_data = MultiDict(request.json)
    else:
        form_data = request.form

    form = form_class(form_data)

    if form.validate_on_submit():
        user = register_user(**form.to_dict())
        form.user = user

        if not _security.confirmable or _security.login_without_confirmation:
            after_this_request(_commit)
            login_user(user)

        if not request.json:
            if 'next' in form:
                redirect_url = get_post_register_redirect(form.next.data)
            else:
                redirect_url = get_post_register_redirect()

            return redirect(redirect_url)
        return _render_json(form, include_auth_token=True)

    if request.json:
        return _render_json(form)

    return _security.render_template(config_value('REGISTER_USER_TEMPLATE'),
                                     register_user_form=form,
                                     **_ctx('register'))

@anonymous_user_required
def register1():
    # 
