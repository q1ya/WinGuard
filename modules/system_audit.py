import platform
import subprocess
from core.ui import log_info, log_success, log_warning, log_alert

def check_os():
    log_info("Enumerating OS Information...")
    os_ver = platform.version()
    os_rel = platform.release()
    log_success(f"Detected OS: Windows {os_rel} (Build {os_ver})")

def check_rdp():
    log_info("Checking RDP Configuration...")
    try:
        # 检查 RDP 注册表
        cmd = 'reg query "HKLM\\System\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections'
        out = subprocess.check_output(cmd, shell=True, text=True)
        if "0x0" in out:
            log_alert("RDP is ENABLED (fDenyTSConnections = 0). Ensure this is intended.")
        else:
            log_success("RDP is DISABLED.")
    except Exception:
        log_warning("Failed to read RDP registry keys. Run as Administrator.")

def run_checks():
    check_os()
    check_rdp()