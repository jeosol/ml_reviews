import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_data(obj, num_rows, num_cols):
    id = -1
    data = np.zeros((num_rows * num_cols, 3))
    for j in range(num_cols):
        for i in range(num_rows):
            id += 1            
            data[id][0] = i+1
            data[id][1] = j+1
            data[id][2] = obj.iloc[id,0]    
    df = pd.DataFrame(data)
    df.columns = ['X1', 'X2', 'y']
    return df

def plot_data(X, y):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    #for i in range(len(X)): 
    #ax.scatter(X.iloc[:,0], X.iloc[:,1], y, cmap='viridis')
    ax.scatter(X[:,0],X[:,1], y, cmap='viridis')
    
def plot_3d_surface(y, num_rows):
    X, Y = np.meshgrid(np.arange(num_rows), np.arange(num_rows))
    Z = y.reshape((num_rows, num_rows))
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='jet', edgecolor='k')
    ax.grid(True)
    ax.set_title('Function Surface');
    ax.set_xlabel('I Grid Index')
    ax.set_ylabel('J Grid Index')
    plt.grid(True)
    
def plot_contour(y, num_rows):
    fig, ax = plt.subplots()
    X, Y = np.meshgrid(np.arange(num_rows), np.arange(num_rows))
    Z = y.reshape((num_rows, num_rows))
    
    cs = ax.contourf(X, Y, Z, levels=[5, 10, 50, 100, 150, 200, 250],
        #colors=['#808080', '#A0A0A0', '#C0C0C0'],
                     extend='both')
    #cs.cmap.set_over('red')
    #cs.cmap.set_under('blue')
    #cs.changed()
    
    ax.set_title('Function Contour');
    ax.set_xlabel('I Grid Index')
    ax.set_ylabel('J Grid Index')
    
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

"""
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
"""
def example_stratified_dataset():
    # source: https://machinelearningmastery.com/cross-validation-for-imbalanced-classification/
    # example of stratified train/test split with an imbalanced dataset
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    # generate 2 class dataset
    X, y = make_classification(n_samples=1000, n_classes=2, weights=[0.99, 0.01], flip_y=0, random_state=1)
    # split into train/test sets with same class ratio
    trainX, testX, trainy, testy = train_test_split(X, y, test_size=0.5, random_state=2, stratify=y)
    # summarize
    train_0, train_1 = len(trainy[trainy==0]), len(trainy[trainy==1])
    test_0, test_1 = len(testy[testy==0]), len(testy[testy==1])
    print('>Train: 0=%d, 1=%d, Test: 0=%d, 1=%d' % (train_0, train_1, test_0, test_1))