from flask import Flask, request, render_template
from datetime import datetime
app = Flask(__name__)

alltodos = []
newTodo=[]

@app.route('/', methods=['POST'])
def Home():
    if request.method == 'POST':
        newTodo = [request.form["title"], request.form["desc"]]
        alltodos.append(newTodo)
        print(alltodos)

    return render_template('index.html', allToDo=alltodos)


@app.route('/about', methods=['POST', 'GET'])
def About():
    if request.method == "POST":
        return "hello akash"
    return render_template('about.html')


# without app.run we can't run this app :)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
