__author__ = 'srlaxminaarayanan'

import requests
import base64
import json
import io
import codecs

class ClassifyImages:
    def __init__(self):
        self.accesstokenUrl = 'https://api.clarifai.com/v1/token/'
        self.tagUrl='https://api.clarifai.com/v1/tag/'

    def _url(self,path):
        return 'http://localhost:5000' + path

    def classify_image(self,image):
        return self.send_image(image)

    def acquire_accesstoken(self):
        data ={}
        data["client_id"]="EsYuml4p15UAGzDQw7-v4GFDlaPpbcDJqNhDvns1"
        data["client_secret"]="vETGZR7XNF0v78ztIfKPuWBDDm3mEeRfTkYloKYC"
        data["grant_type"] ="client_credentials"
        return requests.post(self.accesstokenUrl,data)

    def send_image(self, image):
        accesstoken = self.acquire_accesstoken()
        accesstokendata=json.loads((accesstoken.content.decode("utf-8")))['access_token']
        jpeg_image_buffer = io.BytesIO()
        image.save(jpeg_image_buffer, format="JPEG")
        imgStr = base64.b64encode(jpeg_image_buffer.getvalue())
        payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"model\"\r\n\r\ngeneral-v1.3\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"encoded_data\"\r\n\r\n"+imgStr.decode()+"\r\n-----011000010111000001101001--"
        headers = {
                   'content-type': "multipart/form-data; boundary=---011000010111000001101001",
                   'authorization': "Bearer " + accesstokendata
        }

        try:
            result = requests.post(self.tagUrl,data=payload,headers=headers)
            results = json.loads((result.content.decode("utf-8")))
            if result is not None:
                return results['results'][0]['result']['tag']['classes']
        except requests.exceptions.Timeout:
            print("Timed Out")
        except requests.exceptions.TooManyRedirects:
            print("Please use another URl. The present one has toomany redirects")
            return None
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        except Exception as e:
            print(e)
            return None