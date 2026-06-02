from flask import Flask, request, jsonify

app = Flask(__name__)

# Nosso banco de dados falso. A senha correta aqui é "admin"
DADOS_DE_ACESSO = {
    "admin": "admin"
}

@app.route('/login', methods=['POST'])
def realizar_login():
    # O app recebe as tentativas enviadas pelo script de ataque
    usuario = request.form.get("username")
    senha = request.form.get("password")
    
    # Valida se o usuário e a senha batem com o banco de dados
    if usuario in DADOS_DE_ACESSO and DADOS_DE_ACESSO[usuario] == senha:
        return jsonify({"status": "sucesso", "mensagem": "Acesso concedido!"}), 200
        
    return jsonify({"status": "erro", "mensagem": "Senha errada."}), 401

if __name__ == "__main__":
    # Inicia o servidor local na porta 5000
    print("[*] Iniciando laboratório web vulnerável...")
    app.run(host="127.0.0.1", port=5000, debug=True)
        