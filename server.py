from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num)

app = Flask(__name__)


@app.route('/')
def home():
    return ("<h1>Adivina un número entre el 0 y el 9 y\nagrégalo al final de la URL.</h1>"
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGk0eW8yZnVjeDJzaDhzb3phbmMxam5md2d2d2RuaDVmOHI"
            "yY3JocSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IsfrRWvbUdRny/giphy.gif' width=500>")

@app.route('/<int:number>/')
def guess_number(number):
    global random_num
    if number < random_num:
        return ("<h1>Como Polar en la puerta: Demasiado bajo!</h1>"
                "<img src='https://media.giphy.com/media/fYfYKBGS0gsA6Pk9GS/giphy.gif?cid=790b76112buitdi2aodt6c3x71"
                "r4s20zves45fxvkyr2miwu&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=500>")

    elif number > random_num:
        return ("<h1>Polar tendrá su venganza porque es demasiado alto!</h1>"
                "<img src='https://media.giphy.com/media/WRc6sTKlt9CCWJPteI/giphy.gif?cid=790b76112buitdi2aodt6c3"
                "x71r4s20zves45fxvkyr2miwu&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=500>")
    else:
        random_num = random.randint(0, 9)
        print(random_num)
        return ("<h1>Lo tienes! Inténtalo de nuevo</h1>"
                "<img src='https://media.giphy.com/media/ODFgxlLY4dbysNnKEM/giphy.gif?cid=ecf05e47z157xmanjpg34vcicf59"
                "qo52cuhzcukfxu9v0mmj&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=500>")


if __name__ == "__main__":
    app.run(debug=True)
