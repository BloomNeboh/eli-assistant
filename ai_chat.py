import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        max_tokens=150
    )
    return response.choices[0].message['content']

