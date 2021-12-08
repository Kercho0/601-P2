import searchparty as search 
import tweet_analyzer as analyze
import sys


def test1():
	print("Test 1 Running")
	search.searchparty("Tesla","2021-10-30",10)


def test2():
	print("Test 2 Running")
	search.searchparty("America","2021-01-13",100)

def test3():
	print("Test 3 Running")
	search.searchparty("Halloween","2021-10-29",2500)

def test4():
	print("Test 4 Running")
	analyze.tweet_analyzer("Tesla",'asdlfkasjd;', 5)

def test5():
	print("Test 5 Running")
	analyze.tweet_analyzer("Grammy","2021-03-14", 25)

def test6():
	print("Test 6 Running")
	analyze.tweet_analyzer("Tesla",'', 5)

def test7():
	print("Test 7 Running")
	analyze.tweet_analyzer("Tesla",'2030-21-01', 5)

def unit_test():
	print("Unit Test Running")
	analyze.tweet_analyzer("My nAme 1s Arnaud Harmange and Th!s is a unit T3st That will not r3turn results ",'', 20)

if __name__ == '__main__':
    test1()
    test2()
    test3()
  #  test4()
    test5()
    test6()
  #  test7()
    unit_test()

