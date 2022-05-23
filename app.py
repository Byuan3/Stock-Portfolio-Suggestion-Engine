from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
portfolio = 0.0
data = []


@app.route('/', methods=['GET'])
def index():
    global portfolio, data
    return render_template('index.html', portfolio=portfolio, data=data)


@app.route('/add', methods=['POST'])
def add():
    global portfolio
    if request.method == 'POST':
        amount = request.form.get('amount')
        e = request.form.get('Ethical')
        g = request.form.get('Growth')
        i = request.form.get('Index')
        q = request.form.get('Quality')
        v = request.form.get('Value')
        if amount.isnumeric():
            portfolio += float(amount)
            flash('Add $' + amount)
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    global portfolio
    if request.method == 'POST':
        portfolio = 0
        flash('Your portfolio is reset!')
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
