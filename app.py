from flask import Flask, render_template, flash, redirect, url_for
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

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for ('home'))
    return render_template('register.html', title = 'Register', form=form)
    

if __name__ == '__main__':
    app.run(debug = True)