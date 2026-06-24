# File-Automatic-Backup-System-

## 📌 Overview

The  File Automatic Backup System is a Python-based application that automatically creates backups of important files and folders to prevent data loss. The system monitors specified directories, detects file changes, and generates backup copies with integrity verification using MD5 checksum validation. It helps ensure data security, reliability, and quick recovery of files when needed.

##  🚀Features
Automatic file and folder backup
Timestamp-based backup versioning
MD5 checksum verification for file integrity
Error handling and logging
Easy file recovery from backups
Cross-platform support

## 🛠️Technologies Used
Python
OS Module
Shutil Module
Hashlib (MD5 Checksum)
Datetime Module

## Project Structure
Automatic-Backup-System/
│
├── backup.py
├── source_files/
├── backups/
├── logs/
└── README.md

## How It Works
Select the source file or folder.
The system creates a backup in the backup directory.
A timestamp is added to each backup version.
MD5 checksum is generated for the original and backup files.
Checksums are compared to verify backup integrity.
Backup status is displayed and logged.

# Installation
git clone https://github.com/your-username/Automatic-Backup-System.git
cd Automatic-Backup-System

# Run the Project
python backup.py
Example Output
Backup Started...
Backup Created Successfully

Original File MD5:
a1b2c3d4e5f6...

Backup File MD5:
a1b2c3d4e5f6...

Integrity Check: PASSED

# Future Enhancements
Scheduled automatic backups
Cloud storage integration
Email notifications
Incremental backups
GUI using Tkinter or PyQt

# Resume Highlights
Developed a Python-based Automatic Backup System.
Implemented MD5 checksum validation for data integrity verification.
Automated file backup and recovery processes to reduce data loss risks.

# Author

Abhishek Dhaygude
