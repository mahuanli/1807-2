#coding=utf-8
import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)#常量
CREATE_ENEMY_EVENT = pygame.USEREVENT#pygame常量
CREATE_BULLET_EVENT = pygame.USEREVENT + 1#pygame常量
class GameSprite(pygame.sprite.Sprite):#父类 大写

	def __init__(self,imagename,speed=1):
		super().__init__()#调用父类方法
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y +=self.speed
#背景精灵
class BackGround(GameSprite):
	def __init__(self,is_alt=False):
		self.imagename = "./images/background.png"
		super().__init__(self.imagename, 10)
		self.rect.centerx = SCREEN_RECT.centerx
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super().update()#调用父类
		#把移除屏幕的背景放到屏幕上方
		if self.rect.top >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class EnemySprite(GameSprite):#敌机精灵


	def __init__(self):
		self.imagename = "./images/enemy-1.gif"


		#调用父类方法，创建敌机精灵，并且制定敌机的图像
		super().__init__(self.imagename)
		self.speed = random.randint(1,10)#设置敌机随机速度
		self.rect.bottom = 0#设置敌机随机初始位置
		max = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max)

	def update(self):
		#调用父类方法， 让敌机在垂直方向运动
		super().update()
		#判断是否飞出屏幕 如果是 需要将敌机从精灵组删除
		if self.rect.top >= SCREEN_RECT.height:#销毁敌机
			#print("敌机飞出屏幕...")
			self.kill()


class HeroSprite(GameSprite):#英雄精灵
	def __init__(self):
		self.imagename ="./images/hero1.png"
		super().__init__(self.imagename,0)
		self.bullet_group = pygame.sprite.Group()#创建子弹精灵族
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.height - 60

	def update(self):
		#super().update()
		self.rect.x += self.speed

		if self.rect.left <= 0:
			self.rect.left = 0

		if self.rect.right >= SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width

	def fire(self):
		bullet = BulletSprite()
		bullet.rect.x = self.rect.centerx
		bullet.rect.bottom = self.rect.top-20

		bullet1 = BulletSprite()
		bullet1.rect.x = self.rect.centerx-35
		bullet1.rect.bottom = self.rect.top+30

		bullet2 = BulletSprite()
		bullet2.rect.x = self.rect.centerx+35
		bullet2.rect.bottom = self.rect.top+30
		self.bullet_group.add(bullet)
		self.bullet_group.add(bullet1)
		self.bullet_group.add(bullet2)



#子弹精灵
class BulletSprite(GameSprite):
	def __init__(self):
		self.imagename = "./images/bullet1.png"
		super().__init__(self.imagename,-10)

	def update(self):
		super().update()


		#子弹飞出屏幕 要销毁
		if self.rect.bottom <= 0:
			self.kill()





