'''

MODULES

=> pip install qrcode   (or)
=> pip install qrcode==7.3.1
=> pip install qrcode[pil]

'''


import qrcode
qr = qrcode.make("Please follow My instagram")
# data = "https://www.instagram.com/_sravan_s__?igsh=dG9jM2F5a3pldG15"
data = "https://www.instagram.com/urs_nans?igsh=MW5ydTNsMHZlMWdjNg=="
qr = qrcode.make(data)
qr.save("docpy.png") 
qr.show() 

# https://www.instagram.com/_sravan_s__?igsh=dG9jM2F5a3pldG15


'''

import qrcode
qr = qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name = input("Enter your name:")
age = int(input("Enter your age:"))
email = input("Enter your email:")
mobile = int(input("Enter your mobile:"))
data = {"Name":name, "Age":age, "Email":email, "Mobile":mobile}
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image()
img.save("mydetails_in_qr.png")
img.show()

'''