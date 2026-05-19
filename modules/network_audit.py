import subprocess
from core.ui import log_info, log_success, log_alert, log_warning

def check_firewall():
    log_info("Auditing Windows Defender Firewall Profiles...")
    try:
        out = subprocess.check_output('netsh advfirewall show allprofiles state', shell=True, text=True)
        if "OFF" in out.upper():
            log_alert("CRITICAL: One or more Firewall profiles are DISABLED!")
        else:
            log_success("All Windows Firewall profiles are ACTIVE.")
    except Exception:
        log_warning("Failed to read Firewall status.")

def check_smb():
    log_info("Checking SMBv1 Status...")
    try:
        cmd = 'reg query "HKLM\\SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters" /v SMB1'
        out = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL)
        if "0x1" in out:
            log_alert("SMBv1 is ENABLED! High risk for Ransomware (e.g., WannaCry).")
        else:
            log_success("SMBv1 is explicitly disabled via registry.")
    except Exception:
        log_success("SMBv1 registry key not found (Default on modern Windows is disabled).")

def run_checks():
    check_firewall()
    check_smb()