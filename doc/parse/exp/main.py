import NaturalAPI.parse #或者from Natrual import parse | or `from Natrual import parse`

ini = NaturalAPI.parse.json('config/main.json').start()
print(ini['ver']+","+ini['author'])
