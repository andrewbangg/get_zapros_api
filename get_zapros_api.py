import requests

nums = []

def num():
    n = input()
    if n != '':
        nums.append(n)
        return num()

num()
api_url = 'http://numbersapi.com/'
for i in nums:
    res = requests.get(api_url + i + '/math?json=true')
    getok = res.json()
    if getok['found'] == True:
        print('Interesting')
    else:
        print('Boring')
