import os
os.system("clear")
print("   ____   __              __    __               __  \n  / __/  / / ___ _  ___  / /   / /  ___ _ ____  / /__\n / _/   / / / _ `/ (_-< / _ \ / _ \/ _ `// __/ /  '_/\n/_/    /_/  \_,_/ /___//_//_//_.__/\_,_/ \__/ /_/\_\ ")
print("Loading Dependencies...")
def splash():
  os.system("clear")
  print("   ____   __              __    __               __  \n  / __/  / / ___ _  ___  / /   / /  ___ _ ____  / /__\n / _/   / / / _ `/ (_-< / _ \ / _ \/ _ `// __/ /  '_/\n/_/    /_/  \_,_/ /___//_//_//_.__/\_,_/ \__/ /_/\_\ ")
print("2023 https://github.com/BenPI88")
os.system("cat ver.txt")
print("1: Back Up")
print("2: Restore")
option = input("")
if option == "1":
  splash()
  print("Back up to:")
  backupdir = input("")
  splash()
  print("Backing Up...\n\nInitializing...")
  os.system("cd" + backupdir + " && mkdir flashback && cd flashback && mkdir userfiles")
  splash()
  print("Backing Up...\n\nCopying user files...\n\nFlashback needs sudo permissions to access other users' files. If you feel unfomfortable giving sudo access, you can view the source code over at https://github.com/BenPI88/flashback")
  os.system("sudo cp /home/* " + backupdir + "/userdata/")
  splash()
  print("And Boom! All of your files are backed up to " + backupdir + "! Note that installed programs will not be carried over.")
if option == "2":
  splash()
  print("Restore from:")
  restoredir = input("")
  splash()
  print("Restoring...\n\nMaking sure flashback can access " + restoredir + ".")
  os.system("sudo cd " + restoredir)
  splash()
  print("Restoring...\n\nCopying User Data...")
  print("!IMPORTANT!\n\nPlease Create All Users Displayed Below And Press Enter.")
  os.system("dir " + restoredir)
  input("")
  if os.listdir(restoredir + "/") == os.listdir("/home/"):
