# Remove Nextcloud backups older than N days

import os
import time

BACKUP_PATH = '/mnt/storage/'  # Example
LOG_FILE = '/mnt/storage/log.txt'  # Example
N_DAYS = 3

if not os.path.exists(LOG_FILE):
    os.system(f'touch {LOG_FILE}')

with open(LOG_FILE, 'a', encoding='utf-8') as f:
    f.write('\n')

for backup_folder in os.listdir(BACKUP_PATH):
    if os.path.isdir(BACKUP_PATH + backup_folder):
        backup_stats = os.stat(BACKUP_PATH + backup_folder)
        modified_time = backup_stats.st_mtime

        time_since_modified_in_seconds = (time.time() - modified_time) / 1000.0
        time_since_modified_in_days = time_since_modified_in_seconds / (60 * 60 * 24)

        log_statement = f'Folder {backup_folder} - MT {modified_time} - TSC {time_since_modified_in_days} days'
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_statement)

        print(log_statement)

        if time_since_modified_in_days > N_DAYS:
            os.system(f'rm -r {BACKUP_PATH}{backup_folder}/*')
