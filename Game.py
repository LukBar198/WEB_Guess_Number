from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    min_number = 0
    max_number = 1000
    # guess = (max_number - min_number) // 2 + min_number
    if request.method == 'GET':
        return render_template('start.html', min_number=min_number, max_number=max_number)
    else:
        min_number = int(request.form.get("min_number"))
        max_number = int(request.form.get("max_number"))
        user_response = request.form.get("user_response")

        guess = (max_number - min_number) // 2 + min_number

        if user_response == "too big":
            max_number = guess
        elif user_response == "too small":
            min_number = guess
        elif user_response == "you won":
            return render_template('win.html', guess=guess)

        guess = ((max_number - min_number) // 2) + min_number
        return render_template('game.html', guess=guess, min_number=min_number, max_number=max_number)


if __name__ == '__main__':
    app.run()
