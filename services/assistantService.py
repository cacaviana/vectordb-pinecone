from services.authenticationService import authentication_OpenAI
from fastapi import Form


client_openai = authentication_OpenAI()


def assistant_question(question:str, shortextract:str):
    completion = client_openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant, who will respond only based on the excerpt sent to you."},
        {"role": "user", "content": f"The question{question} and the excerpt {shortextract}"}
    ])
    
    return completion.choices[0].message