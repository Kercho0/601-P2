import searchparty as search 


def test1():
	print("Test 1 Running")
	search.searchparty("Tesla","2021-10-30",10)


def test2():
	print("Test 2 Running")
	search.searchparty("America","2021-01-13",100)

def test3():
	print("Test 3 Running")
	search.searchparty("Halloween","2021-10-29",2500)

if __name__ == '__main__':
	test1()
	test2()
	test3()