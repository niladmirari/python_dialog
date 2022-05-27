import sys

args = sys.argv

print("holy...!") # then python file
import subprocess
popen = subprocess.Popen( "/usr/bin/python3 {}".format( args[1]) , shell=True)
popen.wait()


