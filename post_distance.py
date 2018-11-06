import requests

if __name__ == "__main__":

    distance = {
        "a": [2, 4],
        "b": [5, 6],
    }

    r2 = requests.post("127.0.0.1:5000/distance", json=distance)
    Clark_Info = r2.json()