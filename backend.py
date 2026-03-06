from flask import Flask, request, jsonify
from Prompt import AyrisAI
from flask_cors import CORS

AI = AyrisAI()
app = Flask(__name__)
CORS(app)

arquivo = "/home/asm/Documentos/Ayris-main/Ayris/Source/Set/fundamentos.txt"

with open(arquivo, "r", encoding="utf-8") as f:
    fundamentos = f.read()

X1 = fundamentos

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    # Exemplo de lógica simples de resposta
    bot_reply = AI.Prompt(X1, user_message)
    
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True, port=5000)