from flask import Flask, render_template, request

site = Flask(__name__)

@site.route('/')
def home():
    return render_template('home.html')

@site.route('/listCars')
def listCars():
    return render_template('CarList.html')

@site.route('/car1')
def car1():
    return render_template('Car1.html')
@site.route('/car2')
def car2():
    return render_template('Car2.html')
@site.route('/car3')
def car3():
    return render_template('Car3.html')
if __name__ == "__main__":
    print("Запуск сайта...")
    site.run(debug=True)

    print("Закрытие сайта...")