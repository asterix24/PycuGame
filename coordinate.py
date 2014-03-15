#!/usr/bin/env python

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# 
# Copyright 2014 Daniele Basile <asterix24@gmail.com>
#                Francesca Basile <hidefix92@gmail.com>
# 
# \author Daniele Basile <asterix24@gmail.com>
# \author Francesca Basile <hidefix92@gmail.com>
#


class Pos(object):
	def __init__(self, x, y):
		self._x = x
		self._y = y
	
	def x(self):
		return self._x

	def y(self):
		return self._y

	def set(self,x,y):
		self._x = x
		self._y = y

	def get(self):
		return [self._x, self._y]

	def add_x(self, x):
		self._x += x

	def add_y(self, y):
		self._y += y

	def add(self, pos):
		self._x += pos.x
		self._y += pos.y
	
	def minus(self, pos):
		self._x -= pos.x
		self._y -= pos.y

	def __str__(self):
		return "(%s,%s)" % (self._x, self._y)
