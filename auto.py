import schedule
import time
import subprocess

# Path to the Python script you want to run
SCRIPT_PATH = r'D:\projects\Quizk\main.py'

def run_script():
    try:
        subprocess.run(['python', SCRIPT_PATH], check=True)
        print(f"Successfully ran {SCRIPT_PATH}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run {SCRIPT_PATH}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Schedule the task every 15 minutes
schedule.every(1).minutes.do(run_script)

while True:
    schedule.run_pending()
    time.sleep(1)
