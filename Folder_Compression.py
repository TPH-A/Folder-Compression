import zipfile, os

use = """
Input folder path and your zip path.
And comprassion this folder to zip!
Please remember!Input folder!
By Top Programmer - Hacker(Administrator)
"""


os.system("color b")

def zipDir(dirpath, outFullName):
	zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
	for path, dirnames, filenames in os.walk(dirpath):
		fpath = path.replace(dirpath, '')
		for filename in filenames:
			zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
	zip.close()


print(use)
while True:
	dirp = input("\nInput folder path:")
	out = input("\nInput zip path:")
	try:
		zipDir(dirp, out)
	except FileNotFoundError:
		print("\nFile not found!")
	else:
		zipDir(dirp, out)
		print("\n" + out + " compression to zip!")
