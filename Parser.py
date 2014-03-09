from bs4 import BeautifulSoup

class Parser:
	def __init__(self):
		pass
	
	@staticmethod
	def parse_city_hotels_link_any_date(page):
		soup = BeautifulSoup(page)
		city_wrapper_div = soup.find('div', {'id':'cityWrapper'})
		if city_wrapper_div:
			booking_secondary_button_anchor = city_wrapper_div.find('a',{'class':'booking-secondary-button'})
			if booking_secondary_button_anchor and booking_secondary_button_anchor.has_key('href'):
				return booking_secondary_button_anchor['href']
			
	@staticmethod
	def parse_numof_records(page):
		soup = BeautifulSoup(page)
		records_count_div = soup.find('div',{'class':'sr_header'})
		if records_count_div:
			record_count_header = records_count_div.find('h1',{'class':'sorth1'})
			if record_count_header:
				record_count_text = record_count_header.text.trim()
				if record_count_text.startswith('0 properties'):
					return 0
				else:
					return 1
		return 0
	
	@staticmethod
	def parse_hotels_inpage(page):
		soup = BeautifulSoup(page)
		hotels_info_list = []
		item_container_divs = soup.findAll('div',{'class':'sr_item highlight_hover_hotel flash_deal_soldout'})
		for each_item_container in item_container_divs:
			each_item_content = each_item_container.find('div',{'class':'sr_item_content'})
			if each_item_content:
				sprite_icon_span = each_item_content.find('span',{'class':'jq_tooltip use_sprites icon_thumbyellow '})
				if sprite_icon_span:
					hotel_name_anchor = each_item_content.find('a',{'class':'hotel_name_link url'})
					if hotel_name_anchor:
						hotel_name = hotel_name_anchor.text.strip()
						hotel_link = hotel_name_anchor['href']
						hotel_id = each_item_content['data-hotelid']
						hotels_info_list.append({'hotel_name':hotel_name,'hotel_link':hotel_link,'hotel_id':hotel_id})
		return hotels_info_list
					
					
					
					
					
					
					
					
					
				