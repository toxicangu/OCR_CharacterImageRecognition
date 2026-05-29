Angel Octavio Mercado Perez | A01772335

# OCR Reconocimiento de Texto en Imagen

Este proyecto es un sistema web de OCR (Optical Character Recognition) desarrollado con Django, OpenCV y Tesseract OCR. La aplicación permite subir imágenes desde una interfaz HTML, aplicar filtros de preprocesamiento opcionales y extraer automáticamente el texto contenido en las imágenes. El texto detectado y las métricas de procesamiento se almacenan posteriormente en una base de datos.

---

# Características

- Subida de imágenes desde una interfaz web
- Extracción de texto mediante Tesseract OCR    
- Aplicación de filtros OpenCV antes del OCR
- Almacenamiento del texto detectado en la base de datos
- Sobrescritura automática del texto si la imagen es actualizada
- Visualización de métricas del OCR:
  - Tiempo de procesamiento
  - Cantidad de texto detectado
- Soporte para OCR en español e inglés

---

# Tecnologías utilizadas

- Python
- Django
- OpenCV
- Tesseract OCR
- Pillow
- SQLite

---

# Dependencias necesarias

Antes de ejecutar el proyecto, es necesario instalar todas las dependencias requeridas.

## Paquetes de Python

Instalar los siguientes paquetes:
pip install django
pip install pillow
pip install pytesseract
pip install opencv-python
pip install numpy

O todo de una vez:
pip install django pillow pytesseract opencv-python numpy

- Subida de imágenes desde una interfaz web
- Extracción de texto mediante Tesseract OCR
- Aplicación de filtros OpenCV antes del OCR
- Almacenamiento del texto detectado en la base de datos
- Sobrescritura automática del texto si la imagen es actualizada
- Visualización de métricas del OCR:
  - Tiempo de procesamiento
  - Cantidad de texto detectado
- Soporte para OCR en español e inglés

# Instalación del proyecto

## 1. Clonar el repositorio

```bash
git clone <https://github.com/toxicangu/OCR_CharacterImageRecognition>
```

Entrar al proyecto:

```bash
cd <ocr_project>
```

# 2. Instalar dependencias de Python

Instalar todas las dependencias necesarias:

```bash
pip install django pillow pytesseract opencv-python numpy
```

---
# 3. Instalar Tesseract OCR

Este proyecto requiere instalar Tesseract OCR manualmente.

## Descargar Tesseract

Descargar desde:

https://github.com/UB-Mannheim/tesseract/wiki

---

# 4. Instalar Tesseract

Durante la instalación:

- Activar:
  - "Add Tesseract to PATH"
- Instalar idiomas:
  - Spanish
  - English

---

# 5. Verificar instalación

Abrir CMD y ejecutar:

```bash
tesseract --version
```

Debe mostrarse algo como:

```bash
tesseract 5.x.x
```

---

# 6. Verificar idiomas instalados

```bash
tesseract --list-langs
```

Debe aparecer:

```bash
eng
spa
```

---

# 7. Configurar Tesseract en Django

En `views.py` agregar:

```python
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

os.environ["TESSDATA_PREFIX"] = (
    r"C:\Program Files\Tesseract-OCR\tessdata"
)
```

---

# Estructura del proyecto

```text
ocr_project/
│
├── manage.py
├── db.sqlite3
│
├── media/
│
├── ocr/
│   ├── migrations/
│   ├── templates/
│   │   ├── upload.html
│   │   └── result.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── ocr_project/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
# Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Ejecutar servidor

```bash
python manage.py runserver
```

Abrir:

```text
http://127.0.0.1:8000
```

---

# Funcionamiento del sistema

1. El usuario sube una imagen
2. Selecciona un filtro OpenCV
3. La imagen se procesa
4. Tesseract extrae el texto
5. Se calculan métricas
6. Los datos se guardan en SQLite
7. El resultado se muestra en pantalla

---

# Métricas generadas

El sistema almacena:

- Texto detectado
- Cantidad de caracteres detectados
- Tiempo de procesamiento
- Imagen procesada
- Fecha de carga

---

# Filtros disponibles

| Filtro | Descripción |
|---|---|
| Grayscale | Convierte la imagen a escala de grises |
| Threshold | Mejora contraste para OCR |
| Blur Reduction | Reduce ruido |
| Sharpen | Mejora nitidez |

---

# Notas importantes

- OCR funciona mejor con:
  - Texto negro
  - Fondo blanco
  - Imágenes nítidas
  - PNG de alta calidad
