#!/usr/bin/python
import re
import os
#first: replace br
f1 = file("/Users/liupeng/Desktop/testlog.txt", "r+")
f2 = file("/Users/liupeng/Desktop/crash_temp.txt", "w+")
for s in f1.readlines():
      f2.write(s.replace("<br>","\r\n\n")) 
      print s  
                          
f1.close()
f2.close()

#second: match crash log and write temp file
f3 = file("/Users/liupeng/Desktop/crash_temp.txt", "r+") 
content = f3.read()   
print content  
s = re.findall(r'^STACK_TRACE ([\s\S]*?)PRODUCT : ', content, re.M)

print s
print '\r\n\n==================match success==================\r\n\n'


#sort function  
from collections import defaultdict    
def leaders(xs, top=10):
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]
    

print leaders(s)


print '\r\n\n==================replace the same ==================\r\n\n'

# out_str = ",".join(str(leaders(s)))
# Write them to a file, again using "with" so the file will be closed.
with open("/Users/liupeng/Desktop/output_temp.txt", "w") as outp:
    for x in leaders(s):
        s = str(x)
        patt = re.compile( r'\\r\\n\\n')
        b = patt.sub('<br>',s)
        patt = re.compile( r'\\r\\n\\n\\tat')
        b = patt.sub('<br>',b)
        print b
        patt = re.compile( r'\\tat')
        b = patt.sub('<br>',b)
        print b
        outp.write('   ====================start==================   \r\n\n \r\n\n')
        outp.write(b + '\r\n\n \r\n\n     ==================new log ==================       \r\n\n \r\n\n  ') 
        outp.write(' \r\n\n \r\n\n    ======================end================   \r\n\n \r\n\n')

    
#last: out result file.
f1 = file("/Users/liupeng/Desktop/output_temp.txt", "r+")
f2 = file("/Users/liupeng/Desktop/output.txt", "w+")
for s in f1.readlines():
      f2.write(s.replace("<br>","\r\n\n").replace('\n',"")) 
      print s  
                          
f1.close()
f2.close()

print '\r\n\n==================replace success==================\r\n\n'
        
#remove temp file
os.remove("/Users/liupeng/Desktop/output_temp.txt")
os.remove("/Users/liupeng/Desktop/crash_temp.txt")

print '\r\n\n===finish=== \n result file: /Users/liupeng/Desktop/output.txt===============\r\n\n'

