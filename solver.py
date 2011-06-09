import math
import sys

def digit(num,place):
	value=num%int(math.pow(10,place+1))
	value=value/int(math.pow(10,place))
	return value

def nod(num):
	numofdigits=0
	while(num>0):
		numofdigits+=1
		num=num/10
	return numofdigits

def n2l(num):
	l=[]
	for i in range(nod(num)):
		l.append(digit(num,i))
	return l

def chd(num):
	l=n2l(num)
	for i in l:
		for j in l[l.index(i)+1:]+l[:l.index(i)]:
			if i==j:
				return False
	return True

def check(a,b,c,d,e):
	numlist=[a,b,c,d,e]
	for i in range(5):
		for x in sys.argv[i+1]:
			for y in sys.argv[i+1]:
				cx=numlist[i]
				ix=len(sys.argv[i+1])-sys.argv[i+1].index(x)-1
				cy=numlist[i]
				iy=len(sys.argv[i+1])-sys.argv[i+1].index(y)-1	
				if x==y:
					if digit(cx,ix)!=digit(cy,iy):
						return False
				if x!=y:
					if digit(cx,ix)==digit(cy,iy):
						return False
									
	for p in sys.argv[1]:
		lis=[]
		for q in sys.argv[2]:
			for r in sys.argv[3]:
				for s in sys.argv[4]:
					for t in sys.argv[5]:
						lis=[p,q,r,s,t]
						dic={p:1,q:2,r:3,s:4,t:5}
						for x in lis:
							for y in lis:
								cx=numlist[dic[x]-1]
								ix=len(sys.argv[dic[x]])-sys.argv[dic[x]].index(x)-1
								cy=numlist[dic[y]-1]
								iy=len(sys.argv[dic[y]])-sys.argv[dic[y]].index(y)-1
								if x==y:
									if digit(cx,ix)!=digit(cy,iy):
										return False
								if x!=y:
									if digit(cx,ix)==digit(cy,iy):
										return False
	return True


if len(sys.argv)!=6:
	print "Usage :"
	print "python solver.py <number1> <number2> <product1> <product2> <product>"
	exit()

def solve():					
	for num1 in range(100,1000):
		for num2 in range(10,100):
			product1=digit(num2,0)*num1
			product2=digit(num2,1)*num1
			product=num1*num2
			if check(num1,num2,product1,product2,product):
				print num1,num2,product1,product2,product 
				exit()
				
if __name__=='__main__':
	solve()
