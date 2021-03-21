from flask import Flask, request, render_template
from datetime import datetime
app = Flask(__name__)

alltodos = []
newTodo = []


@app.route('/', methods=['POST', 'get'])
def Home():
    if request.method == 'POST':
        newTodo = [request.form["title"], request.form["desc"]]
        newDict = {"title": request.form["title"],
                   "desc": request.form["desc"]}
        alltodos.append(newDict)
        print(alltodos)

    return render_template('index.html', allToDo=alltodos)


@app.route('/about', methods=['POST', 'GET'])
def About():
    if request.method == "POST":
        return "hello akash"
    return render_template('about.html')


@app.route('/delete/<title>/<desc>', methods=['POST', 'GET'])
def delete(title, desc):
    for i in range(len(alltodos)):
        print(alltodos[i]["title"])
        if alltodos[i]["title"] == title:
            del alltodos[i]
            break
    print(alltodos)
    return "hello"


# without app.run we can't run this app :)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
