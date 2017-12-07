from . import *
import os.path

__all__ = []

for i in range(24):
	fn = 'day{0}.py'.format(i+1)
	if os.path.isfile(fn):
		__all__.append(fn)