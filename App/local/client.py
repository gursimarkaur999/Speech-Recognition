import requests

# server url
URL = "http://127.0.0.1/predict"


# audio file we'd like to send for predicting keyword
TEST_AUDIO_FILE_PATH = "input/down/4cb874bb_nohash_1.wav"


if __name__ == "__main__":
    print("hello")
    audio_file = open(TEST_AUDIO_FILE_PATH, "rb")
    print("hellp")
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
    values = {"file": (TEST_AUDIO_FILE_PATH, audio_file, "audio/wav")}
    print("3")
    response = requests.post(URL, files=values, headers=headers)
    print("4")
    print(response)
    data = response.json()

    print(f"Predicted keyword is: {data['keyword']}")
