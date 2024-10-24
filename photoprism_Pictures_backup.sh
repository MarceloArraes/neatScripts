#!/usr/bin/env zsh

source ~/.zshrc
# Load environment variables from .env file
export $(grep -v '^#' .env | xargs)

# Define paths
BACKUP_DIR=~/Pictures  # Create a directory for backups

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

S3_DB_BACKUP_DIR="$S3_BUCKET/pictures/backups"


aws s3 sync $BACKUP_DIR $S3_DB_BACKUP_DIR --storage-class GLACIER
# delete ensures that if i delete on the Pictures will be deleted on S3. Don't want that for now.
# aws s3 sync $BACKUP_DIR $S3_DB_BACKUP_DIR --delete --exact-timestamps

# Log success message
echo "Backup completed to S3"