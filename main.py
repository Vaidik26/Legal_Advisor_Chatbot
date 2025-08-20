from src.vector_store import load_vector
from src.prompt import prompt
from src.utils import llm_load
from llama_index.core.prompts import PromptTemplate
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

llm = llm_load()

index = load_vector()

qa_prompt = PromptTemplate(prompt)

chat_engine = index.as_chat_engine(text_qa_prompt = qa_prompt, llm=llm)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print("User:", msg)
    
    response = chat_engine.chat(msg)
    print("Response:", response.response)
    
    return response.response.strip()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)