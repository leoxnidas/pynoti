import os
import subprocess


def _check():
	output = subprocess.check_output(['which', 'notify-send'])
	if len(output) == 0:
		return False
	return True


if _check():

	LOW = 1
	NORMAL = 2
	CRITICAL = 3

	def valid_img(i):
		return True if i.endswith('.png') or i.endswith('.jpg') or i.endswith('.jpeg') else False

	def valid_code(code):
		return True if code in (LOW, NORMAL, CRITICAL) else False

	def code_as_str(code):
		if code == LOW:
			return 'low'
		elif code == NORMAL:
			return 'normal'
		elif code == CRITICAL:
			return 'critical'
		return ''

	class Noti(object):

		def __init__(self, titleMsg, msg, ulevel=LOW, extime=1, iconpath=None, appname='pynotify-send'):
			self._title = titleMsg if titleMsg is not None else ''
			self._msg= msg if msg is not None else ''
			self._iconpath = iconpath
			self._urgency_level_code = ulevel
			self._expiration_time = extime if extime is not None or extime > 0 else 1
			self._appname = appname if appname is not None or len(appname) > 0 else 'pynotify-send'

		def run(self):
			cmd = ['notify-send', self._title, self._msg, '-t', str(self._expiration_time), '-a', self._appname]

			if valid_code(self._urgency_level_code):
				cmd += ['-u', code_as_str(self._urgency_level_code)]

			if self._iconpath is not None and os.path.exists(self._iconpath) and valid_img(self._iconpath):
				cmd += ['-i', self._iconpath]

			subprocess.call(cmd)

else:
	print("please install notify-send")


if __name__ == '__main__':
	Noti("test title", "This is a test message").run()

