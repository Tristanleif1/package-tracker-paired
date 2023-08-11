from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired
from map.map import map

city_origin = [key for key in map.keys()]
city_destination = [value for value in map.values()]

print(city_origin)
print(city_destination)



class ShippingForm(FlaskForm):
    name_sender = StringField('Sender Name', validators=[DataRequired()])
    name_recipient = StringField('Recipient Name', validators=[DataRequired()])
    origin = SelectField('Origin', key=city_origin, validators=[DataRequired()])
    destination = SelectField('Destination', value=city_destination, validators=[DataRequired()])
    express_shipping = BooleanField('Express Shipping', validators=[DataRequired()])

    