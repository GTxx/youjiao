from flask import Blueprint, render_template

from youjiao.activity.models import Activity

activity = Blueprint("activity_content", __name__, template_folder='templates')


@activity.route('/activity/<id>')
def activity_view(id):
    obj = Activity.query.get(id)
    return render_template('activity.html', activity=obj)


@activity.route('/activity')
def activity_list():
    query = Activity.query.all()
    return render_template('activity_list.html', activity_list=query)
