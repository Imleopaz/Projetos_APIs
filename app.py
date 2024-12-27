from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados simulados (em um banco de dados real, os dados viriam de um DB)
postos = [
    {"id": 1, "nome": "Posto A", "preco": {"gasolina": 5.99, "etanol": 4.49}},
    {"id": 2, "nome": "Posto B", "preco": {"gasolina": 6.05, "etanol": 4.55}},
]

@app.route('/postos', methods=['GET'])
def listar_postos():
    return jsonify(postos), 200

@app.route('/postos/<int:id>', methods=['GET'])
def obter_posto(id):
    posto = next((p for p in postos if p['id'] == id), None)
    if posto:
        return jsonify(posto), 200
    return jsonify({"message": "Posto não encontrado"}), 404

@app.route('/postos', methods=['POST'])
def criar_posto():
    data = request.get_json()
    novo_posto = {
        "id": len(postos) + 1,
        "nome": data['nome'],
        "preco": data['preco']
    }
    postos.append(novo_posto)
    return jsonify(novo_posto), 201

@app.route('/postos/<int:id>', methods=['PUT'])
def atualizar_posto(id):
    data = request.get_json()
    posto = next((p for p in postos if p['id'] == id), None)
    if posto:
        posto['nome'] = data['nome']
        posto['preco'] = data['preco']
        return jsonify(posto), 200
    return jsonify({"message": "Posto não encontrado"}), 404

@app.route('/postos/<int:id>', methods=['DELETE'])
def deletar_posto(id):
    posto = next((p for p in postos if p['id'] == id), None)
    if posto:
        postos.remove(posto)
        return jsonify({"message": "Posto deletado com sucesso"}), 200
    return jsonify({"message": "Posto não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
