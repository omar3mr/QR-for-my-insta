import qrcode
from PIL import Image  # لعرض الصورة

# إنشاء QR Code
qr = qrcode.make("Follow @r1rr1")

# حفظ الصورة
qr.save("my_qrcode.png")

# فتح الصورة وعرضها
img = Image.open("my_qrcode.png")
img.show()

print("QR Code generated, saved, and opened.")