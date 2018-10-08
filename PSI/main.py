#python 3.6
#
#Projet de Sciences de l'ingenieur DURAND Ulysse TS1 : Scanner 3d
#
#Programme qui vient afficher le rendu de l'acquisition du scanner 3d


import os, sys, pygame
from classes import *
from pygame.locals import *

size = width, height = 600,600
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Projet SI scanner3d")


lss = 0
theta = 0
focal = 200


class Drawing:
	def applyperspective(vec,w):
		a = Transform.perspective(w,vec.z)
		b = vec.tomatrix()
		res = a.multiply(b)
		res = res.tovector()
		return res

	def getinorigine(vec):
		return vec.add(Vector([width/2,height/2,0]))

	def apply3dstuff(vec):
		vec = Drawing.applyperspective(vec,focal)
		vec = Drawing.getinorigine(vec)
		return vec


	def ellipse(pos,color,radius):
		pos = Drawing.apply3dstuff(pos)
		pygame.draw.circle(screen,color,(int(pos.x),int(pos.y)),radius,0)

	def line(posa, posb, color, strokeweight):
		posa = Drawing.apply3dstuff(posa)
		posb = Drawing.apply3dstuff(posb)
		pygame.draw.line(screen, color, [int(posa.x),int(posa.y)], [int(posb.x),int(posb.y)],strokeweight)


def main():
	setup()
	while True:
		loop()

def setup():
	lss = width
	if height<width:
		lss = height



def loop():
	events()
	draw()
	pygame.display.update()

def draw():
	global theta
	theta+=0.01
	screen.fill([255,255,255])
	points = []
	for i in range(2):
		for j in range(2):
			for k in range(2):
				points.append(Vector([i*100-50,j*100-50,k*100-50]))

	for i in range(len(points)):
		points[i] = points[i].rotate(theta,theta,theta)
		points[i] = points[i].translate(Vector([0,0,200]))

	for point in points:
		Drawing.ellipse(point,[0,0,0],3)

	def connect(i,j):
		Drawing.line(points[i],points[j],[0,0,0],2)
	for i in range(2):
		connect(i*4+0,i*4+1)
		connect(i*4+2,i*4+3)
		connect(i*4+1,i*4+3)
		connect(i*4+0,i*4+2)
	for i in range(4):
		connect(i,i+4)

def events():
	pygame.time.Clock().tick(30)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.display.quit()
			sys.exit(0)


if __name__=="__main__":
	main()