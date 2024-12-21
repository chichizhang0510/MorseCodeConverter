from flask import Flask, render_template
import secrets
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

from morse_machine import MorseMachine


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = 'your_secret_key'

class InteractiveForm(FlaskForm):
    Input = TextAreaField('Content you want to convert', validators=[DataRequired()])
    Type = SelectField('Operation you want to do', choices=[('en', 'Encryption'), ('de', 'Decryption')])
    submit = SubmitField('Convert')


@app.route("/", methods=['POST', 'GET'])
def home():
    mc = MorseMachine()
    result = "There you can see the output!"
    form = InteractiveForm()
    if form.validate_on_submit():
        mc.get_input(form.Input.data)
        if form.Type.data == "en":
            mc.encryption()
        else:
            mc.decryption()
        result = mc.output
        return render_template("index.html", form=form, result=result)
    return render_template("index.html", form=form, result=result)


if __name__ == "__main__":
    app.run(debug=True)