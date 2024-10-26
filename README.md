# neatScripts

## to run the ansible script to setup zshell do this

`ansible-playbook install-ohmyzsh.yml --ask-become-pass`

## docker deluge

`https://github.com/linuxserver/docker-deluge`

## jellyfin

`https://jellyfin.org/docs/general/installation/container/`
`https://github.com/jellyfin/jellyfin`

## useful comands

`xclip -selection clipboard < file.txt`

- To copy files from my pc to server:
  `rsync -avz --progress takeout-20241023T004732Z-001.zip marceloserver@10.0.0.4:/home/marceloserver/Pictures`
  `scp -r takeout-20241023T004732Z-001.zip  marceloserver@10.0.0.4:/home/marceloserver/Pictures`
- To see the progress of a file being changed (like a log)
  `tail -f backup.log`
- To download videos from youtube:
  - `yt-dlp https://www.youtube.com/watch\?v\=Rvw6gMfs0yk`
- To download videos and make it on audio mp3 and naming toasty.mp3:
  - `yt-dlp -o toasty.mp3 -x https://www.youtube.com/watch\?v\=Rvw6gMfs0yk --audio-format mp3`

## things I installed

- Tool to manipulate audio and video:

  - `sudo apt install ffmpeg`

- Tool to copy text to the clipboard with the terminal:
  - `sudo apt install xclip`
-

## transfering files from local to

## Some things/commands i have being using often on my server journey

Docker commands:
See images: docker images
See containers(the objects of images): docker ps
To see all, even the stopped ones: docker ps -a

Generate ssh:
`ssh-keygen -t rsa -b 4096`

To copy ssh to server to not need to enter password each time:
`ssh-copy-id marceloserver@10.0.0.4`

To use Docker compose (instead of Docker run … )
Inside a folder with the compose.yaml file with the docker configs, run:
docker compose up

To start my twingate client on my computer:
twingate start

Allow new ports to go through the ubuntu firewall:

`sudo ufw allow 13378/tcp`

See then:
`sudo ufw status`

Configuring Postgres for connection to Nextcloud:
<https://hub.docker.com/_/postgres/>
`sudo ufw s`
`ssh-keygen -t rsa -b 4096`
`docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

Creating the database:
`postgres=# CREATE USER nextcloud WITH PASSWORD '**\*\***';`
`CREATE DATABASE nextclouddb TEMPLATE template0 ENCODING 'UNICODE';`
`ALTER DATABASE nextclouddb OWNER TO nextcloud;`
`GRANT ALL PRIVILEGES ON DATABASE nextclouddb TO nextcloud;`

How to copy files from outside to inside my server:
`sudo scp -r "/home/marcelo/Downloads/" marceloserver@10.0.0.4:/home/yourusername/audiobooks`

How to change the reboot mode of docker container:
`docker update --restart='always' 9b93de560f83`

Things I did to schedule times for my server to be up and running:
`sudo crontab -e`

## Shutdown every day at midnight

`0 0 \* \* \* /sbin/shutdown -h now`

## Special Tuesday shutdown at 10 PM

- Here, 0 0* \* \_represents midnight every day, and 0 22* \* 2 represents 10 PM on Tuesdays.
  `0 22 \* _2 /sbin/shutdown -h now`

`sudo nano /etc/systemd/system/reboot.service`
Add the following content:
ini
Copy code
[Unit]
Description=Reboot the system

[Service]
Type=oneshot
ExecStart=/sbin/reboot

Save and exit.

Create Timer Unit Files for Regular and Special Days
Regular Day Timer: This timer will handle the startup at 17:30 for days other than Tuesday.
bash
Copy code

sudo nano /etc/systemd/system/reboot-regular.timer
Add the following content:
ini
Copy code

[Unit]
Description=Timer to reboot the system on regular days

[Timer]
OnCalendar=_-_-\* 17:30:00
Unit=reboot.service

[Install]
WantedBy=timers.target
Save and exit.
Tuesday Timer: This timer will handle the special Tuesday startup at 16:00.
bash
Copy code
sudo nano /etc/systemd/system/reboot-tuesday.timer
Add the following content:
ini
Copy code
[Unit]
Description=Timer to reboot the system on Tuesdays

[Timer]
OnCalendar=Tue _-_-\* 16:00:00
Unit=reboot.service

[Install]
WantedBy=timers.target
Save and exit.
Reload Systemd and Enable Timers
Reload systemd to recognize the new unit files and start the timers:
bash
Copy code
sudo systemctl daemon-reload
sudo systemctl enable reboot-regular.timer
sudo systemctl enable reboot-tuesday.timer
sudo systemctl start reboot-regular.timer
sudo systemctl start reboot-tuesday.timer

## To remember

- I should put depends on the docker compose file, so that the containers start only when the other previous necessary docker containers are up and running.
