import unittest
from berlinclock import *

class Test_SecondsLine(unittest.TestCase):
	
	def test_should_return_Y_for_an_even_second(self):
		line = SecondsLine(2)
		self.assertEqual('Y', str(line))

	def test_should_return_O_for_an_odd_second(self):
		line = SecondsLine(1)
		self.assertEqual('O', str(line))

class Test_OneMinuteLine(unittest.TestCase):

	def test_should_return_YOOO_when_it_is_one_minute_past_the_hour(self):
		line = OneMinuteLine(1)
		self.assertEqual('YOOO', str(line))

	def test_should_return_YYOO_when_it_is_two_minutes_past_the_hour(self):
		line = OneMinuteLine(2)
		self.assertEqual('YYOO', str(line))

	def test_should_return_OOOO_when_it_is_five_minutes_past_the_hour(self):
		line = OneMinuteLine(5)
		self.assertEqual('OOOO', str(line))

class Test_FiveMinuteLine(unittest.TestCase):

	def test_should_return_YOOOOOOOOOO_when_it_is_five_minutes_past_the_hour(self):
		line = FiveMinuteLine(5)
		self.assertEqual('YOOOOOOOOOO', str(line))

	def test_should_return_YYROOOOOOOO_when_it_is_fifteen_minutes_past_the_hour(self):
		line = FiveMinuteLine(15)
		self.assertEqual('YYROOOOOOOO', str(line))

	def test_should_return_YYRYYRYYRYY_when_it_is_fiftyfive_minutes_past_the_hour(self):
		line = FiveMinuteLine(55)
		self.assertEqual('YYRYYRYYRYY', str(line))

class Test_OneHourLine(unittest.TestCase):

	def test_should_return_ROOO_when_it_is_one_hour_past(self):
		line = OneHourLine(1)
		self.assertEqual('ROOO', str(line))

	def test_should_return_RROO_when_it_is_two_hours_past(self):
		line = OneHourLine(2)
		self.assertEqual('RROO', str(line))

	def test_should_return_OOOO_when_it_is_five_hours_past(self):
		line = OneHourLine(5)
		self.assertEqual('OOOO', str(line))

class Test_FiveHourLine(unittest.TestCase):

	def test_should_return_ROOO_when_it_is_five_hours_past(self):
		line = FiveHourLine(5)
		self.assertEqual('ROOO', str(line))

	def test_should_return_RRRO_when_it_is_fifteen_hours_past(self):
		line = FiveHourLine(15)
		self.assertEqual('RRRO', str(line))

	def test_should_return_RRRR_when_it_is_twentythree_hours_past(self):
		line = FiveHourLine(23)
		self.assertEqual('RRRR', str(line))

class Test_BerlinClock(unittest.TestCase):

	def test_should_return_correct_time_for_165000(self):
		clock = BerlinClock('16:50:00')
		self.assertEqual('Y\r\nRRRO\r\nROOO\r\nYYRYYRYYRYO\r\nOOOO', str(clock))

if __name__ == '__main__':
	unittest.main()
