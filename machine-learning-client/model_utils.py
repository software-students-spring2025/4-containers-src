import numpy as np

def preprocess_image():
    pddata_train = pd.read_csv('data/sign_mnist_train.csv')
    data_train = pddata_train.values
    data_train_X = data_train[:,1:]
    data_train_X = data_train_X.reshape((data_train_X.shape[0], 28,28,1))
    data_train_y = data_train[:,:1].reshape(-1)
    data_train_y = to_cat(data_train_y, 26)

    test_size = 0.1
    test_ind = int(test_size*data_train_X.shape[0])
    data_train_X, data_val_X, data_train_y, data_val_y = data_train_X[test_ind:], data_train_X[:test_ind],data_train_y[test_ind:], data_train_y[:test_ind]


    pddata_test = pd.read_csv('data/sign_mnist_test.csv')
    data_test = pddata_test.values
    data_test_X = data_test[:, 1:]
    data_test_X = data_test_X.reshape((data_test_X.shape[0], 28,28,1))
    data_test_y = data_test[:, :1].reshape(-1)
    data_test_y = to_cat(data_test_y, 26)

def to_cat(y, num_cats):
    res = []
    for i in range(y.shape[0]):
        label = [0]*num_cats
        label[y[i]] = 1
        res.append(label)
    return np.array(res)

def accuracy(y_pred, y):
    num_correct = 0
    for i in range(y_pred.shape[0]):
        num_correct += y_pred[i].argmax() == y[i].argmax()
    return num_correct / y_pred.shape[0]