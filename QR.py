import qrcode
from PIL import Image 


qr = qrcode.make("Follow @r1rr1")


qr.save("my_qrcode.png")


img = Image.open("my_qrcode.png")
img.show()

print("QR Code generated, saved, and opened.")
