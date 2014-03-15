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
	def __init__(self):
		self.update_callback = []

		# Draw text context
		self.texts = []

		# Fall text context
		self.obj_to_animate = None
		self.obj_to_animate_n = None
		self.start_pos = None
		self.curr_pos  = None
		self.end_pos = None

	def draw_text(self, text, color, position, size=18):
		font = pygame.font.Font(cfg.FONT, size)
		txt = font.render(text, True, color)

		self.texts.append({'text': txt, 'position': position.get()})
		self.update_callback.append(self._draw_text_update)

	def _draw_text_update(self, surface):
		for i in self.texts:
			surface.blit(i['text'], i['position'])

		return surface

	def fall_text(self, text, color, start_pos, end_pos, size=18):
		font = pygame.font.Font(cfg.FONT, size)
		self.obj_to_animate = font.render(text, False, color)
		self.obj_to_animate_n = font.render(text, False, cfg.BLACK)

		self.start_pos = Pos(start_pos.x(), start_pos.y())
		self.curr_pos = Pos(start_pos.x(), start_pos.y())
		self.end_pos = end_pos

		self.update_callback.append(self._fall_text_update)

	def _fall_text_update(self, surface):
		if self.curr_pos is not None:
			if self.curr_pos.y() == self.end_pos.y():
				surface.blit(self.obj_to_animate_n, self.curr_pos.get())
				self.curr_pos = Pos(self.start_pos.x(), self.start_pos.y())
				return surface

			surface.blit(self.obj_to_animate_n, self.curr_pos.get())
			self.curr_pos.add_y(2)
			surface.blit(self.obj_to_animate, self.curr_pos.get())

		return surface

	def update(self, surface):
		for update_foo in self.update_callback:
			surface = update_foo(surface)

		return surface


