import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def get_pexels_photos(photo_category):
    headers = {"Authorization": "563492ad6f91700001000001723b6a32d0eb450690f61b3f2fa9e746"}
    response = requests.get("https://api.pexels.com/v1/search?query={}&per_page=12".format(photo_category), headers=headers)
    if response.status_code == 200:
        return response.json()["photos"]       
    else:
        raise Exception(f"Error: {response.status_code}")

def get_image_urls(photo_category):
    image_urls = get_pexels_photos(photo_category)
    loiu = []
    for i in range(0, 12):
        a = image_urls[i]["src"]["tiny"]
        loiu.append(a)
    return loiu   


@app.route("/", methods=["GET", "POST"])

def index():
    image_urls = None
    if request.method == "POST":
        photo_category = request.form["photo_category"]
        image_urls = get_image_urls(photo_category)
    return render_template('index.html', image_urls=image_urls)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
