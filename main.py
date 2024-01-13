from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_data = requests.get("https://api.npoint.io/1c8b7c49b6e0fe402ce8").json()
print(blog_data)
@app.route("/")
def hello_world():
    return render_template("index.html", posts = blog_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:id_num>")
def post(id_num):

    return render_template("post.html", ID = id_num, posts = blog_data)


if __name__ == '__main__':
    app.run(debug=True)
