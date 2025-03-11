file = open('youtube.txt','w')

try:
    file.write('Hello Aman !')
except:
    print('An error occurred')
finally:
    file.close()
    print('File closed')

with open('youtube.txt','w') as file:
    file.write('Hello Aman !')
    print('File closed')