total = 0 
sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"

for db in range(0,len(sentence)):
    if sentence[db:db+5] == "whale":
        total = total + 1
        
print(total)













#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
#f.close()
