city_list = [
				'New York',
				'Paris',
				'London',
				'Amsterdam',
				'Paris',
				'Istanbul',
				'Rome',
				'Barcelona'
			]

class Reader:
	def __init__(self):
		pass
	@staticmethod
	def read_cities(self):
		return city_list
	@staticmethod
	def read_search_url_any_date(destination):
		url = """http://www.booking.com/searchresults.html?src=index&nflt=&ss_raw=&error_url=http%3A%2F%2Fwww.booking.com%2Findex.en-us.html%3Fsid%3D04194cf6440a1bebe2771d743bf4add0%3Bdcid%3D1%3B&dcid=1&
		sid=04194cf6440a1bebe2771d743bf4add0&si=ai%2Cco%2Cci%2Cre%2Cdi&ss="""+destination+"""&checkin_monthday=0&checkin_year_month=0&checkout_monthday=0&
		checkout_year_month=0&idf=on&interval_of_time=any&sb_predefined_group_options_value=2&no_rooms=1&group_adults=2&group_children=0"""
		return url
	