from deluge_client import DelugeRPCClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
deluge_host = "10.0.0.4"  # IP of the machine where Deluge daemon is running
deluge_port = 58846       # RPC port of the Deluge daemon (from your Docker config)
deluge_username = os.getenv('DELUGE_USERNAME')
deluge_password = os.getenv('DELUGE_PASSWORD')

# Ask for magnet link input
torrent_url = input("Please paste the magnet link: ")

# Step 1: Connect to the Deluge daemon
client = DelugeRPCClient(deluge_host, deluge_port, deluge_username, deluge_password)
try:
    client.connect()
    print("Connected to Deluge daemon")
except Exception as e:
    print(f"Failed to connect to Deluge daemon: {e}")
    exit(1)

# Step 2: Add the magnet link
try:
    client.call('core.add_torrent_magnet', torrent_url, {})
    print("Torrent added successfully")
except Exception as e:
    print(f"Failed to add torrent: {e}")
