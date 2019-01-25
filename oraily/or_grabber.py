import json
import time
import random
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

ENDPOINT = "https://catchvideo.net/getvideo"
HEADERS = {'X-Requested-With': 'XMLHttpRequest'}

session = requests.Session()

retry = Retry(
    total=3,
    read=3,
    connect=3,
    backoff_factor=0.5,
    status_forcelist=(500, 502, 503, 504)
)
adapter = HTTPAdapter(max_retries=retry)

session.mount('http://', adapter)
session.mount('https://', adapter)

links = [
    # ("url", "filename.mp4"),
    ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video1_3", "video1_3.mp4"),
    ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video1_4", "video1_4.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video1_5", "video1_5.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video2_1", "video2_1.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video2_2", "video2_2.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video2_3", "video2_3.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video2_4", "video2_4.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video3_1", "video3_1.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video3_2", "video3_2.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video3_3", "video3_3.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video3_4", "video3_4.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video3_5", "video3_5.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video4_1", "video4_1.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video4_2", "video4_2.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video4_3", "video4_3.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video5_1", "video5_1.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video5_2", "video5_2.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video5_3", "video5_3.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video5_4", "video5_4.mp4"),
    # ("https://learning.oreilly.com/videos/python-digital-forensics/9781787126664/9781787126664-video5_5", "video5_5.mp4"),
]

with open('links.txt', 'w') as output_file:
    for url_data in links:
        origin_url = url_data[0]
        filename = url_data[1].replace(" ", "_")
        data = {"url": origin_url, "ap": False, "status": "start"}

        # response = requests.post(ENDPOINT, headers=HEADERS, data=data)
        response = session.post(ENDPOINT, headers=HEADERS, data=data)
        print('xxxx', response.text)
        response_data = json.loads(response.text)

        delay = random.choice([1.6, 1.2, 0.5, 2, 2.2])
        time.sleep(delay)

        try:
            dest_url = response_data["output"]["format"][0]["url"]
            dest_url = dest_url.replace("cdnapi", "cdnbakmi")
            dest_url = dest_url.replace("playManifest", "serveFlavor")
            dest_url = dest_url.replace("format/url/protocol/http", "")
            dest_url = dest_url.replace("//", "/")
            dest_url = dest_url.replace(":/", "://")
            # dest_url = dest_url.replace("format/url/protocol/http", "v/12")
            output_file.write(dest_url + "/name/" + filename + "\n")
            # output_file.write(origin_url + " " + dest_url + "/name/" + filename + "\n")
        except Exception as e:
            print(response.text)
            output_file.write("error: " + origin_url + "\n")
print('Finito!')
