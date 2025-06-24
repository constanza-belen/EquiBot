from flask import Flask, render_template, request, jsonify
from ai_analysis import analizar_equidad, analizar_equidad_texto

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analizar_texto", methods=["POST"])
def analizar_texto():
    data = request.get_json()
    resultado = analizar_equidad_texto(data["texto"])
    return jsonify(resultado)

@app.route("/subir_pdf", methods=["POST"])
def subir_pdf():
    file = request.files["file"]
    resultado = analizar_equidad(file)
    return jsonify(resultado)