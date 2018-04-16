from flask_wtf import FlaskForm
from wtforms import StringField,FileField
from flask_wtf.file import FileRequired,FileAllowed
from wtforms.validators import InputRequired
from wtforms.widgets import TextArea
    
class UploadForm(FlaskForm):
    photo = FileField(validators   = [FileRequired(),FileAllowed(['jpg','png','jpeg'],'Only Images Allowed')])
    description = StringField(validators = [InputRequired()],widget = TextArea())
    
    