#!/usr/bin/python
import re
import os
#first: replace br
f1 = file("/Users/liupeng/Desktop/testlog.txt", "r+")
f2 = file("/Users/liupeng/Desktop/crash_temp.txt", "w+")
for s in f1.readlines():
      f2.write(s.replace("<br>","\r\n\n")) 
                          
f1.close()
f2.close()

#second: match crash log and write temp file
f3 = file("/Users/liupeng/Desktop/crash_temp.txt", "r+") 
content = f3.read()   
print content  
s = re.findall(r'^STACK_TRACE ([\s\S]*?)PRODUCT : ', content, re.M)

print s
print '\r\n\n==================match success==================\r\n\n'

#remove the smae log 
l2 = {}.fromkeys(s).keys()
print '\r\n\n==================replace the same ==================\r\n\n'

out_str = ",".join(l2)
# Write them to a file, again using "with" so the file will be closed.
with open("/Users/liupeng/Desktop/output_temp.txt", "w") as outp:
    outp.write(out_str)

#last: out result file.
f4 = file("/Users/liupeng/Desktop/output_temp.txt", "r+")
f5 = file("/Users/liupeng/Desktop/output.txt", "w+")
for s in f4.readlines():
      f5.write(s.replace(",: ","\r\n\n ==================crash log==========================\n\n")) 
                          
f4.close()
f5.close()

print '\r\n\n==================replace success==================\r\n\n'
        
#remove temp file
os.remove("/Users/liupeng/Desktop/output_temp.txt")
os.remove("/Users/liupeng/Desktop/crash_temp.txt")

print '\r\n\n===finish=== \n result file: /Users/liupeng/Desktop/output.txt===============\r\n\n'

