#!/usr/bin/env python
def fibonacci(n) :
	fib = [1, 1]
	endOfList = len(fib)-1
	while fib[endOfList] < n :
		fib.append(fib[endOfList]+fib[endOfList-1])
		endOfList+=1
	ans = []
	while endOfList >= 0 :
		if n - fib[endOfList] >= 0 :
			ans.append(1)
			n -= fib[endOfList]
		else:
			ans.append(0)
		endOfList-=1
	for dig in ans:
		print dig,

n = input("Ingrese numero natural: ")
fibonacci(n)
