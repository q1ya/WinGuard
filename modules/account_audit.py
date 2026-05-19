import subprocess
from core.ui import log_info, log_success, log_warning, log_alert

def check_guest_account():
    log_info("Checking Guest Account Status...")
    try:
        out = subprocess.check_output('net user guest', shell=True, text=True, stderr=subprocess.DEVNULL)
        if "Account active               Yes" in out:
            log_alert("Guest account is ACTIVE! This violates standard baselines.")
        else:
            log_success("Guest account is properly disabled.")
    except Exception:
        log_warning("Could not query Guest account (Requires Administrator privileges).")

def check_password_policy():
    log_info("Checking Global Password Policy...")
    try:
        out = subprocess.check_output('net accounts', shell=True, text=True)
        
        # 检查密码最小长度策略
        if "Minimum password length" in out:
            for line in out.splitlines():
                if "Minimum password length" in line:
                    length = int(line.split()[-1])
                    if length < 8:
                        log_alert(f"Password length too short: {length} (Baseline: >= 8)")
                    else:
                        log_success(f"Minimum password length is compliant ({length}).")
    except Exception:
        log_warning("Failed to query password policies.")

def run_checks():
    check_guest_account()
    check_password_policy()