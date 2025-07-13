from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import PyPDF2
import os

# Usar ruta relativa válida en Render
model_dir = os.path.join(os.path.dirname(__file__), "modelo_beto_sesgo")

# Cargar modelo y tokenizer
model = AutoModelForSequenceClassification.from_pretrained(model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_dir)
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def analizar_equidad(file):
    file.stream.seek(0)
    reader = PyPDF2.PdfReader(file.stream)
    texto = "".join([page.extract_text() or "" for page in reader.pages])
    resultado = classifier(texto[:512])
    label = resultado[0]['label']
    score = resultado[0]['score']
    if label == 'LABEL_0':
        return round(score * 100, 2), "Hay equidad"
    else:
        return round((1 - score) * 100, 2), "No hay equidad"

def analizar_equidad_texto(texto):
    resultado = classifier(texto[:512])
    label = resultado[0]['label']
    score = resultado[0]['score']
    if label == 'LABEL_0':
        return round(score * 100, 2), "Hay equidad"
    else:
        return round((1 - score) * 100, 2), "No hay equidad"
