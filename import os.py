import os
import random
import openai

# Configurar la clave de API de OpenAI
api_key = "no_me_Deja_subirlo_con_el_api"  # O usa os.getenv("OPENAI_API_KEY") para extraer de variables de entorno
openai.api_key = api_key

# Listas de categorías, subcategorías, facetas y feedback
categorias = ["Tecnología", "Salud", "Educación", "Finanzas", "Deportes"]
subcategorias = ["Software", "Hardware", "Medicina", "Enfermería", "Biología"]
facetas = ["Innovación", "Practicidad", "Estabilidad", "Costo", "Desempeño"]
feedbacks = ["Positivo", "Negativo", "Neutral", "Mejorable", "Excelente"]

# Función para generar datos sintéticos
def generar_datos_sinteticos(prompt_base, cantidad_datos):
    datos = []

    for _ in range(cantidad_datos):
        # Seleccionar elementos aleatorios para crear un nuevo prompt
        categoria = random.choice(categorias)
        subcategoria = random.choice(subcategorias)
        faceta = random.choice(facetas)
        feedback = random.choice(feedbacks)

        # Crear el prompt para OpenAI
        # prompt = f"{prompt_base}\nCategoría: {categoria}\nSubcategoría: {subcategoria}\nFaceta: {faceta}\nFeedback: {feedback}\nGenera datos sintéticos relacionados con estos elementos."
        prompt = fr'''
Categoría: {categoria}

- Subcategoría: {subcategoria}
    - Faceta: {faceta}
    - Resumen del Comportamiento: {feedback}

Salida Esperada:

Plan de Mejora:

1. Comunicación

- Subcategoría: Verbal
    - Objetivo:
      Mejorar la interacción con la audiencia durante las presentaciones de proyectos.
    - Estrategia:
      1. Preparación de Preguntas: Anticipar preguntas comunes de la audiencia para responderlas de manera efectiva.
      2. Práctica con Feedback: Realizar presentaciones simuladas y recibir retroalimentación constructiva.
      3. Contacto Visual y Movimientos: Fomentar el contacto visual con diferentes miembros de la audiencia y utilizar movimientos naturales para enfatizar puntos clave.
- Subcategoría: No Verbal
    - Objetivo:
      Mejorar el contacto visual durante las reuniones de equipo.
    - Estrategia:
      1. Simulaciones de Reuniones: Participar en simulaciones de reuniones para mejorar el contacto visual.
      2. Feedback de Compañeros: Pedir a compañeros observadores que den retroalimentación específica sobre el contacto visual.
      3. Mantener la Atención: Fijar la mirada en cada persona al menos 2-3 segundos durante las interacciones.'''


        # Llamar a la API de OpenAI para generar datos
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-0125",  # Usa el modelo que prefieras
            prompt=prompt,
            max_tokens=100,  # Ajusta según tus necesidades
            temperature=0.7,  # Ajusta según la variabilidad deseada
        )

        # Agregar el resultado a la lista de datos
        datos.append(response.choices[0].text.strip())

    return datos

# Ejemplo de uso
prompt_base = r'''Eres un experto en desarrollo personal y profesional con un enfoque en habilidades blandas. Tu tarea es proporcionar un plan de mejora personalizado basado en los siguientes datos, que incluyen las puntuaciones históricas, fechas, facetas y resúmenes del comportamiento.

Instrucciones:

1. Recibirás un conjunto de datos con las siguientes categorías y subcategorías, junto con sus respectivas puntuaciones, fechas, facetas (contexto) y resúmenes.
2. Debes analizar esta información y generar un plan de mejora detallado y personalizado para cada subcategoría, ofreciendo estrategias y recomendaciones específicas.
3. El plan debe incluir acciones prácticas para mejorar el rendimiento en las subcategorías identificadas.

Ejemplo de Datos:
1. Comunicación

- Subcategoría: Verbal
    - Objetivo:
      Mejorar la interacción con la audiencia durante las presentaciones de proyectos.
    - Estrategia:
      1. Preparación de Preguntas: Anticipar preguntas comunes de la audiencia para responderlas de manera efectiva.
      2. Práctica con Feedback: Realizar presentaciones simuladas y recibir retroalimentación constructiva.
      3. Contacto Visual y Movimientos: Fomentar el contacto visual con diferentes miembros de la audiencia y utilizar movimientos naturales para enfatizar puntos clave.
- Subcategoría: No Verbal
    - Objetivo:
      Mejorar el contacto visual durante las reuniones de equipo.
    - Estrategia:
      1. Simulaciones de Reuniones: Participar en simulaciones de reuniones para mejorar el contacto visual.
      2. Feedback de Compañeros: Pedir a compañeros observadores que den retroalimentación específica sobre el contacto visual.
      3. Mantener la Atención: Fijar la mirada en cada persona al menos 2-3 segundos durante las interacciones.'''
cantidad_datos = 5  # Cambia según tus necesidades

datos_generados = generar_datos_sinteticos(prompt_base, cantidad_datos)

# Imprimir o guardar los datos generados
for i, dato in enumerate(datos_generados):
    print(f"Dato {i+1}: {dato}")
