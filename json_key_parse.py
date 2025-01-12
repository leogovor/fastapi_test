import requests
import this

url = 'https://jsonplaceholder.typicode.com/todos'


def get_json_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок
        return response.json()  # Возвращаем JSON
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Ошибка HTTP
    except Exception as err:
        print(f'Other error occurred: {err}')  # Остальные
def extract_data_by_key(json_data, key):
    return json_data.get(key, 'Ключ не найден')

data = get_json_from_url(url)
print(data)
if data:
    key = 'n'
    extracted_data = extract_data_by_key(data, key)
    print(extracted_data)
