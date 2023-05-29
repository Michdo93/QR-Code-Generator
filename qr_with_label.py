import qrcode
from PIL import Image, ImageDraw, ImageFont

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

    qr_image = qr.make_image(fill_color="black", back_color="white")
    # qr_image.save(filename)

    qr_size = qr_image.size

    # Create an empty image for the label
    label_image = Image.new("RGB", (qr_size[0], 20), color="white")

    # Add the text to the label
    draw = ImageDraw.Draw(label_image)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Path to the "DejaVu Sans" font
    font = ImageFont.truetype(font_path, 10)  # Customize the font style and size
    text_width, text_height = draw.textsize(data, font=font)
    text_x = (qr_size[0] - text_width) // 2
    text_y = (label_image.height - text_height) // 2
    draw.text((text_x, text_y), data, font=font, fill="black")

    # Create an image with QR code and label
    final_image = Image.new("RGB", (qr_size[0], qr_size[1] + label_image.height), color="white")
    final_image.paste(qr_image, (0, 0))
    final_image.paste(label_image, (0, qr_size[1]))

    # Save the final image
    final_image.save(filename)

# Example call of the function for creating and saving a QR code
create_qr_code("word1", "word1.png")
create_qr_code("word2", "word2.png")
