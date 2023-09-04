import qrcode
def qr_code_generator(id_name):
    qr_image=qrcode.make(id_name)
    qr_image.save("barcode.jpg")