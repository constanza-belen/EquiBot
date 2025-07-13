# EquiBot 

![EquiBot logo](./Captura%20de%20Pantalla%202025-07-13%20a%20la(s)%2013.58.27.png)

EquiBot es un algoritmo en proceso de desarrollo que tiene como propósito crear una herramienta de apoyo para la detección de sesgo de género en textos educacionales. Está siendo entrenado para detectar sesgos de género en lenguaje de forma automática usando Inteligencia Artificial.

---

## Demo visual

![Captura de pantalla](./Captura%20de%20Pantalla%202025-07-13%20a%20la(s)%2013.58.27.png)

Puedes ver el sitio en vivo en: [https://equibot.cl](https://equibot.cl)

---

## Instalación local

### Requisitos:
- Python 3.10 o 3.11
- Git

### Clonar el repositorio:
```bash
git clone https://github.com/constanza-belen/EquiBot.git
cd EquiBot
```

### Crear entorno virtual e instalar dependencias:
```bash
python -m venv venv
source venv/bin/activate   # En Mac/Linux
venv\Scripts\activate      # En Windows

pip install -r requirements.txt
```

### Requisitos en `requirements.txt`
```txt
flask>=2.0
transformers>=4.31
torch>=2.0
safetensors
PyPDF2>=3.0
gunicorn
```

### Ejecutar localmente
```bash
python app.py
```

La app quedará disponible en `http://localhost:5000`

---

## Modelo entrenado

EquiBot utiliza una versión ajustada de [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased), un modelo de lenguaje entrenado por la Universidad de Chile.

Se entrenó localmente en un conjunto balanceado de frases con y sin sesgo de género, usando aprendizaje supervisado.

El modelo ajustado está disponible en Hugging Face:

**🔗 https://huggingface.co/constanza-belen/Modelo_EquiBot**

> ✉️ El modelo es público, no requiere token y puede ser utilizado por otras personas.

---

## 🌍 Estructura del proyecto
```
EquiBot/
├── app.py                # Lógica Flask
├── ai_analysis.py        # Análisis con transformers + modelo
├── requirements.txt
├── static/               # CSS, logo, etc.
│   └── style.css
├── templates/            # HTML
│   └── index.html
```

---

## Licencia

Este proyecto se distribuye bajo una **[Licencia Creative Commons BY-NC](https://creativecommons.org/licenses/by-nc/4.0/deed.es)**:
- ✅ Se permite usar, modificar y compartir
- ❌ No se permite uso comercial
- ✅ Se debe dar crédito al equipo desarrollador

---

## Contribuciones

¡Estás invitado/a a colaborar! Puedes:
- Proponer mejoras o ideas
- Reportar errores
- Sugerir nuevos tipos de sesgo o ejemplos para reentrenamiento

Pull requests son bienvenidos, pero actualmente no se revisan de forma regular.

---

## Autores y contacto

Proyecto desarrollado por un equipo de investigadores/as e ingenieros/as patrocinados por el fondo de investigación otorgado por **InES de Género - Universidad Mayor**.
- Cristian Gutierrez, co-investigador, cristian.gutierrez@umayor.cl

- Dariana Mindiola, co-investigadora, dariana.mindiola@umayor.cl

- Constanza Orellana, asistente de investigación, constanza.orellanar@umayor.cl

- Nicolás Villanueva, asistente de investigación, nicolas.villanueva@mayor.cl

- Mabel Vega, investigadora principal y líder del proyecto, mabel.vega@umayor.cl

- Christian Yañéz, co-investigador, christian.yanez@umayor.cl

📧 Contacto: **contacto@equibot.com**