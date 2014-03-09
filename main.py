#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib
import urllib2
from google.appengine.api import urlfetch
from Reader import *
from Parser import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        url = Reader.read_search_url_any_date("Dhaka")
        response = urlfetch.fetch('http://www.booking.com/searchresults.en-us.html?sid=04194cf6440a1bebe2771d743bf4add0;dcid=1;class_interval=1;csflt=%7B%7D;dtdisc=0;hyb_red=0;idf=1;inac=0;nha_red=0;no_rooms=1;offset=0;property_room_info=1;redirected_from_city=0;redirected_from_landmark=0;redirected_from_region=0;review_score_group=empty;score_min=0;si=ai%2Cco%2Cci%2Cre%2Cdi;src=index;ss_all=0;;city=-755070;origin=disamb;srhash=2552117110;srpos=1', deadline=60)
        #response = urllib2.urlopen('www.booking.com/searchresults.html?src=index&nflt=&ss_raw=&error_url=http%3A%2F%2Fwww.booking.com%2Findex.en-us.html%3Fsid%3D04194cf6440a1bebe2771d743bf4add0%3Bdcid%3D1%3B&dcid=1&sid=04194cf6440a1bebe2771d743bf4add0&si=ai%2Cco%2Cci%2Cre%2Cdi&ss=Istanbul&checkin_monthday=0&checkin_year_month=0&checkout_monthday=0&checkout_year_month=0&idf=on&interval_of_time=any&sb_predefined_group_options_value=2&no_rooms=1&group_adults=2&group_children=0')
        page = response.content
        hotels_link = Parser.parse_city_hotels_link_any_date(page)
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
