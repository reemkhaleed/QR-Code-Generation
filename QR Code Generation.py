import qrcode
from PIL import Image

def main():
    
    github_url = "https://github.com/reemkhaleed?tab=repositories"

    
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(github_url)
    qr.make(fit=True)

    
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')


    logo_path = "GitHub.png" 
    logo = Image.open(logo_path)

    qr_width, qr_height = qr_img.size
    logo_size = int(qr_width * 0.2)
    logo = logo.resize((logo_size, logo_size))

    
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

   
    qr_img.save("My_Github.png")
    print("QR code with GitHub logo saved as 'My_Github.png'")

if __name__ == "__main__":
    main()
