from math import *

class Vector:

	def __init__(self, data):
		self.data = data;
		self.x = 0;
		self.y = 0;
		self.z = 0;

		if len(data)>=1:
			self.x = data[0]
		if len(data)>=2:
			self.y = data[1]
		if len(data)>=3:
			self.z = data[2]

		self.length = len(data)

	def display(self):
		point(self.x,-self.y,self.z);

	def printv(self,displaylength = False):
		print()
		if displaylength:
			print("length : "+str(self.length))
			print()
		for i in range(self.length):
			print(str(self.data[i]))


	def tomatrix(self):
		res = Matrix(Matrix.datafromfunction(self.length,1,lambda i,j:self.data[i]))
		return res

	def add(self,x):
		if isinstance(x,Vector) and x.length == self.length:
			return Vector([self.data[i]+x.data[i] for i in range(self.length)])
		elif type(x) is int or type(x) is float:
			return Vector([self.data[i]+x for i in range(self.length)])

	def multiply(self,factor):
		return self.tomatrix().multiply(factor).tovector()

	def rotate(self,thetax,thetay,thetaz):
		mat = self.tomatrix()
		mat = Transform.rotationX(thetax).multiply(mat)
		mat = Transform.rotationY(thetay).multiply(mat)
		mat = Transform.rotationZ(thetaz).multiply(mat)
		return mat.tovector()

	def translate(self,delta):
		return self.add(delta)


class Matrix:

	def __init__(self, data):
		self.data = data
		self.size = self.m, self.n = len(data),len(data[0])

	def datafromvalue(m,n,anumber):
		return Matrix.datawithfunction(m,n,lambda i,j:anumber)

	def datafromfunction(m,n,func):
		res = []
		for i in range(m):
			therow = []
			for j in range(n):
				therow.append(func(i,j))
			res.append(therow)
		return res



	def get(self, i, j):
		return self.data[i][j]

	def set(self, x, i, j):
		self.data[i][j] = x

	def tovector(self):
		return Vector([self.data[i][0] for i in range(self.m)])

	def multiply(self, factor):
		if isinstance(factor, Matrix):
			a = self
			b = factor
			if (a.n == b.m):
				c = Matrix(Matrix.datafromfunction(a.m,b.n,lambda i,j : sum([a.get(i,k) * b.get(k,j) for k in range(a.n)])))
				return c
			else:
				print(a.size,b.size)

		elif type(factor) is float or type(factor) is int:
			c = Matrix(Matrix.datafromfunction(self.m,self.n,lambda i,j: self.get(i,j)*factor))
			return c

	def printm(self, displaysize = False):
		print()
		if displaysize:
			print("size : "+str(self.size))
			print()
		for i in range(self.m):
			text = ""
			for j in range(self.n):
				text+=str(self.get(i,j))+" "
			print(text)

		print()


class Transform:

	def rotationX(theta):
		return Matrix([[  1           ,  0           ,  0           ],
					   [  0           ,  cos(theta)  ,  -sin(theta) ],
					   [  0           ,  sin(theta)  ,  cos(theta)  ]])

	def rotationY(theta):
		return Matrix([[  cos(theta)  ,  0           ,  sin(theta)  ],
					   [  0           ,  1           ,  0           ],
					   [  -sin(theta) ,  0           ,  cos(theta)  ]])

	def rotationZ(theta):
		return Matrix([[  cos(theta)  ,  -sin(theta) ,  0           ],
					   [  sin(theta)  ,  cos(theta)  ,  0           ],
					   [  0           ,  0           ,  1           ]])

	def perspective(w,z):
		return Matrix([[w/z,0  ,0],
					   [0  ,w/z,0],
					   [0  ,0  ,0]])



