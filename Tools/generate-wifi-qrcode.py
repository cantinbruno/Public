import qrcode
import os

ssid = input("Entrez le SSID du réseau Wi-Fi : ")
password = input("Entrez le mot de passe du réseau Wi-Fi : ")

security = "WPA"
wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(wifi_data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")
current_path = os.getcwd()
file_path = os.path.join(current_path, "WIFI.png")
qr_img.save(file_path)

print("Le QR code pour se connecter au réseau Wi-Fi a été généré avec succès.")
print(f"Le QR code est enregistré à l'emplacement : {file_path}")
input("\nAppuyez sur Entrée pour terminer le script.")
