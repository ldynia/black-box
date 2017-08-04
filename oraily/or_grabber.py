import json
import requests

ENDPOINT = "http://catchvideo.net/getvideo".
HEADERS = {'X-Requested-With': 'XMLHttpRequest'}

# https://www.safaribooksonline.com/learning-paths/learning-path-decision-making/9781491995457/
# https://www.safaribooksonline.com/learning-paths/learning-path-team/9781491994399/
# https://www.safaribooksonline.com/learning-paths/learning-path-meeting/9781491994450/
# https://www.safaribooksonline.com/learning-paths/learning-path-leadership/9781491994412/
# https://www.safaribooksonline.com/learning-paths/learning-path-refactoring/9781491995495/
# https://www.safaribooksonline.com/learning-paths/learning-path-cloud/9781491984475/

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
