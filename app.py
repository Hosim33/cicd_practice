from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/cloud')
def hello_cloud():
    return 'AWS, Azure, GCP!'

if __name__ == '__main__':
    app.run()
