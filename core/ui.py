import os

# 激活 Windows 的 ANSI 终端色彩转义支持
if os.name == 'nt':
    os.system("")

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'

def print_banner():
    banner = f"""{Colors.CYAN}
    __       __  _           ______                              __ 
   / /_  __ / / (_)____     / ____/ __  __ ____ _ _____ _____ / /_
  / | / / // / / // __ \\   / / __  / / / // __ `// ___// ___// __/
 / /|/ // / / / // / / /  / /_/ / / /_/ // /_/ // /   / /   / /_  
/_/ |_//_/ /_//_//_/ /_/   \\____/  \\__,_/ \\__,_//_/   /_/    \\__/ 
                                                                  
        [Windows Security Baseline Scanner v1.0 - By Weichun]
        [Target: Win10 / Win11 / WinServer] [Python 3.12+]
    {Colors.RESET}"""
    print(banner)

def log_info(msg):
    print(f"{Colors.CYAN}[*] {msg}{Colors.RESET}")

def log_warning(msg):
    print(f"{Colors.YELLOW}[!] {msg}{Colors.RESET}")

def log_alert(msg):
    print(f"{Colors.RED}[🚨] {msg}{Colors.RESET}")

def log_success(msg):
    print(f"{Colors.GREEN}[+] {msg}{Colors.RESET}")