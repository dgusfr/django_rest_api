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

if __name__ == "__main__":
    new_item = {"name": "Item Teste"}
    create_item(new_item)

    get_all_items()
