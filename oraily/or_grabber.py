import json
import requests

ENDPOINT = "http://catchvideo.net/getvideo"
HEADERS = {'X-Requested-With': 'XMLHttpRequest'}

links = [
    # ("url", "filename.mp4"),
]

with open('links.txt', 'w') as output_file:
    for url_data in links:
        origin_url = url_data[0]
        filename = url_data[1].replace(" ", "_")
        print(origin_url)

        data = {"url": origin_url, "ap": False, "status": "start"}
        response = requests.post(ENDPOINT, headers=HEADERS, data=data)
        response_data = json.loads(response.text)
        try:
            dest_url = response_data["output"]["format"][0]["url"]
            dest_url = dest_url.replace("cdnapi", "cdnbakmi")
            dest_url = dest_url.replace("playManifest", "serveFlavor")
            dest_url = dest_url.replace("format/url/protocol/http", "v/2")
            output_file.write(origin_url + " " + dest_url + "/name/" + filename + "\n")
        except Exception as e:
            print(response.text)
            output_file.write("error: " + origin_url + "\n")

print('Finito!')
