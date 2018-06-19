from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    iframe = "map"
    return render_template("index.html",iframe=iframe)

@app.route('/location')
def location():
    return render_template("location.html")

@app.route('/map')
def map():
    return render_template("Map1.html")

if __name__ == '__main__':
    app.run(debug=False, host='aqa.science')
