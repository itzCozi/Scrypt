try:
  import random
  import os
  import sys
  import rsa
  import string
  import hashlib
  import platform
  import time, datetime
except ImportError:
  print("Error: Missing module(s) please install the following module(s): random, time, hashlib, string")


# Classes
class functions:
  def clearconsole():
    if platform == "linux" or platform == "linux2":
      os.system("clear")
    else:
      os.system("cls")
    return str("")

  def createDigest():
    keyValue = random.randint(90, 200)  
    buffer = random.randint(6, 9) 
    publicKey, privateKey = rsa.newkeys(keyValue)
    encMessage = rsa.encrypt(str(random.randint(1,3)).encode(), publicKey)
    hexMessage = binascii.hexlify(encMessage)
    bar = str(hexMessage).replace("'", '')
    foo = str(bar).replace('b', '')

    if len(list(foo)) > 10:
      foolist = list(foo)
      returnvalue = ''.join(random.choice(foolist)for i in range(buffer))
    else:
      returnvalue = foo
    return returnvalue
  
  def checkfile(file, print=None):
    if os.path.isfile(file) == False:
      returnList = ("File not found", "Or is not a file")
    if os.path.isfile(file) == True:
      with open(file, "r") as File:
        lines = File.readlines()
        size = ("Size:", os.path.getsize(file))
        lastedited = ("Last-Opened:", os.path.getmtime(file))
        linenum = ("Line-Number:", len(lines))
        creationTime = ("Created:", os.path.getctime(file))
        returnList = (size, lastedited, linenum, creationTime)
      if print!=None:
        print(returnList)
      else:
        return returnList

  def mutilate(file):
    with open(file, "r+") as Fout:
      for line in Fout:
        lineList = list(line)
        randoms = list(string.printable)
        
      for i in lineList:
        newList = lineList + randoms
        random.shuffle(newList)
 
      newLine = ''.join(random.choice(newList) for i in range(len(lineList)))
      Fout.truncate(0)
      Fout.write(newLine)

  def getinfo():
    # DISCLAMER: This is not for malicious use, this is for development only.
    OS = ("Operating-System: ", sys.platform)
    currentTime = ("Time: ", datetime.now().time())
    currentDate = ("Date: ", datetime.now().date())
    currentProccess = ("Current-Process: ", os.getpid())
    encoding = ("Encoding: ", sys.getfilesystemencoding())
    returnList = (OS, currentDate, currentTime, currentProccess, encoding)
    return returnList
  
  def wipefile(file):
    with open(file, "w") as Fout:
      Fout.truncate(0)
      Fout.close()
    return str("")


def parse(file):
  with open(file,'r+')as FILE: