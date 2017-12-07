import requests
from .session import session

def getpuzzleinput(year, day):
    cookies = dict(session=session)
    r = requests.get('http://adventofcode.com/{0}/day/{1}/input'.format(year, day), cookies=cookies)
    r.raise_for_status()
    return r.text.strip()
