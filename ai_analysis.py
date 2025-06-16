from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import PyPDF2
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Asegúrate de que exista la carpeta donde se guardará el modelo
os.makedirs("modelo_beto_sesgo", exist_ok=True)

# Ruta donde se espera el archivo de pesos
model_path = "modelo_beto_sesgo/model.safetensors"

# Descargar desde Google Drive si no existe
if not os.path.exists(model_path):
    import gdown
    url = "https://drive.google.com/uc?id=1OtDgQzNJkVbLKRR0zjw2qVbsNlfJ1zdd"
    gdown.download(url, model_path, quiet=False)

# Cargar modelo y tokenizer desde carpeta local
model_dir = "modelo_beto_sesgo"
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir)
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def analizar_equidad(file):
    file.stream.seek(0)
    reader = PyPDF2.PdfReader(file.stream)
    texto = ""
    for page in reader.pages:
        texto += page.extract_text() or ""
    
    resultado = classifier(texto[:512])
    label = resultado[0]['label']
    score = resultado[0]['score']
    if label == 'LABEL_0':
        porcentaje_equidad = round(score * 100, 2)
        mensaje = "Hay equidad"
    else:
        porcentaje_equidad = round((1 - score) * 100, 2)
        mensaje = "No hay equidad"
    return porcentaje_equidad, mensaje

def analizar_equidad_texto(texto):
    resultado = classifier(texto[:512])
    label = resultado[0]['label']
    score = resultado[0]['score']
    if label == 'LABEL_0':
        porcentaje_equidad = round(score * 100, 2)
        mensaje = "Hay equidad"
    else:
        porcentaje_equidad = round((1 - score) * 100, 2)
        mensaje = "No hay equidad"
    return porcentaje_equidad, mensaje

@app.route('/subir_pdf', methods=['POST'])
def subir_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    porcentaje, mensaje = analizar_equidad(file)
    return jsonify({'porcentaje': porcentaje, 'mensaje': mensaje})

if __name__ == '__main__':
    app.run(debug=True)

####
