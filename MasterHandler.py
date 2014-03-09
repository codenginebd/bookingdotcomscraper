from Parser import *
from Reader import *

url_all_hotels_first_part = 'http://www.booking.com/searchresults.en-us.html?sid=04194cf6440a1bebe2771d743bf4add0;dcid=1;class_interval=1;csflt=%7B%7D;dest_id=-755070;dest_type=city;dtdisc=0;hyb_red=0;idf=1;inac=0;nha_red=0;no_rooms=1;property_room_info=1;redirected_from_city=0;redirected_from_landmark=0;redirected_from_region=0;review_score_group=empty;score_min=0;si=ai%2Cco%2Cci%2Cre%2Cdi;src=index;ss='
url_all_hotels_second_part = ';ss_all=0;ssb=empty;or_radius=0;rows=20;offset='

whole_url = url_all_hotels_first_part+'Dhaka'+url_all_hotels_second_part+str(0)

destination_list = [
					'Istanbul',
					'New York'
				]

class MasterHandler:
	def __init__(self):
		pass
	def do_initialization(self):
		for each_destination in destination_list:
			page_count = 0
			while True:
				###Form the url.
				url_full = url_all_hotels_first_part+each_destination+url_all_hotels_second_part+str(page_count)
				###Fetch data
				response = urlfetch.fetch(url_full, deadline=60)
				page = response.content
				if Parser.parse_numof_records(page) == 0:
					break
				
				
				page_count += 20
			
	