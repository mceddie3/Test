from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route('/hello')
def hello(i):
    print(i)
    return 1


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/secret')
def my_secret_route():
    return 'don\'t tell'


@app.route('/questions/<int:question_id>')    #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
def find_question(question_id):
    return ('you asked for question{0}'.format(question_id))


if __name__ == '__main__':
    app.run()
