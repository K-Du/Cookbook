# Needs to be entered before importing xgboost

import os
mingw_path = r'C:\Program Files\mingw-w64\x86_64-6.2.0-posix-seh-rt_v5-rev1'
os.environ['PATH'] = mingw_path + ';' + os.environ['PATH']
