"""
TASK 1
Patricia Mae M. Manuel
"""


Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}
x = Sessions_Attended.values()
x = str(x)
No_of_Sessions = x.split(",")

i = 0
for temp in No_of_Sessions:
    i += 1

print ("I have attended " + str(i) + " sessions.")

