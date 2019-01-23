from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = 'ec6d70c7e3e2243b841908052fefbc8d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

posts = [
    {
        'author': 'Rahul Sharma',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 21st, 2018'
    },

    {
        'author': 'Vatsal Gherwada',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 29st, 2018'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))

    return render_template('register.html', title="Register", form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)