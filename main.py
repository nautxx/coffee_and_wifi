from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap   # pip install Flask-Bootstrap
from flask_wtf import FlaskForm # pip install -U Flask-WTF
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from dotenv import load_dotenv  # pip install python-dotenv
import os
from forms import CafeForm, BrewForm


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY")
Bootstrap(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # writes object data into .csv file
        with open("cafe-data.csv", mode="a") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/log', methods=["GET", "POST"])
def log_brew():
    form = BrewForm()
    if form.validate_on_submit():
        # writes object data into .csv file
        with open("brew_data.csv", mode="a") as csv_file:
            csv_file.write(
                f"\n{form.coffee.data},"
                f"{form.region.data},"
                f"{form.roast_level.data},"
                f"{form.roast_date.data},"
                f"{form.brew_method.data},"
                f"{form.grind_settings.data},"
                f"{form.water_temp.data},"
                f"{form.dose.data},"
                f"{form.water_in_or_yield.data},"
                f"{form.brew_time.data},"
                f"{form.notes.data}"
            )
        return redirect(url_for('cafes'))
    return render_template('log.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        # render csv_data into list_of_rows array
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6182, debug=True)
    # app.run(debug=True)