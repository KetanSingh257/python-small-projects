

import qrcode  

url = input("enter your url : ")
filename = input("filename want to save it as =")
if not (filename.endswith(".png")):             
    filename += ".png"


img = qrcode.make(url)         
img.save(filename)

print("QR saves succesfully")