from transformers import pipeline

# Carga del modelo T5 base orientado a QA
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def ask_question(prompt):
    if not prompt.strip():
        return "⚠️ La pregunta está vacía."

    try:
        response = qa_pipeline(f"Pregunta: {prompt}", max_new_tokens=100)
        return response[0]["generated_text"].strip()
    except Exception as e:
        return f"❌ Error al procesar la pregunta: {e}"

if __name__ == "__main__":
    print("🤖 Asistente con FLAN-T5. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            break
        print("IA:", ask_question(user_input))




# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def ask_question(prompt, temperature=0.7):
#     try:
#         if not prompt.strip():
#             return "⚠️ La pregunta está vacía. Intenta con otra."
        
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=temperature,
#             max_tokens=150
#         )
#         answer = response.choices[0].message["content"].strip()
#         return answer or "❌ No se obtuvo respuesta del modelo."
#     except Exception as e:
#         return f"❌ Error al procesar la pregunta: {e}"

# if __name__ == "__main__":
#     print("🤖 Asistente IA. Escribe 'salir' para terminar.")
#     while True:
#         user_input = input("Tú: ")
#         if user_input.lower() == "salir":
#             break
#         respuesta = ask_question(user_input)
#         print(f"IA: {respuesta}\n")
