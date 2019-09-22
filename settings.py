import pygame

class Settings():
	#settings class to hold values

	def __init__(self):
		self.screen_width = 700
		self.screen_right = 690
		self.screen_height = 500
		self.screen_top = 490
		self.paddle_color = (255,255,255)
		self.paddle_width = 10
		self.paddle_height = 100
		self.ball_color = (255,255,255)
		self.ball_width = 10
		self.ball_height = 10
		self.leftStartX = 20
		self.leftStartY = 200
		self.rightStartX = 670
		self.rightStartY = 200
		self.ballStartX = 345
		self.ballStartY = 195
		self.netStartPos = [349, 0]
		self.netEndPos = [349, 500]
		self.netWidth = 5