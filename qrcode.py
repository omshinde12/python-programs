import pyqrcode
import png
from pyqrcode import QRCode
s="D:/shinde/photo/IMG_20210905_204327_224 (1).jpg"
url=pyqrcode.create(s)

url.png('my.png',scale=6)
