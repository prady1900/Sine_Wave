import csv
from matplotlib import pyplot as plt

values = [127, 146, 164, 182, 198, 213, 226, 236, 245, 251, 254, 254, 252, 247, 247, 239, 229, 217,
          203, 187, 170, 152, 133, 115, 96, 78, 61, 46, 33, 21, 12, 5, 1, 0, 5, 12, 21, 33, 46, 61, 78, 96, 115]
diff_list = []


#FNDING DIFFERENCES B/W NEXT AND PREVIOUS VALUES
for index in range(len(values)-1):
    diff = abs(int(values[index+1] - values[index]))
    diff_list.append(diff)


#WRITING DATA TO A CSV FILE
with open("Sine_Values.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["ORIGINAL VALUES", "DIFFERENCE"])

    for m, n in zip(values, diff_list):
        writer.writerow([m, n])

    writer.writerow([values[-1]])
    f.close()


# funtion to calculate value of x
'''
ans = 0
while ans < 360:
    ans = ans + 9
    x.append(ans)
'''
x = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 174, 177, 180,
      189, 198, 207, 216, 225, 234, 243, 252, 261, 270, 279, 288, 297, 306, 315, 324, 333, 342, 351, 360]


#Sine Wave Graph
plt.plot(x, diff_list)
plt.title("Sine_Wave")
plt.xlabel("ANGLE")
plt.ylabel("Sine Values")
plt.show()






