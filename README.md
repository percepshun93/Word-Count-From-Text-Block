# Word-Count-From-Text-Block
This code shows the number of times every word has been used in a given block of text. It also shows the most frequently used word and also the first word that gets repeated.

# Functionality

A given block of text is read using the python file i/o operations.
The text block is formatted to remove all commas so that each word can be placed as an element of a list using the split() function.
A dictionary is then created which will hold the words and the number of times they are repeated as key-value pairs.

This key value pair is then printed.

# Making the list of words

Using python's built in functionality for reading files, make a list of all the words using this line:

file = open('text_block.txt','r')

this basically creates a file object that opens the specified file in read mode. This ensures that the file cannot be overwritten or deleted.

once the file object is created, we can read each line of the contents in the text file and add every word to a list as so:

for line in file:
  line.split()
  
We now have a list containing all the words of the text file as elements of the list, ready to be iterated upon.


# Getting the number of repetitions

The main line of code here is:

dictionary_of_words[word] =  dictionary_of_words.get(word,0)

This line basically checks if the [word] is already present in the dictionary. If it is not, then it returns 0. 
So basically every time a word from the list of words is encountered for the first time, this line will return a 0. We however want to set it to 1 since when a word is encountered for the first time, it's count is 1.

So our code now becomes:

dictionary_of_words[word] =  dictionary_of_words.get(word,0) + 1

Now for a repeated increment in the count, all you have to do is place this in a loop for every word in the list, i.e, for the entire text block.

for word in words_list:
  dictionary_of_words[word] =  dictionary_of_words.get(word,0)+1
  
 Now you'll have a dictionary that countains all the words as Keys and their counts as Values. These key-value pairs can be printed out as such:
 
 for key,value in dictionary_of_words.items():
  print(key,value)
  
 # Finding the most frequent word
 
 Once you have the count of all the words in the text, all you have to do is find the Key (word) that has the largest count (value).
 Run a max loop for that.
 
 # Finding the first word that gets repeated
 
 The main idea behind this is, the first word that has its count incremented above 1 is the first word that gets repeated.
