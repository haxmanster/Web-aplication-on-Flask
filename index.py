from flask import Flask,render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
 return render_template('index.html')

path = 'c:/'
dirs = [os.listdir(path)]

def list_dir():
  for file in dirs:

    return file

app.jinja_env.globals.update(list_dir=list_dir)

if __name__ == "__main__":
 app.run(host='0.0.0.0',debug=True)
