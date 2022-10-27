from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4138d469444dd804d57db2c3cb47026b'

@app.route("/login")
    
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = 'Home')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form=form)
    

if __name__ == '__main__':
    app.run(debug = True)