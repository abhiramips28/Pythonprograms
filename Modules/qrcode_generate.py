import pyqrcode
s = "Hi dears"
url = pyqrcode.create(s)
url.svg("myqrcode.svg",scale=8)

url.png("myqrcode.png",scale=6)