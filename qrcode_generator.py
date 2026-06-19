import qrcode

data = input("Enter a text or URL: ").strip()
file_name = input("Enter a file name: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(f"{file_name}.png")

print(f"QR Code saved as {file_name}.png")