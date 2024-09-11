from flask import Flask, send_file, render_template

app = Flask(__name__)

# Rota para servir o HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para servir o arquivo XML gerado
@app.route('/xml')
def xml_file():
    return send_file('dados_convertidos.xml', mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True)
