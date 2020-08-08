from collections import defaultdict
from typing import DefaultDict
import click
from flask import Flask

app = Flask(__name__)


@app.route('/index',defaults={'name':'Programmer'})
@app.route('/index/<name>')
def index(name):
    return "<h1>hello %s!</h1>" % name

@app.cli.command()
def hello():
    click.echo('Hello, Human!')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)