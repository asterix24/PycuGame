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

from pygame.locals import *
import pygame

import cfg
from coordinate import *

list_image = [
	'resourse/images/level1.png',
	'resourse/images/level2.png',
]

class Level(object):
    def __init__(self):
        self.curr = 0
        self.curr_background = None
        self.new()

    def new(self):
        image_name = list_image[self.curr]
        self.curr_background = pygame.image.load(image_name).convert()
        self.curr += 1

    def update(self, surface, context):
        for event in context:
            if (event.type == KEYDOWN and event.key == K_n):
                self.new()

        surface.blit(self.curr_background, (0,0))
        return surface

