import numpy as np
import matplotlib.pyplot as plt
import time

plt.ion()
f = np.zeros((100,100) ,dtype=int)
p_x = []
p_y = []
for j in range(8):
    p_x.append(50)
    p_y.append(50+j)
# f[50,50:58] = 1
f[p_x,p_y] = 1
figure = plt.figure()
for i in range(8):
    plt.cla()
    plt.imshow(f,cmap="Greys_r")
    plt.title("x_head = "+str(p_x[-1])+" , y_head = "+str(p_y[-1]))
    figure.canvas.draw()
    figure.canvas.flush_events()
    # f[50,50+i] = 0
    # f[50,58+i] = 1
    
    ### remove the first point
    f[p_x[0],p_y[0]] = 0
    p_x.pop(0)
    p_y.pop(0)

    ### add new point
    if (i<2):
        # move to right
        p_x.append(p_x[-1])
        p_y.append(p_y[-1]+1)
    elif (i<4):
        # move to top
        p_x.append(p_x[-1]-1)
        p_y.append(p_y[-1])
    elif (i<6):
        # move to left
        p_x.append(p_x[-1])
        p_y.append(p_y[-1]-1)
    else:
        # move to down
        p_x.append(p_x[-1]+1)
        p_y.append(p_y[-1])
    
    if p_x[-1]==-1 or p_x[-1]==100 or p_y[-1]==-1 or p_y[-1]==100:
        break
    else:
        hit_snake = 0
        for j in range(len(p_x)-1):
            if p_x[-1]==p_x[j] and p_y[-1]==p_y[j]:
                hit_snake = 1
                break
        if hit_snake==1:
            break
        else:
            f[p_x[-1],p_y[-1]] = 1
    time.sleep(0.1)
print("game over")

# head = 57
# while (head<100):
#     f[50,head-7:head+1] = 1
#     plt.cla()
#     plt.imshow(f,cmap="Greys_r")
#     plt.title("head = "+str(head))
#     figure.canvas.draw()
#     figure.canvas.flush_events()
#     f[50,head-7:head+1] = 0
#     head = head + 1
#     time.sleep(0.1)
# print("game over")