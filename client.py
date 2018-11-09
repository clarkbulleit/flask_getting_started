import requests

if __name__ == "__main__":

    distance = {
        "a": [2, 4],
        "b": [5, 6],
    }

    r1 = requests.get("http://127.0.0.1:5001/name")
    r2 = requests.get("http://127.0.0.1:5001/hello/Clark")
    r3 = requests.post("http://127.0.0.1:5001/distance", json=distance)

    # r2 = requests.post("http://vcm-7335.vm.duke.edu:5000/distance", json=distance)
    name = r1
    Clark = r2.json()
    distance = r3.json()

    print(name)
    print(Clark)
    print(distance)
