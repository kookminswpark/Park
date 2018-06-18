import random
class numbergame:
	def __init__(self):
		self.digits = 0
		self.trials = 0
	
	def newgame(self, count):
		self.digits = random.randint(1, count)
		self.trials = 0
	def guess(self, userguess):
		self.trials += 1
		
		if userguess < self.digits:
			msg= "Greater"
		elif userguess > self.digits:
			msg= "Smaller"
		else:
			msg= "Success"
		return msg
	def getguesscount(self):
		return self.trials
if __name__ == '__main__' :
	game = numbergame()
	count = int(input("input Greatest number in range: "))
	game. newgame(count)
	
	while True :
                 userguess = int(input("input guess number: "))
                 print(game.guess(userguess))
         
                 if userguess == game.digits:
                         break
                         
        print("Success in %d trials" % game.getguesscount())
									     
