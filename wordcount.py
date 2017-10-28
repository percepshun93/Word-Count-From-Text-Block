#open the file in read mode
file = open('sample.txt','r')

for line in file:
	line = line.replace(',','')
	line = line.replace('.','')
	line = line.rstrip()
	words_list = line.split()
	#print(words_list)
	#print(line)
	
	
word_count = {}


for word in words_list:
	word_count[word] = word_count.get(word,0) + 1 
	#If the key 'word' is not there then the get returns 0
	#The first time a word is encountered in a text it's value in the dictionary 
	#should be set to 1 which is done by the +1
	
for key,value in word_count.items():
	print (key,value)

	
#find the most frequent word by finding the value of the highest key-value pair

largest = 0
freq_word = None

for key,value in word_count.items():
	#print(key,value)
	if not key == 'the':    #i included this line because "the" is the most commonly used word ever
		if value > largest:
			largest = value
			freq_word = key

print("\nThe 2nd most frequently used word after 'the' is ->",freq_word,"->and it occurs",largest,'times')



#what is the first word that gets repeated
newdict = {}
newlist=[]
for word in words_list:
	newdict[word] = newdict.get(word,0) + 1
		
	if newdict[word] > 1:
		newlist.append(word)

#print(words_list)		
#print(newlist)	
print("First word to get repeated after 'the' is:",newlist[1])