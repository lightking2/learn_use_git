

def deco(func):
	print("before funced")
	func()
	print("after funced")
	return func
	
@deco
def myfunc():
	print("myfunc().called.")



myfunc()
myfunc(