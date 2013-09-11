class FibonacciClass():
	def __init__(self):
		self.x= {}
		self.x[0]=0
		self.x[1]=1
	def fib(self,n):
		try:
			return self.x[n]
		except KeyError:
			self.x[n]= self.fib(n-1)+self.fib(n-2)
			return self.x[n]

			
if __name__ =="__main__":
	f=FibonacciClass()
	print f.fib(8)

