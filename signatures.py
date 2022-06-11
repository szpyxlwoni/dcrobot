import glob
import codecs

savedFile = codecs.open('./signature', 'w', 'utf-8')
tempStr = ''

for fileName in glob.glob("./signatures/*"):
	try:
	    f = codecs.open(fileName, 'r', 'utf-8')
	except IOError:
		f.close()
	else:
		tempStr = ''.join([tempStr, fileName, '=', f.read(), '\n'])
		f.close()

savedFile.write(tempStr)
savedFile.close()