This directory should have all of the necessary files 

I have added several more unit tests

I have also added more error handling for incorrect input from the user, and it gives feedback messages to the user about what went wrong 

The new test all test various input formats, one is correct in order to make sure that it actually works, one returns no tweets so it tests what happens in that case, 
and the other tests are to see what happens if the user inputs an invalid date format. One tests if there is a non numerical input and the other tests 
if the date is valid aka if it is a real date. 

The unit test is similar, the search input is long and very specific with odd characters. it also must return 5 tweets matching that criteria, which is impossible 
so the guarnateed output is that no tweets with that search term will be found. 

Note about the unit tests- you will have to comment out some of them in Main when they are called (test 4 and 7 specifically) if you want to run the other tests 
as they exit the program when an error is found. 

I hope this is sufficient for a regrade. If not, i'm not sure i will have more time to spend on this before the end of the semester since we recieved this
feedback so late. Please let me know if there are any questions. 
