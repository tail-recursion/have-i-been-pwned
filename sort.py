import re
import csv

top = set()
ranking = {}
csvfile = open('top-1m.csv')
reader = csv.reader(csvfile, delimiter=',')
for row in reader:
    top.add(row[1])
    ranking[row[1]] = row[0]
    
csvfile.close()

f = open('hibp.txt')
lines = f.readlines()
lines = list(map(lambda x: x.replace('\n','').replace('.txt','').replace(' ','').lower(), lines))
lines = list(map(lambda x: re.sub('\(\d+\)','',x), lines))


pwned_top = []
i = 0
for pwned in lines:
  if pwned in top:
    print(ranking[pwned] + ',' + pwned)
    pwned_top.append([ranking[pwned],pwned])
    i+=1
  else:
    pwned = pwned.replace('www.','')
    if pwned in top:
      print(ranking[pwned] + ',' + pwned)
      pwned_top.append([ranking[pwned],pwned])
      i+=1
  
 pwned_top.sort(key=lambda x: x[0])

 for pwned in pwned_top:
    print(pwned[0] + ', ' + pwned[1])
 
