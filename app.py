from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


# global variable holding game data
game_data = []

# global variable holding who's turn it is (X or O)
is_x_turn = True


# determine if a user has just won the game
def has_user_won():
    global game_data

    # add logic here
    return False


# update the game data with x and y
def update_game_state(x_coordinate, y_coordinate):
    global game_data
    # update game data here


@app.route('/result', methods=['POST', 'GET'])
def result():
    global is_x_turn
    if request.method == 'GET':
        x = request.args.get('x')
        y = request.args.get('y')
        update_game_state(x, y)

        if has_user_won():
            if is_x_turn:
                return "X WON"
            else:
                return "O WON"

    # flip who's turn it is with boolean logic
    is_x_turn = not is_x_turn
    return render_template("index.html", game_data=game_data, is_x_turn=is_x_turn)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", game_data=game_data, is_x_turn=is_x_turn)


if __name__ == '__main__':
    # init game data
    game_data = [["" for i in range(3)] for j in range (3)]
    is_x_turn = True

    # experiment with setting game_data
    game_data[1][2] = "THIS IS SET"

    app.run()
