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
			if len(titleMsg) == 0 and len(msg) == 0:
				raise RuntimeError('No summary specified.')

			if not isinstace(titleMsg, str) or not isinstace(msg, str):
				raise RuntimeError('Messages should be python strings.')

			self._title = titleMsg if titleMsg is not None or len(titleMsg) > 0 else ''
			self._msg= msg if msg is not None or len(msg) else ''
			self._iconpath = iconpath
			self._urgency_level_code = ulevel
			self._expiration_time = extime if extime is not None or extime > 0 else 1
			self._appname = appname if appname is not None or len(appname) > 0 else 'pynotify-send'

		def run(self):
			cmd = ['notify-send', '-t', str(self._expiration_time), '-a', self._appname]

			if valid_code(self._urgency_level_code):
				cmd += ['-u', code_as_str(self._urgency_level_code)]

			if self._iconpath is not None and os.path.exists(self._iconpath) and valid_img(self._iconpath):
				cmd += ['-i', self._iconpath]

			if len(self._title) > 0:
				cmd += [self._title]

			if len(self._msg) > 0:
				cmd += [self._msg]

			subprocess.call(cmd)

else:
	raise RuntimeError("please install notify-send")


if __name__ == '__main__':
	Noti("test title", "This is a test message").run()
	Noti("test title", "").run()
	Noti("", "This is a test message").run()
	Noti("", "").run()

