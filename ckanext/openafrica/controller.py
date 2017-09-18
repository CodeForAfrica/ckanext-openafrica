# encoding: utf-8

# Copyright (c) 2015-2017 Code for Africa

# This file is part of CKAN openAfrica Extension.

# CKAN openAFRICA Extension is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# CKAN openAFRICA Extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with CKAN openAFRICA Extension. If not, see <http://www.gnu.org/licenses/>.

from ckan.lib.base import render

from ckan.controllers.home import HomeController


class CustomPageController(HomeController):
	"""This controller is used to extend some of the static pages with
	the accompanying URL routing associated with it."""
	def toc(self):
		return render('home/about/toc.html')
	def accessibility(self):
		return render('home/about/accessibility.html')
	def coc(self):
		return render('home/about/coc.html')
	def moderation(self):
		return render('home/about/moderation.html')
	def faq(self):
		return render('home/about/faq.html')
	def privacy(self):
		return render('home/about/privacy.html')
	def contact(self):
		return render('home/about/contact.html')
