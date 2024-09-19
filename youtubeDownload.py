# yt_dlp_server.py
import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Usage: python yt_dlp_server.py <video-url>")
        sys.exit(1)

    video_url = sys.argv[1]
    server_ip = "10.0.0.4"  # Replace with your server's IP or domain
    username = "marceloserver"  # Replace with your server's username

    # command = f"ssh {username}@{server_ip} 'yt-dlp \"{video_url}\"'"

    output_path = "/home/marceloserver/Downloads/YoutubeVideos/%(title)s.%(ext)s"

    command = f"ssh {username}@{server_ip} 'source ~/.zprofile; yt-dlp -o \"{output_path}\" \"{video_url}\"'"

    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    main()
