from time import time

print()
print("NO NEW LINE IS THERE WRITE CONTINUOUSLY,just SPACES")
s="this is a simple paragraph that is meant to be nice and easy to type which is why there will be no commas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph but just a series of sentences"

print()
print(s)

print("\nAfter you are done press enter to know your time")
input("\nPress any key to Start:")

try:
	print("\nTimer Started\n")
	start=time()
	t=input()
	end=time()
	if(t==s):
		print("\nVoila you typed that correctly")
		print("Your time was %s"%round(end-start,2))

	else: 
		print("\nWrongly entered")
		print("Try again")

except KeyboardInterrupt:
	print("")
