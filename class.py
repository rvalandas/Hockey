class Player:
	playerCount =0
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Player.playerCount += 1
	def displayCount(self):
		print "total count = ", Player.playerCount
	def displayPlayer(self):
		print "Name is ", self.name, " salary is ", self.salary
		
emp1 = Player("Leela", 2000)
emp2 = Player("Mani", 3000)

emp1.displayPlayer()
emp2.displayPlayer()
print "Total players %d" % Player.playerCount
