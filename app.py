from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])

    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        roots = f"Корни уравнения: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        roots = f"Уравнение имеет один корень: {root}"
    else:
        roots = "Уравнение не имеет действительных корней"

    return render_template('index.html', roots=roots)

if __name__ == '__main__':
    app.run()


