import easyocr
import cv2
import numpy as np
import requests
from sys import getsizeof

def requestImage(url):
    resp = requests.get(url, stream=True).raw
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))
    print(type(image), round(getsizeof(image)/1024/1024,2))
    return image

def callreader(lang, image):
    my_ocr = easyocr.Reader([lang,'en'], gpu=True)
    record = my_ocr.readtext(image, detail=0)
    for i, e in enumerate(record):
        print(i, e)
    return my_ocr

def main(lang="ch_tra"):
    url = str(input())
    image = requestImage(url)
    reader = callreader(lang, image)

if __name__ == "__main__":
    main("ch_tra")