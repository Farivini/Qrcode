import pyqrcode

url = pyqrcode.create('https://www.linkedin.com/in/vinicius-farineli/')
url.svg('uca-url.svg', scale=8)
url.eps('uca-url.eps', scale=2)
print(url.terminal(quiet_zone=1))
