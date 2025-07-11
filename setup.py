import sys
import subprocess
import os
import platform
import shutil
import logging

try:
    from rich.console import Console
    import requests
except ImportError:
    print("Required libraries (rich, requests) not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich", "requests"])
    from rich.console import Console
    import requests

import datetime  # Added missing import

# Initialize rich console for styled output
console = Console()

# Required Python version
MIN_PYTHON = (3, 6)

def check_python_version():
    if sys.version_info < MIN_PYTHON:
        console.print("[red]Error: Python 3.6 or higher is required. Current version: {}.{}.{}[/red]".format(
            sys.version_info.major, sys.version_info.minor, sys.version_info.micro))
        sys.exit(1)
    console.print("[green]Python version check passed: {}.{}.{}[/green]".format(
        sys.version_info.major, sys.version_info.minor, sys.version_info.micro))

def install_dependencies():
    required_libs = ["requests", "rich", "cryptography"]
    try:
        for lib in required_libs:
            console.print(f"[yellow]Installing {lib}...[/yellow]")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
        console.print("[green]All dependencies installed successfully![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Failed to install dependencies: {e}[/red]")
        sys.exit(1)

def check_terminal_compatibility():
    term = os.environ.get("TERM", "unknown")
    is_ansi_supported = term.lower() in ["xterm", "xterm-256color", "linux", "screen", "tmux", "cmd", "powershell"]
    platform_name = platform.system().lower()

    console.print(f"[cyan]Terminal Details:[/cyan]")
    console.print(f"  - Terminal Type: {term}")
    console.print(f"  - Platform: {platform_name}")

    if is_ansi_supported and platform_name in ["windows", "linux", "android"]:
        console.print("[green]Terminal is ANSI-compatible. Script should work fine.[/green]")
    else:
        console.print("[yellow]Warning: Terminal may not fully support ANSI codes. Styling might not work as expected. Recommend using Windows Terminal or a similar ANSI-compatible terminal.[/yellow]")

def setup_logging():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "setup_log.log")
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f"Setup process started at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST")
    console.print("[green]Logging setup completed. Log file: logs/setup_log.log[/green]")

def main():
    console.print("[bold cyan]Setting up InstaRepPro.py...[/bold cyan]")
    
    # Check Python version
    check_python_version()
    
    # Setup logging
    setup_logging()
    
    # Install dependencies
    install_dependencies()
    
    # Check terminal compatibility
    check_terminal_compatibility()
    
    # Additional feature: Create a sample config file
    config_content = "Support us by following on insta, join all chanels in bio !"
    with open("readme.txt", "w") as f:
        f.write(config_content)
    console.print("[green]readme.txt created.[/green]")
    
    # Additional feature: Verify internet connectivity
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            console.print("[green]Internet connectivity confirmed.[/green]")
        else:
            console.print("[yellow]Warning: Internet connectivity issue detected. Some features may not work.[/yellow]")
    except requests.RequestException:
        console.print("[red]Error: No internet connection. Please connect to the internet and rerun setup.[/red]")
        sys.exit(1)
    
    console.print("[bold green]Setup completed successfully! You can now run InstaRepPro.py.[/bold green]")
    
    # Cleanup: Move setup.py to backup
    setup_file = os.path.abspath(__file__)
    try:
        backup_file = setup_file + ".bak"
        shutil.move(setup_file, backup_file)
        console.print("[yellow]setup.py moved to setup.py.bak for safety. Delete manually if desired.[/yellow]")
    except Exception as e:
        console.print(f"[yellow]Failed to move setup.py: {e}. Please delete manually.[/yellow]")

if __name__ == "__main__":
    main()