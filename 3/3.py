from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 1


if __name__ == '__main__': #запуск
    app.run()