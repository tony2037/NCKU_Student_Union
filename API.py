import cognitive_face as CF
import cv2

img = open("./Su.jpg",'rb')


KEY = "8b25b24d3a464d27ad8aa1b4ea84bb07"  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = "https://eastasia.api.cognitive.microsoft.com/face/v1.0"
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
faces = CF.face.detect(img)
print(faces)


"""
return :
[{u'faceId': u'68a0f8cf-9dba-4a25-afb3-f9cdf57cca51', u'faceRectangle': {u'width': 89, u'top': 66, u'height': 89, u'left': 446}}]
"""
