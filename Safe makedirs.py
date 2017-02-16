# Safely creates directories even if they already exist

import os 

def safe_makedirs(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
