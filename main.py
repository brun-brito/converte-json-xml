import os
from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/xml')
def get_xml():
    return send_file('dados_convertidos.xml', mimetype='application/xml')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
