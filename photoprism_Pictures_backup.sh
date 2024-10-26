#!/usr/bin/env zsh

source ~/.zshrc
# Load environment variables from .env file
export $(grep -v '^#' .env | xargs)

# Define paths
BACKUP_DIR=~/Pictures  # Create a directory for backups

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

S3_DB_BACKUP_DIR="$S3_BUCKET/pictures/backups"


nohup aws s3 sync $BACKUP_DIR $S3_DB_BACKUP_DIR --exact-timestamps --storage-class GLACIER &> backup.log &

# Log success message
echo "Backup process started in background. Check backup.log for details."
