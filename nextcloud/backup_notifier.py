'''Nextcloud Backup Email Notification
Author: @davej23
Date: 16-03-23
'''

# Simple email notifier (using Gmail) for Nextcloud backup status
# App PW handling is not great but is functional

import os
import json
from enum import Enum
from typing import List
from datetime import datetime
from email.message import EmailMessage
import argparse
import smtplib
import ssl

parser = argparse.ArgumentParser()
parser.add_argument('--backup_dir')
parser.add_argument('--email')
parser.add_argument('--app_pw')

args = parser.parse_args()

BACKUP_DIR_PARENT = args.backup_dir
EMAIL = args.email
APP_PW = args.app_pw

ABSOLUTE_TIME = datetime.now()
DATE = datetime.strftime(ABSOLUTE_TIME, "%Y%m%d")
DATA_BACKUP_DIR = f'{BACKUP_DIR_PARENT}/backup_{DATE}'
DB_BACKUP_FILE = f'{BACKUP_DIR_PARENT}/database-dump-{DATE}.sql'

class Status(Enum):
    SUCCESSFUL = 'Successful'
    FAILED = 'Failed'
    UNKNOWN = 'Unknown'


class ReportItem:
    def __init__(self, path: str):
        self.path = path
        self.status = Status.UNKNOWN

    def __repr__(self):
        return '{' + f'"path": "{self.path}", "status": "{self.status.value}"' + '}'


class StatusReport:
    def __init__(self, date: datetime):
        self.date = date
        self.report_items: List[ReportItem] = []

    def add_locations(self, backup_dirs: List[str]):
        for backup_dir in backup_dirs:
            self.report_items.append(ReportItem(backup_dir))

    def check_folder_existence(self, report_item: ReportItem) -> ReportItem:
        if not os.path.exists(report_item.path):
            report_item.status = Status.FAILED
        else:
            report_item.status = Status.SUCCESSFUL

        return report_item

    def update_status(self):
        for report_item in self.report_items:
            report_item = self.check_folder_existence(report_item)

    def __repr__(self):
        return json.dumps({'date': str(self.date), 'report_items': json.loads(str(self.report_items))})


# Create report and check status of backups
status_report = StatusReport(date=ABSOLUTE_TIME)
status_report.add_locations([DATA_BACKUP_DIR, DB_BACKUP_FILE])
status_report.update_status()

# Send email
msg = EmailMessage()
msg['Subject'] = f'Nextcloud Backup Status Report {DATE}'
msg['From'] = EMAIL
msg['To'] = EMAIL
msg.set_content(json.dumps(json.loads(str(status_report)), indent=4))

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as server:
    server.login(EMAIL, APP_PW)
    server.send_message(msg)
