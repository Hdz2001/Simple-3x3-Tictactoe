import pygame 
import math 

pygame.init()
pygame.display.set_caption('3x3 TicTacToe')

width = 1250 
height = 750

screen = pygame.display.set_mode((width, height))

# COLOURS
BLACK = (0,0,0)
WHITE = (255, 255, 255)

# FONT AND THICKNESS AND BACKGROUND ETC. 
bg = pygame.image.load('dst.jpg')
bg = pygame.transform.scale(bg,(width,height))
icon = pygame.image.load('icon.jfif')
icon = pygame.transform.scale(icon,(int(height/6),int(height/6)))
size = int(height/10)
font = pygame.font.Font('CONSOLA.TTF', size)
thickness = 2;

# VARIABLES
running = True
p1_turn = True
found_winner = False 
mouseX, mouseY = pygame.mouse.get_pos()
p1_move = []
p2_move = []
taken = [[False,False,False],[False,False,False], [False,False,False]]
winning_conditions = [[[1,1],[1,2],[1,3]], [[2,1],[2,2],[2,3]], [[3,1],[3,2],[3,3]], [[1,1],[2,1],[3,1]], [[1,2],[2,2],[3,2]], [[1,3],[2,3],[3,3]], [[1,1],[2,2],[3,3]], [[1,3],[2,2],[3,1]]]

X = font.render('X', True, WHITE)
O = font.render('O', True, WHITE)
player1_text = font.render('P1: X', True, WHITE)
player1_text_rect = player1_text.get_rect(center = (0.87*width, height/6))
player2_text = font.render('P2: O', True, WHITE)
player2_text_rect = player2_text.get_rect(center = (0.87*width, height/2))
p1_turn_text = font.render('P1 Turn', True, WHITE)
p2_turn_text = font.render('P2 Turn', True, WHITE)
result1 = font.render('P1 WINS!', True, WHITE)
result2 = font.render('P2 WINS!', True, WHITE)
result3 = font.render('DRAW!', True, WHITE)
result1_rect = result1.get_rect(center = (0.8*width, 5*height/6))
result2_rect = result2.get_rect(center = (0.8*width, 5*height/6))
result3_rect = result3.get_rect(center = (0.8*width, 5*height/6))

def drawBackGroundAndIcon():
	screen.blit(bg,(0,0))
	screen.blit(icon,(0.64*width,height/12))
	screen.blit(icon,(0.64*width,5*height/12))

def writePlayer1And2():
	screen.blit(player1_text,(player1_text_rect))
	screen.blit(player2_text,player2_text_rect)

def drawBoard():
	pygame.draw.line(screen, WHITE, (height,0), (height,height), thickness)
	pygame.draw.line(screen, WHITE, (0.2*width,0), (0.2*width,height), thickness)
	pygame.draw.line(screen, WHITE, (0.4*width,0), (0.4*width,height), thickness)
	pygame.draw.line(screen, WHITE, (0,1/3*height),(0.6*width,1/3*height), thickness)
	pygame.draw.line(screen, WHITE, (0,2/3*height), (0.6*width,2/3*height), thickness)

	for i in p1_move: 
		currX1 = height/3*(i[0]-1)
		currX2 = height/3*(i[0])
		currY1 = height/3*(i[1]-1)
		currY2 = height/3*(i[1])
		pointX = currX1 + (currX2-currX1)/2
		pointY = currY1 + (currY2-currY1)/2
		p1_rect = X.get_rect(center= (pointX,pointY))
		screen.blit(X, p1_rect)

	for j in p2_move: 
		currX1 = height/3*(j[0]-1)
		currX2 = height/3*(j[0])
		currY1 = height/3*(j[1]-1)
		currY2 = height/3*(j[1])
		pointX = currX1 + (currX2-currX1)/2
		pointY = currY1 + (currY2-currY1)/2
		p2_rect = O.get_rect(center = (pointX,pointY))
		screen.blit(O, p2_rect)

def playerMove(col,row):
	# col is for x axis and row is for y axis 
	global p1_turn
	currX1 = height/3*(col-1)
	currX2 = height/3*(col)
	currY1 = height/3*(row-1)
	currY2 = height/3*(row)

	if (currX1<mouseX<currX2) and (currY1<mouseY<currY2) and not taken[row-1][col-1]:
		if p1_turn:
			p1_move.append([col,row])
			p1_turn = False 
		else: 
			p2_move.append([col,row])
			p1_turn = True
		taken[row-1][col-1] = True

while running:
	drawBackGroundAndIcon();
	writePlayer1And2();
	drawBoard();

	mouseX, mouseY = pygame.mouse.get_pos()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 
		if event.type == pygame.MOUSEBUTTONDOWN and not found_winner:
			if event.button == 1: 
				playerMove(1,1)
				playerMove(1,2)
				playerMove(1,3)
				playerMove(2,1)
				playerMove(2,2)
				playerMove(2,3)
				playerMove(3,1)
				playerMove(3,2)
				playerMove(3,3)

				print(p1_move)
				print(p2_move)
				print(taken)
				print(p1_turn)	
							
	for i in winning_conditions:
		if all(elem in p1_move for elem in i): 
			found_winner = True
			screen.blit(result1,result1_rect)
		elif all(elem in p2_move for elem in i):
			found_winner = True
			screen.blit(result2,result2_rect)
		elif len(p1_move) + len(p2_move) == 9 and not found_winner:
			screen.blit(result3,result3_rect)

	pygame.display.flip()

pygame.quit()
