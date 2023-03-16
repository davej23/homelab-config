# Remove Nextcloud backups older than N days
# Backup folders are named `backup_YYYYMMDD`

import os
from datetime import datetime

BACKUP_PATH = '/mnt/storage/'  # Example
LOG_FILE = BACKUP_PATH + 'log.txt'  # Example
N_DAYS = 3

if not os.path.exists(LOG_FILE):
    os.system(f'touch {LOG_FILE}')

with open(LOG_FILE, 'a', encoding='utf-8') as f:
    f.write('\n')

for backup_folder in os.listdir(BACKUP_PATH):
    if os.path.isdir(BACKUP_PATH + backup_folder):

        backup_date_str = backup_folder.split('_')[-1]
        backup_date = datetime.strptime(backup_date_str, '%Y%m%d')

        todays_date = datetime.now()

        days_since_created = (todays_date - backup_date).days

        log_statement = f'Time {todays_date} - Folder {backup_folder} - Backup Date {backup_date} - Days since backup {days_since_created} days'
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_statement+'\n')

        print(log_statement)

        if days_since_created > N_DAYS:
            os.system(f'rm -r {BACKUP_PATH}{backup_folder}/*')
