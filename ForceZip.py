#ForceZip created by Alex Moica

import itertools
import zipfile
import os
import zlib

dp = os.path.join(os.path.dirname(__file__),'')

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
	fileName = input("Name of zip file: ")
	if '.zip' not in fileName:
		fileName = dp+(fileName + '.zip')
	if zipfile.is_zipfile(fileName):
		break
	else:
		print(fileName,"is not a valid zip file.\n")

print("\nFiles in", fileName + ":", '\n')
zf = zipfile.ZipFile(fileName,'r')

i=0
for val in zf.namelist():
	i=i+1
	print('[',i,']', val)
	
while True:
	while True:
		try:
			index = int(input("\nFile number to extract: "))
			break
		except ValueError as e:
			print(e)
			
	subFile=''
	v=0
	for val in zf.namelist():
		v=v+1
		if v == index:
			subFile = val
			break
			
	if subFile in zf.namelist():
		break
	else:
		print("Invalid file index:",index)
	
while True:
	for i in itertools.count():
		tries = itertools.product(chars, repeat=i)
		for current in tries:
			print(''.join(current))
			b = bytes(''.join(current), 'utf-8')
			try:
				zf.extract(subFile, (os.path.join(os.path.expanduser('~'), 'Desktop')), b)
				print("\nPassword cracked! Password is: ", ''.join(current))
				print(subFile, "extracted successfully to Desktop.")
				input("Press Enter to continue...")
				exit()
			except RuntimeError as e:
				pass					
			except zlib.error:
				pass
			except zipfile.BadZipFile:
				pass