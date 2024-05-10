import os
import random
import json  # Para guardar datos en formato JSON
import openai

# Configurar la clave de API de OpenAI
api_key = "tu_clave_de_api"  # O usa os.getenv("OPENAI_API_KEY") para extraer de variables de entorno
openai.api_key = api_key

# Listas de categorías, subcategorías, facetas y feedback
categorias = ["Tecnología", "Salud", "Educación", "Finanzas", "Deportes"]
subcategorias = ["Software", "Hardware", "Medicina", "Enfermería", "Biología"]
facetas = ["Innovación", "Practicidad", "Estabilidad", "Costo", "Desempeño"]
feedbacks = ["Positivo", "Negativo", "Neutral", "Mejorable", "Excelente"]

# Función para seleccionar elementos aleatorios de las listas
def seleccionar_aleatorio():
    return {
        "categoria": random.choice(categorias),
        "subcategoria": random.choice(subcategorias),
        "faceta": random.choice(facetas),
        "feedback": random.choice(feedbacks),
    }

# Función para generar datos sintéticos
def generar_datos_sinteticos(prompt_base, cantidad_datos):
    datos = []

    for _ in range(cantidad_datos):
        # Seleccionar elementos aleatorios para crear un nuevo prompt
        seleccion = seleccionar_aleatorio()

        prompt = fr'''
Categoría: {seleccion["categoria"]}
- Subcategoría: {seleccion["subcategoria"]}
  - Faceta: {seleccion["faceta"]}
  - Resumen del Comportamiento: {seleccion["feedback"]}

Salida Esperada:

Plan de Mejora:

1. Comunicación

- Subcategoría: Verbal
    - Objetivo: Mejorar la interacción con la audiencia durante las presentaciones de proyectos.
    - Estrategia: 
      1. Preparación de Preguntas: Anticipar preguntas comunes para responderlas de manera efectiva.
      2. Práctica con Feedback: Simulaciones y retroalimentación constructiva.
      3. Contacto Visual y Movimientos: Enfatizar puntos clave con contacto visual y movimientos naturales.
'''

        # Llamar a la API de OpenAI para generar datos
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-0125",  # Modelo preferido
            prompt=prompt,
            max_tokens=100,  # Ajusta según necesidades
            temperature=0.7,  # Ajusta según la variabilidad deseada
        )

        # Guardar la respuesta
        datos.append({
            "input": seleccion,
            "output": response.choices[0].text.strip(),
        })

    return datos

# Función para guardar datos en un archivo JSON
def guardar_datos_json(datos, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

# Ejemplo de uso
prompt_base = r'''Eres un experto en desarrollo personal y profesional. Genera un plan de mejora detallado y personalizado basado en estas categorías y subcategorías.'''
cantidad_datos = 5  # Cambia según tus necesidades

datos_generados = generar_datos_sinteticos(prompt_base, cantidad_datos)

# Guardar datos generados en un archivo JSON
nombre_archivo = "datos_sinteticos.json"
guardar_datos_json(datos_generados, nombre_archivo)

# Imprimir la confirmación de guardado
print(f"Datos guardados en {nombre_archivo}")

