
# EquiBot

**EquiBot** es una aplicación web que permite analizar archivos PDF o texto libre para detectar posibles sesgos de género, utilizando un modelo de lenguaje entrenado con BETO (BERT en español).

Este proyecto forma parte del trabajo del equipo de investigación de sesgos del programa **InES de Género**.

---

## ¿Qué hace esta app?

1. Permite subir un archivo PDF o escribir texto en la interfaz web.
2. Extrae el contenido del documento o usa el texto ingresado.
3. Clasifica automáticamente el texto como **con** o **sin sesgo de género** usando un modelo de aprendizaje automático basado en Transformers.
4. Muestra el **porcentaje estimado de equidad de género** y un mensaje interpretativo.

---

## Requisitos

- Python 3.10 o superior
- Compatible con CPU
- Recomendado usar entorno virtual

---

## Instalación

1. Clona o descomprime el repositorio:

   ```bash
   unzip EquiBot.zip
   cd EquiBot
   ```

2. Instala las dependencias:

   ```bash
   pip install flask flask-cors transformers torch pymupdf
   ```

---

## Ejecución

1. Inicia el backend Flask:

   ```bash
   python app.py
   ```

2. Abre tu navegador y ve a:

   ```
   http://127.0.0.1:5000/
   ```

   Allí verás la interfaz para subir PDFs o escribir texto.

---

## Estructura del proyecto

```
EquiBot/
├── app.py                   # Servidor Flask con endpoints
├── ai_analysis.py           # Lógica del análisis con BETO
├── modelo_beto_sesgo/       # Carpeta con el modelo entrenado (Transformers)
├── static/                  # Recursos estáticos (CSS, JS si los hubiera)
├── templates/
│   └── index.html           # Plantilla HTML principal renderizada por Flask
```

---

## Créditos y equipo

Desarrollado por el equipo de investigación de sesgos del programa **InES de Género**.

- Mabel Vega, investigadora principal y líder del proyecto. mabel.vega@umayor.cl
- Cristian Gutierrez, co-investigador, cristian.gutierrez@umayor.cl
- Dariana Mindiola, co-investigadora, dariana.mindiola@umayor.cl
- Christian Yañéz, co-investigador, christian.yanez@umayor.cl
- Nicolás Villanueva, asistente de investigación, nicolas.villanueva@mayor.cl
- Constanza Orellana, asistente de investigación, constanza.orellanar@umayor.cl

---
## Consideraciones éticas

Este modelo es una herramienta de apoyo al análisis de textos con enfoque de género, pero **no reemplaza evaluaciones humanas**. Puede fallar en contextos ambiguos, sarcasmo o frases muy técnicas.

Se recomienda usarlo junto a estrategias pedagógicas, de revisión editorial o de formación institucional.

---
## Licencia

Este proyecto es parte de una investigación en curso. Para usos académicos o institucionales, contactar a sus responsables.

