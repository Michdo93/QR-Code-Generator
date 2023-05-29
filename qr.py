import qrcode

# Function to create a QR code and save it as an image file
def create_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)

    
    
# Example call of the function for creating and saving a QR code
create_qr_code("word1", "word1.png")
create_qr_code("word2", "word2.png")
