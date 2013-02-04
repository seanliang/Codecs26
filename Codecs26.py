import sublime
import os
import sys

if sublime.platform() == 'linux' and '3000' > sublime.version() > '2000':
	path = os.path.join(sublime.packages_path(), 'Codecs26', 'lib')
	if path not in sys.path:
		sys.path.append(path)
else:
	print('Warning: Codecs26 is working for Sublime Text 2 on linux only')
