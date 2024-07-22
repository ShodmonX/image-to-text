import requests


def imagetotext():
    api_url = 'https://api.api-ninjas.com/v1/imagetotext'
    image_file_descriptor = open('image.png', 'rb')
    files = {'image': image_file_descriptor}
    r = requests.post(api_url, files=files).json()
    text = ""


    for i in r:
        text += i["text"] 
        text += " "


    return text