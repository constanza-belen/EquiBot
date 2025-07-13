from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import PyPDF2

# Nombre de tu modelo en Hugging Face
model_name = "constanza-belen/Modelo_EquiBot"

# Cargar modelo y tokenizer desde Hugging Face
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
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
