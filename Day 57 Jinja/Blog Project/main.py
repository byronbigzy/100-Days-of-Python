from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

URL = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(URL)
blogposts = [Post(post['id'], post["title"], post['subtitle'], post['body']) for post in response.json()]

@app.route('/')
def home():
    return render_template("index.html", blogposts=blogposts)

@app.route('/about')
def about():
    return render_template("about.html", blogposts=blogposts)

@app.route('/contact')
def contact():
    return render_template("contact.html", blogposts=blogposts)

@app.route('/post/<int:id>')
def get_post(id):
    result = None
    for post in blogposts:
        if post.id == id:
            result = post
    return render_template('post.html', post=result)


if __name__ == "__main__":
    app.run(debug=True)
