import requests
import time

result = 'result'
status = 'status'

response_1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsed_response_text_1 = response_1.json()
print(parsed_response_text_1)
token_1 = parsed_response_text_1["token"]
response_2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token_1})
print(response_2.text)
if (response_2.text) != '{"status":"Job is NOT ready"}':
    print('Job is ready')
else:
    time.sleep(parsed_response_text_1["seconds"] + 1)
response_3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token_1})
parsed_response_text_3 = response_3.json()
if result in parsed_response_text_3 and parsed_response_text_3['status'] == 'Job is ready':
    print(f"Найден {result}, {status} - 'Job is ready': " + response_3.text)
else:
    print(f"Ошибка! Не найдены {result} и {status}")

