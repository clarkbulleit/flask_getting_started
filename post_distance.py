import requests

if __name__ == "__main__":

    distance = {
        "a": [2, 4],
        "b": [5, 6],
    }

    # r2 = requests.post("http://127.0.0.1:5000/distance", json=distance)
    r2 = requests.post("http://vcm-7335.vm.duke.edu:5000/distance", json=distance)
    dist = r2.json()
    print(dist)
