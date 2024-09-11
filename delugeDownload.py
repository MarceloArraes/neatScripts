import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Configuration
deluge_url = "http://10.0.0.4:8112/json"
username = os.getenv('DELUGE_USERNAME')
password = os.getenv('DELUGE_PASSWORD')
#torrent_url = "magnet:?xt=urn:btih:F4007F11ACE3D5A7883747B7C81FEF870666BCCD&dn=Mythic.Quest.Ravens.Banquet.S01.COMPLETE.720p.ATVP.WEBRip.x264-G&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2F47.ip-51-68-199.eu%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2780%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2730%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce" 
#The URL of the torrent file
torrent_url = input("Please paste the magnet link: ")

# Step 1: Login to Deluge and get session ID
login_payload = {
    "method": "auth.login",
    "params": [password],
    "id": 1
}
session = requests.Session()
response = session.post(deluge_url, json=login_payload)
if response.status_code == 200 and response.json().get("result"):
    print("Login successful")
else:
    print("Login failed")
    exit(1)

# Step 2: Add the URL to Deluge for downloading
add_torrent_payload = {
    "method": "web.add_torrents",
    "params": [[
        {"path": torrent_url, "options": {}}
    ]],
    "id": 2
}
response = session.post(deluge_url, json=add_torrent_payload)
if response.status_code == 200 and response.json().get("result"):
    print("Torrent added successfully")
else:
    print("Failed to add torrent")
    print(response.text)
