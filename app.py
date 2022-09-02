from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


# global variable holding game data
game_data = []

# global variable holding who's turn it is (X or O)
is_x_turn = True


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        x = request.args.get('x')
        y = request.args.get('y')
        print(x, y)

    # flip turn with boolean logic
    global is_x_turn
    is_x_turn = not is_x_turn
    return render_template("index.html", game_data=game_data, is_x_turn=is_x_turn)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", game_data=game_data, is_x_turn=is_x_turn)


if __name__ == '__main__':
    # init game data
    game_data = 3*[3*[""]]
    app.run()
