from flask import Flask, render_template, request, jsonify
from ai_analysis import analizar_equidad, analizar_equidad_texto

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subir_pdf', methods=['POST'])
def subir_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No se envió archivo'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nombre de archivo vacío'}), 400

    porcentaje_equidad, mensaje = analizar_equidad(file)
    return jsonify({'porcentaje': porcentaje_equidad, 'mensaje': mensaje})

@app.route('/analizar_texto', methods=['POST'])
def analizar_texto():
    data = request.get_json()
    texto = data.get('texto', '')
    porcentaje, mensaje = analizar_equidad_texto(texto)
    return jsonify({'porcentaje': porcentaje, 'mensaje': mensaje})

if __name__ == '__main__':
    app.run(debug=True)
