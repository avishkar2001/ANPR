import requests
import cv2

d = {
    "region": None,
    "state": None,
    "numberplate": None,
    "time": None,
    "vehicle-of-building": None,
    "phone-number": None
}
regions = ["in"]

with open("n.png", "rb") as fp:
    print(fp)
    response = requests.post( 
        "https://api.platerecognizer.com/v1/plate-reader/",
        data=dict(regions=regions), 
        files=dict(upload=fp), 
        headers={"Authorization": "Token 1ac3c81851a6320238b59b06c4623b7325e29eee"}
    )
    print(response.json())