import datetime
name = input('What is your name\n ')
age = int(input('How old are you?\n'))
now = datetime.datetime.now()
diff = 100 - age
print('Hello', name, now.year+diff)
