from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '3f3040542f9e39e5cc0a30ac826f383d'

posts = [
    {
        'title': 'This is a title',
        'name': 'Test1',
        'paragraph': 'this is a test',
        'content': 'foo'
    },
    {
        'title': 'This is also a title',
        'name': 'Test2',
        'paragraph': 'this is also a test',
        'content': 'bar'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('homepage.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About Us")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', "success")
        return redirect(url_for('home'))
    return render_template('register.html', title="register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'logged in with {form.email.data}', "success")
        return redirect(url_for('home'))
    return render_template('login.html', title="login", form=form)

@app.route("/progression")
def test():
    return render_template('progression.html', title="progression")


if __name__ == '__main__':
    app.run(debug=True)

