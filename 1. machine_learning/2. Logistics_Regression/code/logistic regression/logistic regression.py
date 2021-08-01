import numpy as np
import matplotlib.pyplot as plt

def loaddata(filename):
    file = open(filename)
    x = []
    y = []
    for line in file.readlines():
        line = line.strip().split()
        x.append([1,float(line[0]),float(line[1])])
        y.append(float(line[2]))
    #从 list 到 matrix
    x_matrix = np.mat(x)
    y_matrix = np.mat(y).T
    file.close()
    return x_matrix,y_matrix

#logistic
def w_calc(x_matrix, y_matrix, alpha = 0.001, maxIter = 10001):
    # w init  randn是一种产生标准正态分布的随机数或矩阵的函数，返回一个n*m随机项矩阵
    w = np.mat(np.random.randn(3,1))
    w_dynamic = []
    # w update
    for i in range(maxIter):
        H = 1/(1+np.exp(-x_matrix*w))
        dw = x_matrix.T*(H - y_matrix) #(3,1)
        w-= alpha*dw
        if i%100 == 0:
            w_dynamic.append([w.copy(),i])  #copy才能存到，不是存的是最后一个数
    return w,w_dynamic

x_matrix,y_matrix = loaddata('lr_data.txt')
print("x_matrix",x_matrix,x_matrix.shape)
print("y_matrix",y_matrix,y_matrix.shape)
w_update,w_dynamic = w_calc(x_matrix,y_matrix,0.001,10000)
print('w_update',w_update)


#show
for wi in w_dynamic:
    plt.clf()  #不记录每一步，清除前一步
    w0 = wi[0][0,0]
    w1 = wi[0][1,0]
    w2 = wi[0][2,0]
    plot_x1 = np.arange(1,7,0.01)
    plot_x2 = -w0/w2 - w1/w2*plot_x1
    plt.plot(plot_x1,plot_x2,c='r',label = 'decision boundary')
    plt.scatter(x_matrix[:,1][y_matrix==0].A,x_matrix[:,2][y_matrix==0].A,marker="^",s=150,label='label=0')
    plt.scatter(x_matrix[:,1][y_matrix==1].A,x_matrix[:,2][y_matrix==1].A,s=150,label='label=1')
    plt.grid()
    plt.legend() #标签
    plt.title('iter:%s'%np.str(wi[1]))
    plt.pause(0.1)

    # plt.show()