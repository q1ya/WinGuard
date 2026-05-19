import os
import time
import sys
from core.ui import print_banner, log_info, Colors
from modules import system_audit, account_audit, network_audit

def is_admin():
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    if not is_admin():
        print(f"{Colors.YELLOW}[!] WARNING: Not running as Administrator. Some checks will fail or yield incomplete results.{Colors.RESET}\n")
    
    time.sleep(1)
    
    print(f"{Colors.MAGENTA}===================[ 1. SYSTEM CONFIGURATION ]==================={Colors.RESET}")
    system_audit.run_checks()
    time.sleep(0.5)
    
    print(f"\n{Colors.MAGENTA}===================[ 2. IDENTITY & ACCOUNTS ]===================={Colors.RESET}")
    account_audit.run_checks()
    time.sleep(0.5)
    
    print(f"\n{Colors.MAGENTA}===================[ 3. NETWORK & FIREWALL ]====================={Colors.RESET}")
    network_audit.run_checks()
    time.sleep(0.5)
    
    print(f"\n{Colors.CYAN}[*] Security Baseline Audit Completed.{Colors.RESET}\n")

if __name__ == "__main__":
    if sys.version_info < (3, 6):
        print("This script requires Python 3.6 or higher.")
        sys.exit(1)
    main()