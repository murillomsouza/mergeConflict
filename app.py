from flask import Flask, jsonify, request

app = Flask(__name__)

#Padrao
@app.route('/')
def index():
    return "Essa é minha atualização para o conflito"

#Get para verificar status
@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({
        "status": "OK",
        "mensagem": "A API está rodando perfeitamente!"
    })


@app.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def buscar_usuario(usuario_id):
    return jsonify({
        "status": "sucesso",
        "usuario_id": usuario_id,
        "mensagem": f"Usuario {usuario_id} encontrado."
    })

#Post ara enviar dados
@app.route('/api/dados', methods=['POST'])
def receber_dados():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado fornecido"}), 400

    return jsonify({"recebido": dados}), 201

@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = [
        {"id": 1, "nome": "Marina"},
        {"id": 3, "nome": "Pedro"},
        {"id": 2, "nome": "João"},
        {"id": 5, "nome" : "Júlia"}

    ]
    return jsonify({
        "status": "sucesso",
        "usuarios": usuarios
    }), 200



# 5. Bloco de execução
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)