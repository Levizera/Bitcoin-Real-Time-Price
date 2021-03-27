from flask import Flask, render_template, request
import price_tracker as pt

app = Flask(__name__)
btc = pt.GetResponse()

@app.route('/')
def page():
    return render_template('index.html', btc_price=btc.get_response())

if __name__ == '__main__':
    app.run()
