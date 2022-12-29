"""
 Script: ftp_client.py
 By: Dharmender Singh (L00171202)
 Tested: Python v3.10.8; Windows 11
 Date: 2nd November, 2022
"""

import ftplib
import settings.ftp as settings

#make connection
ftp=ftplib.FTP(settings.FTP['URL'])
#anonymous login
ftp.login()
#change to correct directory
ftp.cwd(settings.FTP["PATH"])
#retrieve file
ftp.retrbinary("RETR"+settings.FTP["FILENAME"], open(settings.FTP["FILENAME"], 'wb').write)
ftp.quit()