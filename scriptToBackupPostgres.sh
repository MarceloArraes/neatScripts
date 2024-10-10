#!/bin/bash

# Backup PostgreSQL
pg_dump -U <db_user> -h <db_host> -d <db_name> -F c -b -v -f /path/to/backup/outline_backup_$(date +\%F).sql

# Backup File Storage
aws s3 sync s3://your-bucket-name /path/to/local/backup/s3-backup_$(date +\%F)

# Backup Redis
# redis-cli SAVE
# cp /path/to/redis/dump.rdb /path/to/backup/redis_backup_$(date +\%F).rdb

# Optional: Compress everything into a single file
tar -czvf /path/to/backup/full_backup_$(date +\%F).tar.gz /path/to/backup/*

# 1. Edit the Crontab
# Run the following command to edit the crontab file, which is where you can schedule tasks for your user:

# bash
# Copy code
# crontab -e
# This will open the cron configuration in your default text editor.

# 2. Add the Cron Job
# To schedule your script to run every night at 2 AM, add the following line to the crontab file:

# bash
# Copy code
# 0 2 * * * /path/to/backup-script.sh >> /path/to/backup-log.log 2>&1