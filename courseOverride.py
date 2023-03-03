from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class ORForm(FlaskForm):
    firstname = StringField('What is your first name?', validators=[DataRequired()])
    lastname = StringField('What is your last name?', validators=[DataRequired()])
    vnumber = StringField('What is your V#?', validators=[DataRequired()])
    course = StringField('What is the course ID?', validators=[DataRequired()])
    courseNumber = StringField('What is the course number?', validators=[DataRequired()])
    crnNumber = StringField('What is the CRN number for the course section?', validators=[DataRequired()])
    reason = StringField('What is your reasoning for the override?', validators=[DataRequired()])

    submit = SubmitField('Submit')
    required_css_class = 'required'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    firstname = None
    lastname = None
    vnumber = None
    course = None
    courseNumber = None
    crnNumber = None

    form = ORForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        form.firstname.data = ''
        lastname = form.lastname.data
        form.lastname.data = ''
        vnumber = form.vnumber.data
        form.vnumber.data = ''
        course = form.course.data
        form.course.data = ''
        courseNumber = form.courseNumber.data
        form.courseNumber.data = ''
        crnNumber = form.crnNumber.data
        form.crnNumber.data = ''
        reason = form.reason.data
        form.reason.data = ''

        return render_template('submitted.html'), 200
    return render_template('index.html', form=form, firstname=firstname, lastname=lastname, vnumber=vnumber,
                           course=course, courseNumber=courseNumber, crnNumber=crnNumber)
