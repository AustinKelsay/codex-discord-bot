import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask(q):
  # write each question to a txt file
  with open("questions.txt", "a") as f:
        f.write(q + "\n")

  response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=f"/*{q}*/",
        stop="/",
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.3)

  return response.choices[0].text