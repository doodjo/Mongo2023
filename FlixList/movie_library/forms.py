from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField, URLField, PasswordField


class MovieForm(FlaskForm):
    title = StringField("Naziv")
    director = StringField("Režiser")

    year = IntegerField("Godina")

    submit = SubmitField("Dodaj")

# novo za Dusana
# jedna vrednost po liniji, za update odredjenog polja 

class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        # provera da li polja sadrze jedan element i da je taj element validan npr nije ti empty string
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []  


# ok sakpirao sam 

class ExtendedMovieForm(MovieForm):
    cast = StringListField("Glumci")
    series = StringListField("Series")
    tags = StringListField("Tagovi")
    description = TextAreaField("Opis")
    video_link = URLField("Video Link")

    submit = SubmitField("Update")


class RegisterForm(FlaskForm):
    email = StringField("Email")
    password = PasswordField("Password")

    submit = SubmitField("Registracija")


class LoginForm(FlaskForm):
    email = StringField("Email")
    password = PasswordField("Password")
    
    submit = SubmitField("Prijava")
    
