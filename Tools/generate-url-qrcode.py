import qrcode
import os

url = input("Entrez l'URL que vous souhaitez encoder dans le QR code : ")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")
current_path = os.getcwd()
file_path = os.path.join(current_path, "URL_QRCode.png")
qr_img.save(file_path)

print("Le QR code contenant l'URL a été généré avec succès.")
print(f"Le QR code est enregistré à l'emplacement : {file_path}")
input("\nAppuyez sur Entrée pour terminer le script.")
