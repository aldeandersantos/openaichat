from flask import Flask, request, render_template_string
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

app = Flask(__name__)
client = OpenAI()

HTML = '''
<form method="post">
  Pergunta: <input name="pergunta" />
  <button type="submit">Enviar</button>
</form>
<p><strong>Resposta:</strong> {{ resposta }}</p>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        pergunta = request.form["pergunta"]
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pergunta}]
        ).choices[0].message.content
    return render_template_string(HTML, resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)