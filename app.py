# The code by Yair-T | https://youtube.com/@Yair-T | https://github.com/Yair-T
from flask import Flask,  render_template, url_for, redirect, session, request
from wtforms import SubmitField, StringField
# install passwordtools with: `pip install passwordtools-yt`.
# To documentation., visit on my gitub in: https://github.com/Yair-T/passwordtools.
from passwordtools import PasswordTool 
from flask_wtf import FlaskForm


app = Flask(__name__)
app.config['SECRET_KEY'] = r"ENTER_SECRET_KEY_HERE"


class PasswordForm(FlaskForm):
    password = StringField('Password', render_kw={'type': 'text', 'class': 'password-input', 'placeholder': 'Password', 'readonly': True})
    btn = SubmitField('Generate!', render_kw={'class': 'btn'})


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasswordForm()
    if form.btn.data:
        session['password'] = PasswordTool.generate(length=12)
        return redirect(url_for('index'))
    form.password.data = session.get('password')
    session.clear()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(port=5000, debug=False)
