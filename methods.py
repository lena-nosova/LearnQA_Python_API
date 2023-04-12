import requests
url='https://playground.learnqa.ru/ajax/api/compare_query_type'
request_types = ["GET", "POST", "PUT", "DELETE"]

#1.Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
#  Был отправлен get-запрос, в результате выведено: Wrong method provided

response1 = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response1.text)

#2.Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
#Был отправлен head-запрос, в ответе - пустой результутат

response2 = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response2.text)

#3.Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
#Отравлен post-запрос с методом post -  в ответе - {"success":"!"}

response3 = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": "POST"})
print(response3.text)

#4.С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
for type in request_types:
    for params in request_types:
        if request_types == "GET":
            response = requests.request(method=type, url=url, params={"method": params})
        else:
            response = requests.request(method=type, url=url, data={"method": params})

        if type == params and response.text != '{"success":"!"}':
                print(f"При методе {type} и параметре {params} ошибка: должно быть success, а возвращается:"
                  f" {response.text}")
        elif type != params and response.text == '{"success":"!"}':
                print(f"При методе {type} и параметре {params} ошибка: должно быть Wrong method provided, а а возвращается:"
                  f" {response.text}")