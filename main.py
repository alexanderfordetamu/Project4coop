from urllib.request import urlretrieve
import os.path
import re
from datetime import datetime


url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
filename = 'localcopy.log'


#dictionary

Dy = {}
Wk = {}
Mon = {}
totCount = 0
NotSuccCount = 0
RedCount = 0
FilesReq = {}


if not os.path.isfile(filename):
  filename, headers = urlretrieve(url, filename)

AmazonLog = open(filename)

rgx = re.compile("\[(\d\d/[A-Za-z]{3,4}/\d{4}):(\d{2}:\d{2}:\d{2}).+\] \"([A-Z]{3,6}) (.+) HTTP/1.0\" (\d{3}) .*")

for line in AmazonLog:
  parts = rgx.split(line)
  
  if len(parts) < 7:
    continue

  totCount += 1

  Dt = datetime.strptime(parts[1], "%d/%b/%Y")

  
  if Dt.day in Dy:
    Dy[Dt.day] += 1

  else:
    Dy[Dt.day] = 1

  if Dt.strftime("%V") in Wk:
    Wk[Dt.strftime("%V")] += 1

  else:
    Wk[Dt.strftime("%V")] = 1
  
  if Dt.month in Mon:
    Mon[Dt.month] += 1

  else:
    Mon[Dt.month] = 1
  
  if parts[5][0] == '4':
    NotSuccCount += 1
    
  if parts[5][0] == '3':
    RedCount += 1

  if parts[4] in FilesReq:
    FilesReq[parts[4]] += 1

  else:
    FilesReq[parts[4]] = 1  


NotPer = (NotSuccCount/totCount) * 100
RedPer = (RedCount/totCount) * 100
MostReqFile = max(FilesReq, key=FilesReq.get)
LeastReqFile = min(FilesReq, key=FilesReq.get)


print("Total Requests by Day:", Dy,"\n")
print("Total Requests by Week:", Wk, "\n")
print("Total Requests by Month:",Mon, "\n")
print("Percentage of Non-Successful Requests:",round(NotPer,2),"%", "\n")
print("Percentage of Redirected Requests:",round(RedPer, 2), "%", "\n")
print("Most Requested File:" ,MostReqFile, "\n")
print("Least Requested File:" ,LeastReqFile, "\n")

#Creates month files to write to 
input = open(filename, "r")
outputJan = open("JanuaryLog.txt", "w")
outputFeb = open("FebuaryLog.txt", "w")
outputMar = open("MarchLog.txt", "w")
outputApr = open("AprilLog.txt", "w")
outputMay = open("MayLog.txt", "w")
outputJun = open("JuneLog.txt", "w")
outputJul = open("JulyLog.txt", "w")
outputAug = open("AugustLog.txt", "w")
outputSep = open("SeptemberLog.txt", "w")
outputOct = open("OctoberLog.txt", "w")
outputNov = open("NovemberLog.txt", "w")
outputDec = open("DecemberLog.txt", "w")

#Writes month lines to coordinating file
for line in input:
  if "/Jan/" in line:
    outputJan.write(line)
  elif "/Feb/" in line: 
    outputFeb.write(line)
  elif "/Mar/" in line: 
    outputMar.write(line)
  elif "/Apr/" in line:
    outputApr.write(line)
  elif "/May/" in line:
    outputMay.write(line)
  elif "/Jun/" in line: 
    outputJun.write(line)
  elif "/Jul/" in line: 
    outputJul.write(line)
  elif "/Aug/" in line: 
    outputAug.write(line)
  elif "/Sep/" in line: 
    outputSep.write(line)
  elif "/Oct/" in line: 
    outputOct.write(line)
  elif "/Nov/" in line:
    outputNov.write(line)
  elif "/Dec/" in line:
    outputDec.write(line)

#Closes out all text files  
input.close()
outputJan.close()
outputFeb.close()
outputMar.close()
outputApr.close()
outputMay.close()
outputJun.close()
outputJul.close()
outputAug.close()
outputSep.close()
outputOct.close()
outputNov.close()
outputDec.close()