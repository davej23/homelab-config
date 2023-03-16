'''Nextcloud AIO Outdated Backup Removal Script
Author: @davej23
Date: 16-03-23
'''

# Remove Nextcloud backups older than N days
# Backup folders are named `backup_YYYYMMDD`

import os
from datetime import datetime

BACKUP_PATH = '/mnt/backups/'  # Example
LOG_FILE = BACKUP_PATH + 'log.txt'  # Example
N_DAYS = 3

if not os.path.exists(LOG_FILE):
    os.system(f'touch {LOG_FILE}')

def update_log(message: str, log_file_path: str):
    '''Update log file
    message : str --> Message to log
    log_file_path : str --> Filepath for log file
    '''
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write('\n')
        log_file.write(message)

update_log('', LOG_FILE)

for backup_folder in os.listdir(BACKUP_PATH):
    if os.path.isdir(BACKUP_PATH + backup_folder):

        backup_date_str = backup_folder.split('_')[-1]
        backup_date = datetime.strptime(backup_date_str, '%Y%m%d')

        todays_date = datetime.now()

        days_since_created = (todays_date - backup_date).days

        log_statement = f'Time {todays_date} - Folder {backup_folder} - ' \
            f'Backup Date {backup_date} - Days since backup {days_since_created} days'

        update_log(log_statement, LOG_FILE)

        print(log_statement)

        if days_since_created > N_DAYS:
            os.system(f'rm -r {BACKUP_PATH}{backup_folder}/*')
