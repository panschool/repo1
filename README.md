Crontab dokumentation:

➜  ~ crontab -l
0 3 * * * python3 /Users/pan/PycharmProjects/Test/backup_of_files.py

This cronjob is set to run at 3:00 AM, everyday of every month

Here you should change </Users/pan/PycharmProjects/Test/> to whatever folder you put the python script in.

setup via:
https://crontab.guru/#0_3_*_*_*
