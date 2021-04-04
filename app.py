from flask import Flask, render_template, url_for

app = Flask(__name__)

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

@app.route("/register")
def register():
    return render_template('register.html', title="register")


@app.route("/login")
def login():
    return render_template('login.html', title="login")


@app.route("/progression")
def test():
    return render_template('progression.html', title="progression")


if __name__ == '__main__':
    app.run(debug=True)

