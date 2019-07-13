import re
from urllib.request import urlopen

with open('sitemap.txt') as sitemap:
    line = sitemap.readline()
    while line:
        with urlopen(line) as response:
            html = response.read().decode('utf-8')
            lst = re.findall(r"([a-fA-F\d]{33})", html)
            if lst:
                print('Here is the flag ' + lst[0])
                print(line)
                exit(0)
        line = sitemap.readline()
