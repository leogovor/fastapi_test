import requests

def get_json_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок
        return response.json()  # Возвращаем JSON
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Ошибка HTTP
    except Exception as err:
        print(f'Other error occurred: {err}')  # Остальные ошибки

def extract_data_by_key(json_data, key):
    return json_data.get(key, 'Ключ не найден')  # Извлечение данных по ключу

# Пример использования
url = 'https://api.example.com/data.json'
data = get_json_from_url(url)

if data:
    # Извлекаем данные по нужному ключу
    key = 'desired_key'  # Замените на ваш ключ
    extracted_data = extract_data_by_key(data, key)
    print(extracted_data)