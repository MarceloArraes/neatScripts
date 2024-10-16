# example using dbeaver to connect to localhost postgresql database

I have dbeaver on my machine and I want to connect it to the docker running a local postgres instance:
06e315a0656b postgres:latest "docker-entrypoint.s…" 2 weeks ago Up 7 hours 0.0.0.0:5432->5432/tcp, :::5432->5432/tcp rocket2024agosto-db-1

This is the info on this postgres:

```.env
WSRS_DATABASE_PORT=5432
WSRS_DATABASE_USER="postgres"
WSRS_DATABASE_PASSWORD="123456789"
WSRS_DATABASE_NAME="websocket"
WSRS_DATABASE_HOST="db"
```

ChatGPT said:

To connect DBeaver to your local Postgres instance running in Docker, follow these steps:

Open DBeaver and click on the "New Database Connection" button (or go to Database > New Database Connection).

In the Select database dialog, choose PostgreSQL.

Fill in the connection details:

Host: Since the Docker container is forwarding ports to your local machine, use localhost.
Port: 5432 (as defined by WSRS_DATABASE_PORT).
Database: websocket (as defined by WSRS_DATABASE_NAME).
Username: postgres (as defined by WSRS_DATABASE_USER).
Password: 123456789 (as defined by WSRS_DATABASE_PASSWORD).
Click Test Connection to verify the connection works.
