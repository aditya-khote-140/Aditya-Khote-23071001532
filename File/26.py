'''Write a program to print time (), gmtime() ,localtime (), mktime (), ctime (), asctime ()
with conversion using time module.'''

import time

print("Current time:", time.time())
print("GM Time:", time.gmtime())
print("Local Time:", time.localtime())
print("MK Time:", time.mktime(time.localtime()))
print("C Time:", time.ctime())
print("AS Time:", time.asctime())
