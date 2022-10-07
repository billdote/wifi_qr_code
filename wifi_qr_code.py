#!/usr/bin/python3
import wifi_qrcode_generator as wifi

wifi_network = input('Enter WIFI network: ')
wifi_password = input('Enter WIFI password: ')
auth_type = input('Enter authentication type (WPA, WEP, nopass): ')

if not wifi_password: wifi_password = None

if not auth_type.isupper() and auth_type in ['wpa', 'wep']:
    auth_type = auth_type.upper()

if not wifi_network:
    raise TypeError('WIFI network cannot be empty.')
else:
    # Generate WIFI QR code
    qrcode = wifi.wifi_qrcode(wifi_network, False, auth_type, wifi_password)

# Save QR code
qrcode.save("wifi.png")
