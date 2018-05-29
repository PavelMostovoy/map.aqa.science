from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello worlda again'

if __name__ == '__main__':
    app.run(debug=False, host='aqa.science')
