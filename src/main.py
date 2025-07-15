
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return """<html><head><title>Netflix Clone</title></head>
    <body style='text-align:center;font-family:sans-serif'>
        <h1>Welcome to Netflix Clone 🎬</h1>
        <p>Stream your favorite shows, right here.</p>
        <img src='https://upload.wikimedia.org/wikipedia/commons/7/75/Netflix_icon.svg' height='100'/>
    </body></html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)