from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height_cm = float(request.form['height'])
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

    return render_template('mi.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
