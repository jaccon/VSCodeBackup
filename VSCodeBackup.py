import six
import sys, os
import getpass

home = os.getenv("HOME")
username = getpass.getuser() 
VSCODE_Dumper_Dir = home+"/VSCodeBackup/"


if six.PY2:
    input = raw_input

print "**** VSCode Backup Settings Tool ***** "
print ""
print "1) Backup VSCode Settings"
print "2) Restore VSCode Settings"
print "3) Reset to factory default VSCode settings"
print "4) Exit"
print ""
print "Choose yout option:"
data = input("")
print ""

if( data == "1"):
    print "Backup all Workspaces, Extensions, Themes, Icons and Settings"
    print ""
    print "Copy all VSCode settings to: " + VSCODE_Dumper_Dir
    print ""
    os.system("rm -rf "+ VSCODE_Dumper_Dir)
    os.system("mkdir "+ VSCODE_Dumper_Dir)
    os.system("cp -Rvf "+ home + "/.vscode "+ VSCODE_Dumper_Dir)
    os.system("cp -Rvf "+ home + "/Library/Application\ Support/Code "+ VSCODE_Dumper_Dir)
    print ""
    print "Compact all settings files...."
    os.system("open  "+ VSCODE_Dumper_Dir)


if( data == "2"):
    print "Restore all VSCode Settings Backup"
    os.system("rm -rf  "+ home +"/.vscode")
    os.system("rm -rf  " + home +"/Library/Application\ Support/Code")
    os.system("cp -Rvf "+ VSCODE_Dumper_Dir +"/Code " + home + "/Library/Application\ Support/")
    os.system("mkdir -p " + home + "/.vscode")
    os.system("cp -Rv "+ VSCODE_Dumper_Dir + "/.vscode " + home + "/")
    os.system("chown -R " + username +":staff " + home + "/.vscode")
    os.system("chown -R " + username +":staff " + home + "/Library/Application\ Support/Code") 
    os.system("chmod -R 775 " + home + "/Library/Application\ Support/Code") 
    os.system("chmod -R 775 " + home + "/.vscode") 
    print ""
    print username
    print "All configurations are restored, Please restart your VSCode"
    

if( data == "3"):
    print "Reset a VSCode settings to factory defaults"
    os.system("rm -rf "+ home +"/.vscode")
    os.system("rm -rf " + home +"/Library/Application\ Support/Code/")
    print ""
    print "All settings are reseted, good luck ;-) "

if( data == "4"):
    print "Exit script"
    exit

