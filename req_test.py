import requests

BASE_URL = "http://127.0.0.1:8000/"  # URL base da API

def get_all_items():
    response = requests.get(f"{BASE_URL}")
    print("GET all items:", response.status_code)
    try:
        items = response.json()
        print("Items:", items)
    except requests.exceptions.JSONDecodeError:
        print("Resposta não contém JSON ou ocorreu um erro.")
    return response.json() if response.status_code == 200 else []

def create_item(data):
    response = requests.post(f"{BASE_URL}add/", json=data)
    print("POST create item:", response.status_code)
    try:
        item = response.json()
        print("Item criado:", item)
    except requests.exceptions.JSONDecodeError:
        print("Resposta não contém JSON ou ocorreu um erro.")

def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}delete/{item_id}/")
    print(f"DELETE item {item_id}:", response.status_code)
    if response.status_code == 204:
        print(f"Item {item_id} deletado com sucesso.")
    elif response.status_code == 404:
        print(f"Item {item_id} não encontrado.")
    else:
        print("Erro ao deletar o item.")

def update_item(item_id, data, partial=True):
    method = "PATCH" if partial else "PUT"
    response = requests.request(method, f"{BASE_URL}update/{item_id}/", json=data)
    print(f"{method} update item {item_id}:", response.status_code)
    try:
        item = response.json()
        print("Item atualizado:", item)
    except requests.exceptions.JSONDecodeError:
        print("Resposta não contém JSON ou ocorreu um erro.")

if __name__ == "__main__":
    # Teste: criar um novo item
    new_item = {
        "name": "Produto Teste 3",
        "price": 29.99,
        "description": "Um produto de teste para o sistema de depósito.",
        "category": "Eletrodomésticos",
        "stock": 100
    }
    create_item(new_item)

    # Teste: listar todos os itens
    items = get_all_items()

    # Atualizar ou excluir um item existente, se encontrado
    if items:
        item_id = items[0]['id']
        # Teste: atualizar um item (parcialmente)
        updated_data_partial = {"stock": 80}
        update_item(item_id, updated_data_partial, partial=True)

        # Teste: atualizar um item (completo)
        updated_data_full = {
            "name": "Produto Teste Atualizado",
            "price": 24.99,
            "description": "Produto atualizado com nova descrição e preço.",
            "category": "Eletrônicos",
            "stock": 50
        }
        update_item(item_id, updated_data_full, partial=False)

        # Teste: deletar o item
        delete_item(item_id)
    else:
        print("Nenhum item encontrado para atualizar ou deletar.")

    # Teste: listar todos os itens novamente
    get_all_items()
