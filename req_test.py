import requests

BASE_URL = "http://127.0.0.1:8000/api/" 
def get_all_items():
    response = requests.get(f"{BASE_URL}items/")
    print("GET all items:", response.status_code)
    print(response.json())

def get_item(item_id):
    response = requests.get(f"{BASE_URL}items/{item_id}/")
    print(f"GET item {item_id}:", response.status_code)
    print(response.json())

def create_item(data):
    response = requests.post(f"{BASE_URL}items/", json=data)
    print("POST create item:", response.status_code)
    print(response.json())

def update_item(item_id, data):
    response = requests.put(f"{BASE_URL}items/{item_id}/", json=data)
    print(f"PUT update item {item_id}:", response.status_code)
    print(response.json())

def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}items/{item_id}/")
    print(f"DELETE item {item_id}:", response.status_code)

if __name__ == "__main__":
    get_all_items()

    new_item = {"name": "Item Teste", "description": "Descrição do item teste"}
    create_item(new_item)

    get_item(1)

    updated_item = {"name": "Item Teste Atualizado", "description": "Descrição atualizada"}
    update_item(1, updated_item)

    delete_item(1)
