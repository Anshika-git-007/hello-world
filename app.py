from flask import Flask, render_template

app = Flask(__name__)


@app.route("/click", methods=['GET'])
def click():
    """You should navigate here first.
    On clicking click button , it will redirect to txt.
    """
	return render_template('click_button.html')


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.debug = os.environ.get('FLASK_DEBUG', True)
    app.run(port=6000)
