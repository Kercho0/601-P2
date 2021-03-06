In this portion of the project, I utilied a few of the NLP APIs from Google in order to take text segments and extract information from it. 
The first script measures sentiment. The script (sentiment.py) takes a piece of text and returns score and magnitude. The score reclects 
how positve or negative the text appears to be according to the NLP algorithm and the magnitude refers to how strongly positive or negatve 
the sentiment expressed in the text appears to be. The included screenshots below deomonstrate this script running on two phrases on opposite
ends of the sentiment spectrum

![Sentiment](/sentiment.png)

The second script (entities.py) attempts to find people, organizations, businesses, etc. within a text snippet. Once, for example,
a name of a person is found, it attempts classifies the name as a person, and displays a salience score, which is an attempt at predicting 
how important the name is within the text relative to the other names that are classified. It also retirieves a wikipedia page link related 
to the extracted name. A screenshot of the script being run on the sentence "Martin Luther King attended Boston University" is shown below. 

![Entity](/entity.png)

The third and final script is a categorization script that takes a piece of text and attempts to classify it based on what is covered in the 
text. It can classify it in multiple different categories, if the text segment is long and covers more than one specific subject. the first 
in the list of categories is the one predominantly covered in the text. This script also returns a convidence percentage, letting the user
know how reliable this classification is. A screenshot of the output from feeding this script multiple varied pieces of text is shown below. 

![Classify](/classify.png)
