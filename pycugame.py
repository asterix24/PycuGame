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
#               Francesca Basile <hidefix92@gmail.com>
#
# \author Daniele Basile <asterix24@gmail.com>
# \author Francesca Basile <hidefix92@gmail.com>
#

import sys

import pygame
from pygame.locals import *

import cfg
import font_mgr
import levels
from coordinate import *

# Funzione di init, dove si inizializza la
# finestra principale e tutto il resto
# questa funzione ritorna il contesto,
# ovvero tutto quello che serve agli altri
# oggetti per essere renderizzati a video.
def init():
	pygame.init()
	fpsclock = pygame.time.Clock()
	displaysurf = pygame.display.set_mode((cfg.WINDOWWIDTH, cfg.WINDOWHEIGHT))

	pygame.display.set_caption(cfg.TITLE)
	
	background = pygame.Surface(displaysurf.get_size())
	background = background.convert()

	return fpsclock, displaysurf, background

def event_mgr(context):
	for event in context:
		# usciamo con ESC e q
		if event.type == QUIT or (event.type == KEYDOWN and
				(event.key == K_ESCAPE or event.key == K_q)):
			pygame.quit()
			sys.exit()

# Questo e' il loop principale, dove si aggiorna lo stato
# delle varie cose.
def pycugame():
	fpsclock, displaysurf, background = init()

	# inizializzo il fontmanager
	font = font_mgr.FontMgr()
	font.fall_text("Pycu Game! 1", cfg.YELLOW, Pos(100,100), Pos(100,400), 30)
	font.fall_text("Pycu Game! 2", cfg.BLUE, Pos(400,100), Pos(400,400), 10)
	font.draw_text("Pycu Game! 3", cfg.RED, Pos(200, 200))
	font.draw_text("Pycu Game! 4", cfg.WHITE, Pos(400, 200))
	font.blit_text("Pycu Game! 5", cfg.GREEN, Pos(50, 50), 500)
	font.blit_text("Pycu Game! 6", cfg.GREEN, Pos(52, 52), 500)
	lev_mgr = levels.Level()

	while True:
		background.fill(cfg.BLACK)
		ev_ctx = pygame.event.get()

		event_mgr(ev_ctx)

		background = lev_mgr.update(background, ev_ctx)

		background = font.update(background)
		displaysurf.blit(background, (0, 0))

		pygame.display.flip()
        fpsclock.tick(cfg.FPS)

if __name__ == "__main__":
	pycugame()

