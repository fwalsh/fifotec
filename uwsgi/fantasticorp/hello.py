from flask import Flask
from jinja2 import Environment, PackageLoader


app = Flask(__name__)
env = Environment(loader=PackageLoader('fantasticorp', 'templates'))

@app.route('/')
def hello():
    template = env.get_template('index.html')
    return template.render()

if __name__ == "__main__":
    app.run()
