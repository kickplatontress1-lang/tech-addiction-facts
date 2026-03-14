from flask import Flask
import random

def gen_pass():
    elements = "+-/*!&$#?=@<>123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    password = ""

    for i in range(15):
        password += random.choice(elements)

    return password

facts_list = [
    "Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
    "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
    "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время."
]
ftc = ["Орёл", "Решка"]
imglinks = [
    "/images/mem1.jpeg",
    "/images/mem2.jpeg",
    "/images/mem3.png",
    "/images/mem4.png",
    "/images/mem5.png",
    "/images/mem6.png"
]
password = gen_pass()
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Привет! Здесь ты можешь узнать пару интересных фактов о технологических зависимостях!</h1> <a href="/random_fact">Посмотреть случайный факт!</a>'

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p> <a href="/">Назад</a> <br> <a href="/secret">???</a>'

@app.route("/secret")
def secret():
    return '<h1>Ты нашёл тайную страницу!</h1> <a href="/random_fact">Назад</a> <p><b>Игры:</b></p> <a href="/coin">Монета</a> <br> <a href="/pwd">Генератор паролей</a> <br> <a href="/randimg">Случайная картинка (не работает)</a>'

@app.route("/coin")
def coin():
    return f'<h1>{random.choice(ftc)}</h1> <a href="/coin">Ещё раз</a> <br> <a href="/secret">Назад</a>'

@app.route("/pwd")
def pwd():
    return f'<h1>Пароль:</h1> <p>{password}</p> <a href="/secret">Назад</a>'

@app.route("/randimg")
def randimg():
    return f'<h1>Случайная картинка!</h1> <img src="{random.choice(imglinks)}"> <a href="/randimg">Ещё раз</a> <br> <a href="/secret">Назад</a>'

app.run(debug=True)
