import requests
import json
url = 'http://127.0.0.1:5000/im_size'
my_img = {'image': open('static/uploads/download.jpg', 'rb')}
r = requests.post(url, files=my_img)

# convert server response into JSON format.
print(r.json()['Class'][0])