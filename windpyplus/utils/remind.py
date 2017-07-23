import sys
import time
import subprocess
import webbrowser

def _write_inprogress():
	sys.stdout.write("#")
	sys.stdout.flush()
def _write_msg(start_msg):
	sys.stdout.write(start_msg)
	sys.stdout.flush()
def _play_wav():
	print('\n')
	subprocess.Popen(['start', 'E:\\wav\\notify.wav'], shell = True)
	time.sleep(1)

def _openWeb(url):
	webbrowser.open(url)
	pass

if __name__ == '__main__':
	_write_msg('[getting start:]')
	for i in range(5):
		_write_inprogress()
		time.sleep(1)
	_play_wav()
	#url = 'https://i.bigquant.com/user/romepeng/lab?'
	#_openWeb(url)