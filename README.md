# Automate_ROLE
This simple script automates attendance process in ROLE/MOODLE.

steps:
1) Create "ROLE_USERNAME" and "ROLE_PASSWORD" environment variables in environment variables with their values as your moodle/ROLE username and password respectively. -> https://www.youtube.com/watch?v=Frrlv_5rGhY
2) Restart Your Computer.
3) install python -> https://www.youtube.com/watch?v=UvcQlPZ8ecA
4) create virtual environment -> https://www.youtube.com/watch?v=APOPm01BVrk
5) install requirements using this command "pip install -r requirements.txt" in terminal.
6) run "python ROLE.py" in your terminal in morning before 10:00AM and don't close it. Leave the terminal running and after 5:00PM you can close it.
7) Repeat step 5 every day and always remember that this script will check for attendance events in ROLE between 10:00AM - 5:00PM, not outside these hours.
8) if facing any error regarding chromedriver then install according to your chrome version. -> https://chromedriver.chromium.org/downloads
9) If you want to remove the hassle of running this script daily then you can schedule this script with windows task schedular or crontab.
