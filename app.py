from flask import Flask, render_template, request, redirect, flash
from StockEngine import StockEngine
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
portfolio = 0.0
data = [0, 0, 0, 0, 0]
date = []
profile = []
se = StockEngine()
se.updateDf()

scheduler = BackgroundScheduler()
job1 = scheduler.add_job(se.updateDf, 'interval', minutes=2400)
job2 = scheduler.add_job(se.updateData, 'interval', minutes=2400)
scheduler.start()


@app.route('/', methods=['GET'])
def index():
    global portfolio, data, date
    date = se.date
    data = se.data
    return render_template('index.html', portfolio=portfolio, data=data, stocks=profile, date=date)


@app.route('/add', methods=['POST'])
def add():
    global portfolio, profile, data
    if request.method == 'POST':
        amount = request.form.get('amount')
        strategy = {'e': request.form.get('Ethical'), 'g': request.form.get('Growth'), 'i': request.form.get('Index'),
                    'q': request.form.get('Quality'), 'v': request.form.get('Value')}

        strategy = [k for (k, v) in strategy.items() if v == 'on']
        if amount.isnumeric() and len(strategy) != 0:
            investment = float(amount) / len(strategy)
            for s in strategy:
                se.addInvestment(s, investment)
            portfolio = se.netValue

            tmp = []
            for (stock, amt) in se.stocks.items():
                tmp.append(stock + ': $' + str(amt))
            profile = tmp

            flash('Add $' + amount + ' in total!')
        elif not amount.isnumeric():
            flash('Please enter a number!')
        elif len(strategy) == 0:
            flash('Please select at least one strategy!')

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    global portfolio, profile, data
    if request.method == 'POST':
        portfolio = 0
        profile = []
        se.reset()
        flash('Your portfolio is reset!')
    return redirect('/')


@app.route('/test', methods=['POST'])
def test():
    global portfolio, profile, date
    if request.method == 'POST':
        flash(date)
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8081)
