from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
from flask_pymongo import MongoClient
app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
myDatabase = client["flask-to-do"]
myTable = myDatabase["to-do"]


@app.route('/', methods=['POST', 'get'])
def Home():
    data = myTable.find()
    alltodos = []
    for i in data:
        alltodos.append(i)
    return render_template('index.html', allToDo=alltodos)


@app.route('/submit', methods=["post", "get"])
def submit():
    if request.method == 'POST':
        newTodo = {
            "title": request.form["title"],
            "desc": request.form["desc"]
        }
        res = myTable.insert_one(newTodo)
        return redirect(url_for("Home"))


@app.route('/about', methods=['POST', 'GET'])
def About():
    if request.method == "POST":
        return "hello akash"
    return render_template('about.html')


@app.route('/delete/<title>/<desc>', methods=['POST', 'GET'])
def delete(title, desc):
    myTable.delete_many({"title": title, "desc": desc})
    return redirect(url_for("Home"))


# without app.run we can't run this app :)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
