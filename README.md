

# InstaRepPro Tool Setup and Usage Guide

## Overview
InstaRepPro is a Python-based tool designed to perform specific tasks (as defined in `InstaRepPro.py`). This README provides instructions for setting up and running the tool.

## Folder Contents
- `SourceKey.key`: Key file required for the tool's operation.
- `SourceCode.bin`: Binary file containing essential code for the tool.
- `InstaRepPro.py`: Main script to run the tool.
- `setup.py`: Setup script to configure the environment.
- `readme.txt`: Auto-generated sample configuration file (created during setup).

## Prerequisites
- **Python Version**: Python 3.6 or higher is required.
- **Operating System**: Compatible with Windows, Linux, or Android.
- **Terminal**: An ANSI-compatible terminal (e.g., Windows Terminal, xterm, or tmux) is recommended for proper styling.
- **Internet Connection**: Required for installing dependencies and verifying connectivity.

## Setup Instructions
1. **Run the Setup Script**:
   - Execute `setup.py` to prepare the environment:
     ```bash
     python setup.py
     ```
   - This script will:
     - Check for Python 3.6 or higher.
     - Install required dependencies (`requests`, `rich`, `cryptography`).
     - Set up logging in the `logs/` directory (`logs/setup_log.log`).
     - Verify terminal compatibility and internet connectivity.
     - Create a sample `readme.txt` file with a default message.
     - Move `setup.py` to `setup.py.bak` for safety.

2. **Verify Setup**:
   - Ensure the `logs/setup_log.log` file is created and contains setup details.
   - Check that `readme.txt` is generated in the project directory.
   - Confirm all dependencies are installed by running:
     ```bash
     pip list
     ```
     Look for `requests`, `rich`, and `cryptography` in the output.

## Running the Tool
1. After successful setup, launch the main script:
   ```bash
   python InstaRepPro.py
   ```
2. Follow any on-screen prompts provided by `InstaRepPro.py` to use the tool.

## Troubleshooting
- **Python Version Error**: If you see an error about Python version, ensure Python 3.6 or higher is installed. Download it from [python.org](https://www.python.org/downloads/).
- **Dependency Installation Failure**: Ensure you have an active internet connection and run `setup.py` again.
- **Terminal Styling Issues**: If text styling (colors, bold) doesn't display correctly, use an ANSI-compatible terminal like Windows Terminal.
- **No Internet Connection**: The tool requires internet access for some features. Check your connection and rerun `setup.py`.

## Logs
- All setup activities are logged in `logs/setup_log.log` with timestamps for debugging purposes.

## Notes
- The `setup.py.bak` file is a backup of the setup script. You can delete it manually if no longer needed.
- Support the developers by following their Instagram and joining channels listed in their bio (see `readme.txt` for details).

