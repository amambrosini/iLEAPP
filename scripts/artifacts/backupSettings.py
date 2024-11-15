__artifacts_v2__ = {
    "backupSettings": {
        "name": "Backup Settings",
        "description": "Extracts Backup settings",
        "author": "@AlexisBrignoni",
        "version": "0.2",
        "date": "2023-10-04",
        "requirements": "none",
        "category": "Identifiers",
        "notes": "",
        "paths": ('*/mobile/Library/Preferences/com.apple.mobile.ldbackup.plist',),
        "output_types": ["html", "tsv", "lava"]
    }
}

import plistlib
from scripts.ilapfuncs import artifact_processor, device_info, webkit_timestampsconv

@artifact_processor
def backupSettings(files_found, report_folder, seeker, wrap_text, timezone_offset):
    data_list = []
    source_path = str(files_found[0])
    
    with open(source_path, "rb") as fp:
        pl = plistlib.load(fp)
        for key, val in pl.items():
            if key == 'LastiTunesBackupDate':
                lastime = webkit_timestampsconv(val)
                data_list.append(('Last iTunes Backup Date', lastime))
                device_info("Backup Settings", "Last iTunes Backup Date", lastime, source_path)
            elif key == 'LastiTunesBackupTZ':
                data_list.append((key, val))
                device_info("Backup Settings", "Last iTunes Backup TZ", val, source_path)
            elif key == 'LastCloudBackupDate':
                lastcloudtime = webkit_timestampsconv(val)
                data_list.append(('Last Cloud iTunes Backup Date', lastcloudtime))
                device_info("Backup Settings", "Last Cloud iTunes Backup Date", lastcloudtime, source_path)
            elif key == 'LastCloudBackupTZ':
                data_list.append((key, val))
                device_info("Backup Settings", "Last Cloud iTunes Backup TZ", val, source_path)
            elif key == 'CloudBackupEnabled':
                data_list.append((key,val))
                device_info("Backup Settings", "Cloud Backup Enabled", val, source_path)
            else:
                data_list.append((key, val ))
                
    data_headers = ('Property', 'Property Value')
    return data_headers, data_list, source_path            
