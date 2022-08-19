
class std(object):
	def __int__(self,name,RNO):
		self.name=name
		self.RNO=RNO
	def display(self):
		print(self.name)
		print(self.RNO)
	S1=std("Srinu",1)
	S1.display()
	S2=std("John",2)
	S2.display()
obj=std()
print(obj.a)

