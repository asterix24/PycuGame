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

import sys

import pygame
from pygame.locals import *

import cfg
from coordinate import *

class FontMgr(object):
	def __init__(self, surface):
		self.surface = surface
		self.curr_pos = None
		self.obj_to_animate = None

	def draw_text(self, text, color, position, size=18):
		self.font = pygame.font.Font(cfg.FONT, size)
		text = self.font.render(text, True, color)
		self.surface.blit(text, position)

		return self.surface

	def fall_text(self, text, color, start_pos, end_pos, size=18):
		self.font = pygame.font.Font(cfg.FONT, size)
		self.obj_to_animate = self.font.render(text, False, color)
		self.obj_to_animate_n = self.font.render(text, False, cfg.BLACK)

		self.start_pos = Pos(start_pos.x(), start_pos.y())
		self.curr_pos = Pos(start_pos.x(), start_pos.y())
		self.end_pos = end_pos

	def update(self, surface):
		if self.curr_pos is not None:
			if self.curr_pos.y() == self.end_pos.y():
				self.surface.blit(self.obj_to_animate_n, self.curr_pos.get())
				self.curr_pos = Pos(self.start_pos.x(), self.start_pos.y())
				return self.surface

			self.surface.blit(self.obj_to_animate_n, self.curr_pos.get())
			self.curr_pos.add_y(2)
			self.surface.blit(self.obj_to_animate, self.curr_pos.get())

		return self.surface




