import os 
name = input('Input the name of the link: ')
if not name:
	name = 'random'
print(name)
os.system(f'ssh -R 80:127.0.0.1:8954 {name}@ssh.localhost.run')
