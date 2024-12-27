import requests

# URL base
url_base = "http://127.0.0.1:5000/postos"

# 1. Listar postos
response = requests.get(url_base)
print("Listar Postos:", response.json())

# 2. Obter um posto específico
response = requests.get(f"{url_base}/1")
print("Obter Posto 1:", response.json())

# 3. Criar um novo posto
novo_posto = {
    "nome": "Posto D",
    "preco": {"gasolina": 6.10, "etanol": 4.65}
}
response = requests.post(url_base, json=novo_posto)
print("Criar Posto D:", response.json())

# 4. Atualizar um posto
posto_atualizado = {
    "nome": "Posto A Atualizado",
    "preco": {"gasolina": 5.90, "etanol": 4.45}
}
response = requests.put(f"{url_base}/1", json=posto_atualizado)
print("Atualizar Posto 1:", response.json())

# 5. Deletar um posto
response = requests.delete(f"{url_base}/1")
print("Deletar Posto 1:", response.json())
