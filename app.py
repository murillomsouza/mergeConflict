from flask import Flask, jsonify, request

app = Flask(__name__)

#Padrao
@app.route('/')
def index():
    return "Essa é minha atualização para o conflito"

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

@app.route('/api/usuarios/buscar', methods=['GET'])
def buscar_usuario_por_nome():
    nome = request.args.get('nome')

    if not nome:
        return jsonify({"erro": "Informe o parametro 'nome' na URL"}), 400

    return jsonify({
        "status": "sucesso",
        "nome_buscado": nome,
        "mensagem": f"Buscando usuario com nome '{nome}'."
    }), 200

#Post ara enviar dados
@app.route('/api/dados', methods=['POST'])
def receber_dados():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado fornecido"}), 400

    return jsonify({"recebido": dados}), 201




# 5. Bloco de execução
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)