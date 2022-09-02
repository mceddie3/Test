from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        x = request.args.get('x')
        y = request.args.get('y')
        print(x,y)
    return render_template("index.html")


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
