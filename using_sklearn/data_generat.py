import random

fout = open('two_class_linear_data.txt', 'w')
for i in range(200):
    x1 = random.uniform(0.0, 45.0)
    y1 = random.uniform(55.0, 100.0)
    x2 = random.uniform(55.0, 100.0)
    y2 = random.uniform(0.0, 45.0)
    if random.randint(1, 2) == 1:
        fout.write(str(x1) + ' ' + str(y1) + ' ' + str(0) + '\n')
    else:
        fout.write(str(x2) + ' ' + str(y2) + ' ' + str(1) + '\n')

fout.close()
