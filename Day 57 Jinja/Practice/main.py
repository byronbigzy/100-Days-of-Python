from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    number = random.randint(1, 10)
    year = datetime.now().year
    return render_template('index.html',num=number, year=year)

@app.route("/guess/<name>")
def guess_api(name):
    AGE_URL = f"https://api.agify.io?name={name}"
    GENDER_URL = f"https://api.genderize.io/?name={name}"
    age_response = requests.get(AGE_URL)
    age = age_response.json()["age"]
    gender_response = requests.get(GENDER_URL)
    gender = gender_response.json()["gender"]
    return render_template('guess.html',name=name, age=age, gender=gender)

@app.route("/blog")
def blog_render():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogposts = response.json()
    return render_template("blog.html", blogposts = blogposts)


if __name__ == "__main__":
    app.run(debug=True)