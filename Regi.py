import sqlite3


conn = sqlite3.connect("one.db")
cursor = conn.cursor()


cursor.execute('''CREATE TABLE STUDENT 
              (Mail TEXT PRIMARY KEY NOT NULL, 
              Power INT NOT NULL);''')
conn.commit()


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')