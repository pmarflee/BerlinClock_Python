class SecondsLine(object):

	def __init__(self, seconds):
		self.__seconds = seconds

	def __str__(self):
		return 'Y' if self.__seconds % 2 == 0 else 'O'

class OneMinuteLine(object):

	def __init__(self, minutes):
		self.__minutes = minutes

	def __str__(self):
		return ('Y' * (self.__minutes % 5)).ljust(4, 'O')

class FiveMinuteLine(object):

	def __init__(self, minutes):
		self.__minutes = minutes

	def __getlight(self, minutes):
		if minutes > self.__minutes:
			return 'O'
		elif minutes % 15 == 0:
			return 'R'
		else:
		        return 'Y'			

	def __str__(self):
		return ''.join([self.__getlight(mins) for mins in range(5, 60, 5)])

class OneHourLine(object):

	def __init__(self, hours):
	    self.__hours = hours

	def __str__(self):
		return ('R' * (self.__hours % 5)).ljust(4, 'O')

class FiveHourLine(object):

	def __init__(self, hours):
		self.__hours = hours

	def __str__(self):
		return ''.join(['R' if self.__hours >= hours else 'O' for hours in [5, 10, 15, 20]])

class BerlinClock(object):

	def __init__(self, time):
		segments = time.split(':')
		self.__hours = int(segments[0])
		self.__minutes = int(segments[1])
		self.__seconds = int(segments[2])

	def __str__(self):
		lines =	[ SecondsLine(self.__seconds),
			  FiveHourLine(self.__hours),
			  OneHourLine(self.__hours),
			  FiveMinuteLine(self.__minutes),
			  OneMinuteLine(self.__minutes) ]
		return '\r\n'.join([str(line) for line in lines])
			    