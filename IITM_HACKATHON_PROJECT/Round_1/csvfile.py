import csv
with open('bounce.csv','w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow([' bounce_number ',' time_of_bounce ',' quadrant_of_bounce ',' frame_number '])
    thewriter.writerow([' 1 ',' 0.702423 ',' 4 ',' 42 '])
    thewriter.writerow([' 2 ',' 1.505192 ',' out of bound ',' 90 '])
    thewriter.writerow([' 3 ',' 2.843141 ',' 1 ',' 170 '])
    thewriter.writerow([' 4 ',' 3.662635 ',' out of bound ',' 219 '])
    thewriter.writerow([' 5 ',' 5.318347 ',' 1 ',' 318 '])
    thewriter.writerow([' 6 ',' 6.371982 ',' 2 ',' 381 '])
    thewriter.writerow([' 7 ',' 7.191476 ',' out of bound ',' 430 '])
    thewriter.writerow([' 8 ',' 8.847188 ',' 2 ',' 529 '])
    thewriter.writerow([' 9 ',' 11.991369 ', ' 3 ', ' 717 '])
    thewriter.writerow([' 10 ',' 14.767613 ', ' 3 ', ' 883 '])
    thewriter.writerow([' 11 ',' 16.941780 ', ' out of bound ', ' 1013 '])
    thewriter.writerow([' 12 ',' 18.145934 ', ' 2 ', ' 1085 '])
    thewriter.writerow([' 13 ',' 20.303377 ', ' 2 ', ' 1214 '])
