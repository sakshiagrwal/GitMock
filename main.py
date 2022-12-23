import json
import random
from datetime import datetime, timedelta
from git import Repo

FILE_PATH = './data.json'

repo = Repo('./')

for i in range(20):
    x = random.randint(0, 54)
    y = random.randint(0, 6)
    date = (datetime.now() - timedelta(days=365)) + \
        timedelta(days=1 + x * 7 + y)
    data = {
        'date': date.strftime('%Y-%m-%d')
    }
    print(date.strftime('%Y-%m-%d'))
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f)
    repo.git.add([FILE_PATH])
    repo.git.commit('-m', date.strftime('%Y-%m-%d'), '--date',
                    date.strftime('%Y-%m-%d %H:%M:%S'))

repo.git.push()
