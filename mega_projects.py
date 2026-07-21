import qrcode
from PIL import Image, ImageDraw, ImageFont

# ===========================
# Settings
# ===========================
data = "https://your link here .com"   # Change this link 
name = "Linkdin"                            # Your name or initials

# ===========================
# Generate QR Code
# ===========================
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="pink").convert("RGB")

# ===========================
# Draw Name in Center
# ===========================
draw = ImageDraw.Draw(img)

width, height = img.size

# Size of named box
box_width = width // 3
box_height = height // 9

x1 = (width - box_width) // 2
y1 = (height - box_height) // 2
x2 = x1 + box_width
y2 = y1 + box_height

# Draw named rounded rectangle
draw.rounded_rectangle(
    (x1, y1, x2, y2),
    radius=20,
    fill="pink",
)

# Load font
try:
    
    font = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 25)
except:
    font = ImageFont.load_default()

# Calculate text size
bbox = draw.textbbox((0,0), name, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

#center text
text_x = (width - text_width) // 2
text_y = (height - text_height) // 2

draw.text((text_x, text_y), name, fill="green", font=font)

img.save("custom_qr.png")

print("QR Code saved as custom_qr.png")
