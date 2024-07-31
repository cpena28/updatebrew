import subprocess
import os
import sys

# Get the directory of the current script (updatebrew.py)
script_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory of the script directory
parent_dir = os.path.dirname(script_dir)
# Add the 'utils' directory to the Python path
utils_dir = os.path.join(parent_dir, 'utils')
sys.path.append(utils_dir)

from interface import log_info, log_warn, input_yn, log_done, bcolors

log_info("Starting Homebrew update...")

# Execute 'brew update' and capture the output
update_output = subprocess.run(['brew', 'update'], capture_output=True, text=True).stdout

# Check if the output contains "Already up-to-date."
if "Already up-to-date." in update_output:
    log_done("Your Homebrew is already up-to-date. No updates available.")
else:
    log_info("Updates available. Proceeding with the upgrade and cleanup process.")

    log_info("Running: brew upgrade")
    subprocess.run(['brew', 'upgrade'])
    log_done("Package upgrade completed.")

    log_info("Running: brew cleanup")
    subprocess.run(['brew', 'cleanup'])
    log_done("Cleanup completed.")

    log_info("Running: brew autoremove")
    subprocess.run(['brew', 'autoremove'])
    log_done("Auto-removal of unneeded packages completed.")

log_done("All Homebrew processes have finished.")