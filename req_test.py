import requests

BASE_URL = "http://127.0.0.1:8000/" 

def get_all_items():
    response = requests.get(f"{BASE_URL}")
    print("GET all items:", response.status_code)
    try:
        items = response.json()
        print("Items:", items)
    except requests.exceptions.JSONDecodeError:
        print("Resposta não contém JSON ou ocorreu um erro.")

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
    new_item = {"name": "Item Teste"}
    create_item(new_item)

    get_all_items()

    updated_data_partial = {"name": "Item Teste Atualizado"}
    update_item(1, updated_data_partial, partial=True)

    updated_data_full = {"name": "Item Teste Atualizado Completo"}
    update_item(1, updated_data_full, partial=False)

    delete_item(1)

    get_all_items()
