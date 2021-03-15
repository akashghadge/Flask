from flask import Flask, request, render_template
from datetime import datetime
app = Flask(__name__)

myList="akash"

@app.route('/', methods=['POST', 'GET'])
def Home():
    if request.method == "POST":
        print(request.form)

    return render_template('index.html.jinja')


@app.route('/about')
def About():
    return render_template('about.html')


# without app.run we can't run this app :)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
