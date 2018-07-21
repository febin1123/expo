#file_handling.py
#modes:r-read,w-write,a-append
f=open('test1',r)
print(f.read())
print(f.readline())
print(f.readlines())
for line in f.readlines():
	print(line)
f.close()	
#writing		
f=open('test1',a)	
f.write('a line')
f.write(['aline2','line3','etc.......'])
f.close()
#appending