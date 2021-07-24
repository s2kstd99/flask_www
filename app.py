from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! 바보멍충이 ggggg'

@app.route('/main')
def show_main_page():
    html = "<html><body>니가바보</body></html>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)