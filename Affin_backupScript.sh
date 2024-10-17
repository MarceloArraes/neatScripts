#!/usr/bin/env zsh

source ~/.zshrc
# Load environment variables from .env file
export $(grep -v '^#' .env | xargs)

# Define paths
CONFIG_DIR=~/.affine/self-host/config
STORAGE_DIR=~/.affine/self-host/storage
POSTGRES_DIR=~/.affine/self-host/postgres
BACKUP_DIR=~/.affine/self-host/backups  # Create a directory for backups

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Define the name of the backup file
DB_BACKUP_FILE="$BACKUP_DIR/affine_backup_$(date +%Y%m%d_%H%M%S).sql"

# Backup the PostgreSQL database
pg_dump -U affine -h localhost -p 5434 -W affine  -d affine -F c -f $DB_BACKUP_FILE

# Define S3 paths using environment variable
#S3_CONFIG_DIR="$S3_BUCKET/affine/config"
#S3_STORAGE_DIR="$S3_BUCKET/affine/storage"
#S3_POSTGRES_DIR="$S3_BUCKET/affine/postgres"
S3_DB_BACKUP_DIR="$S3_BUCKET/affine/backups"

# Sync the directories to S3
#aws s3 sync $CONFIG_DIR $S3_CONFIG_DIR
#aws s3 sync $STORAGE_DIR $S3_STORAGE_DIR
#aws s3 sync $POSTGRES_DIR $S3_POSTGRES_DIR
#aws s3 cp $DB_BACKUP_FILE $S3_DB_BACKUP_DIR  # Upload the database backup to S3
aws s3 sync $BACKUP_DIR $S3_DB_BACKUP_DIR

# Log success message
echo "Backup completed to S3"
