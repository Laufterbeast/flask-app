from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask in Codespaces!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/two')

def hello2():

    return "Hello again from Flask in Codespaces!"

@app.route('/three')

def hello2():

    return "Hello again again from Flask in Codespaces!"