import requests

def track_package(tracking_number):
    url = f"https://api.17track.net/track?nums={tracking_number}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if data["dat"][0]["track"]:
            for event in data["dat"][0]["track"]:
                print(event["checkpoint"], event["checkpoint_time"])
        else:
            print("Нет информации о посылке")
    else:
        print("Ошибка при запросе отслеживания")

# Пример использования:
tracking_number = input("Введите номер отслеживания посылки: ")
track_package(tracking_number)
