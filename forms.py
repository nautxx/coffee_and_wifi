from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm():

    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Rating", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')


class BrewForm():

    coffee = StringField("Coffee", validators=[DataRequired()])
    region = StringField("Region", validators=[DataRequired()])
    roast_level = SelectField("Coffee Rating", choices=["Light", "Medium", "Dark", "Darker than Dark"], validators=[DataRequired()])
    roast_date = StringField("Region", validators=[DataRequired()])
    brew_method = SelectField("Brew Method", choices=["Syphon", "Chemex", "Pour Over", "Cold", "Aeropress", "French Press", "Espresso", "Drip Brew"], validators=[DataRequired()])
    grind_settings = StringField("Grind Settings", validators=[DataRequired()])
    water_temp = StringField("Water Temp", validators=[DataRequired()])
    dose = StringField("Dose", validators=[DataRequired()])
    water_in_or_yield = dose = StringField("Water In or Yield", validators=[DataRequired()])
    brew_time = StringField("Brew Time", validators=[DataRequired()])
    notes = StringField("Notes", validators=[DataRequired()])
    submit = SubmitField('Log it')