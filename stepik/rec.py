# Second
import requests

link = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('input.txt') as inf:
    t = inf.readline().strip()

t = str(requests.get(t).text)
while 'we' not in t:
    print(t)
    t = requests.get(link + t).text
print(t)