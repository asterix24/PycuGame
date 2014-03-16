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

		self.texts = []
		self.fall_texts = []
		self.blit_texts = []

	def draw_text(self, text, color, position, size=18):
		font = pygame.font.Font(cfg.FONT, size)
		txt = font.render(text, True, color)

		self.texts.append({'text': txt, 'position': position.get()})
		self.update_callback.append(self._draw_text_update)

	def _draw_text_update(self, surface):
		for i in self.texts:
			surface.blit(i['text'], i['position'])

		return surface

	def fall_text(self, text, color, start_pos, end_pos, delay, size=18):
		font = pygame.font.Font(cfg.FONT, size)

		self.fall_texts.append({
			'obj':font.render(text, True, color),
			'p_start':Pos(start_pos.x(), start_pos.y()),
			'p_curr': Pos(start_pos.x(), start_pos.y()),
			'p_end': end_pos,
			'start': pygame.time.get_ticks(),
			'delta': delay
			})

		self.update_callback.append(self._fall_text_update)

	def _fall_text_update(self, surface):
		for i in self.fall_texts:
			if i['p_curr'] is not None:
				if (pygame.time.get_ticks() - i['start']) > i['delta']:
					i['start'] = pygame.time.get_ticks()
					i['p_curr'].add_y(1)

				if i['p_curr'].y() == i['p_end'].y():
					i['p_curr'] = Pos(i['p_start'].x(), i['p_start'].y())

				surface.blit(i['obj'], i['p_curr'].get())

		return surface

	def blit_text(self, text, color, position, delay, size=18):
		font = pygame.font.Font(cfg.FONT, size)
		self.blit_texts.append({
			'obj':font.render(text, True, color),
			'delay': delay,
			'start': pygame.time.get_ticks(),
			'pos':position,
			'on': True
			})

		self.update_callback.append(self._blit_text_update)

	def _blit_text_update(self, surface):
		for i in self.blit_texts:
			if (pygame.time.get_ticks() - i['start']) > i['delay']:
				i['start'] = pygame.time.get_ticks()
				i['on'] = not i['on']

			if i['on']:
				surface.blit(i['obj'], i['pos'].get())

		return surface

	def update(self, surface):
		for update_foo in self.update_callback:
			surface = update_foo(surface)

		return surface


