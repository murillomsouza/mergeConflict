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
        "status": "sucesso",
        "mensagem": "A API está rodando perfeitamente!"
    })

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