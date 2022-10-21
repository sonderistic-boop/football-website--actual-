from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template('login.html', title = 'Login')

@app.route("/home")
def home():
    return render_template('home.html', title = 'Home')
    

if __name__ == '__main__':
    app.run(debug = True)