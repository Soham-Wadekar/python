from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e5522826fcb36795a8ef27d47ab51c83'

posts = [
    {
        'author': 'Soham Wadekar',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Harum vel minus id quis fugiat recusandae, ad modi nobis ipsum! Esse?',
        'date_posted': 'October 20, 2024'
    },
    {
        'author': 'Soumil Wadekar',
        'title': 'Blog Post 2',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet, at!',
        'date_posted': 'May 1, 2008'
    },
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)