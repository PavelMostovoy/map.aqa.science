from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Map1.html")

@app.route('/location')
def location():
    return render_template("location.html")


if __name__ == '__main__':
    app.run(debug=False, host='aqa.science')
