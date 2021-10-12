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

input = (filename, "r")
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

for line in input:
  if (Dt.month == "1"): 
    outputJan.write(line)
  elif (Dt.month == "2"): 
    FebuaryLog.write(line)
  elif (Dt.month == "3"): 
    MarchLog.write(line)
  elif (Dt.month == "4"): 
    AprilLog.write(line)
  elif (Dt.month == "5"): 
    MayLog.write(line)
  elif (Dt.month == "6"): 
    JuneLog.write(line)
  elif (Dt.month == "7"): 
    JulyLog.write(line)
  elif (Dt.month == "8"): 
    AugustLog.write(line)
  elif (Dt.month == "9"): 
    SeptemberLog.write(line)
  elif (Dt.month == "10"): 
    OctoberLog.write(line)
  elif (Dt.month == "11"): 
    NovemberLog.write(line)
  elif (Dt.month == "12"): 
    DecemberLog.write(line)
    
  else:
    continue