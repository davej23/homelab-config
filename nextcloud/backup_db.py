'''Nextcloud AIO PostgreSQL Backup Script
Author: @davej23
Date: 16-03-23
'''

# Create backup for PostgreSQL Nextcloud AIO database
# Get database credentials from `docker inspect nextcloud-aio-database`
# Create .pgpass file in `/var/lib/postgresql` folder within `nextcloud-aio-database` container
    # Inside this file, hostname:port:database:username:password
        # (e.g. nextcloud-aio-container:5432:nextcloud_database:USER:PASS)
    # chmod 600 ~/.pgpass
# Run pg_dump
# Check for outdated backups and delete them

import os
import json
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('backup_dir')
BACKUP_DIR = parser.parse_args().backup_dir

if BACKUP_DIR[-1] != '/':
    BACKUP_DIR += '/'

LOG_FILE = BACKUP_DIR + 'log-db.txt'  # Example
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

# Update log to start new entry
update_log('', LOG_FILE)
update_log(f'--- DATABASE BACKUP - {datetime.now()} ---', LOG_FILE)

# Enable Maintenance mode
os.system('docker exec --user www-data -it nextcloud-aio-nextcloud php occ maintenance:mode --on')
update_log('Maintenance mode enabled.', LOG_FILE)

# Get database credentials
db_inspect = json.loads(os.popen('docker inspect nextcloud-aio-database').read())
creds = db_inspect[0]['Config']['Env']
creds = dict(zip([n.split('=')[0] for n in creds], [n.split('=')[1] for n in creds]))

POSTGRES_PASSWORD = creds['POSTGRES_PASSWORD']
POSTGRES_DB = creds['POSTGRES_DB']
POSTGRES_USER = creds['POSTGRES_USER']

update_log('Credentials obtained.', LOG_FILE)

# Check pgpass exists, create if not
pgpass_check = os.popen('docker exec nextcloud-aio-database ls -a /var/lib/postgresql').read()

if '.pgpass' not in pgpass_check:
    # Create .pgpass file contents
    pgpass_contents = f'nextcloud-aio-database:5432:\
        {POSTGRES_DB}:{POSTGRES_USER}:{POSTGRES_PASSWORD}'

    # Write .pgpass file into `nextcloud-aio-database` container
    os.system(f'docker exec --user postgres \
            nextcloud-aio-database bash -c "echo {pgpass_contents}" >> /var/lib/postgresql/.pgpass')

    # Change permissions
    os.system('docker exec --user postgres \
        nextcloud-aio-database chmod 600 /var/lib/postgresql/.pgpass')

update_log('.pgpass file acquired.', LOG_FILE)

# Run `pg_dump` in `nextcloud-aio-database` container
os.system(f'docker exec \
    --user postgres \
    nextcloud-aio-database \
        pg_dump {POSTGRES_DB} -h nextcloud-aio-database -U {POSTGRES_USER} -w >> {BACKUP_DIR}latest_backup.sql')

update_log('pg_dump finished running.', LOG_FILE)

# Copy database dump to another location
os.system(f'mv {BACKUP_DIR}latest_backup.sql \
    {BACKUP_DIR}database-dump-`date +"%Y%m%d"`.sql')

update_log('Database dump has been moved to backup location.', LOG_FILE)

# Check no backups older than N days
for file in os.listdir(BACKUP_DIR):
    if 'database-dump' in file:
        backup_date_full_str = file.split('.')[0]
        backup_date_str = backup_date_full_str.split('-')[-1]
        backup_date = datetime.strptime(backup_date_str, '%Y%m%d')

        todays_date = datetime.now()

        days_since_created = (todays_date - backup_date).days

        log_statement = f'Time {todays_date} - File {file} - ' \
            f'Backup Date {backup_date} - Days since backup {days_since_created} days'

        update_log(log_statement, LOG_FILE)

        print(log_statement)

        if days_since_created > N_DAYS:
            os.system(f'rm {BACKUP_DIR}{file}')

# Disable Maintenance mode
os.system('docker exec --user www-data -it nextcloud-aio-nextcloud php occ maintenance:mode --off')
update_log('Maintenance mode disabled.', LOG_FILE)

update_log('Outdated backup check complete. \nBackup complete.', LOG_FILE)
