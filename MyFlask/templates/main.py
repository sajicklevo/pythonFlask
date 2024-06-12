from urllib import request

from flask import Flask,render_template

app = Flask(__name__)



@app.route('/submit', methods=['POST'])
def submit():
  name = request.form['name']
  return f'Hello, {name}'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/home/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
