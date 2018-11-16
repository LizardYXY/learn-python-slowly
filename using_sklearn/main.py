from sklearn import datasets
from sklearn.linear_model import Perceptron
import matplotlib.pylab as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import graphviz

if __name__ == "__main__":
    choose = 4
    if choose == 1:  # Perceptron
        ok = 0
        if ok == 0:
            X = []
            y = []
            # X:数据 y:标签
            x1 = []
            x2 = []
            fin = open('two_class_linear_data.txt', 'r')
            for line in fin.readlines():
                line = line.strip().split(' ')
                para_0 = float(line[0])
                para_1 = float(line[1])
                para_2 = int(line[2])
                X.append([para_0, para_1])
                y.append(para_2)
                if para_2 > 0:
                    x1.append([para_0, para_1])
                else:
                    x2.append([para_0, para_1])
            fin.close()
            clf = Perceptron(alpha=0.1, tol=1e-3, random_state=0)
            print(clf.fit(X, y))
            w = clf.coef_  # 权值向量
            print("Score:%s" % clf.score(X, y))

            # 画图
            plt.figure(num=1)
            x1 = np.array(x1)
            x2 = np.array(x2)
            plt.scatter(x1[:, 0], x1[:, 1], color='red', label='1')
            plt.scatter(x2[:, 0], x2[:, 1], color='blue', label='2')
            plt.legend()
            ww = w[0]
            xx = np.arange(0, 100, 1)
            yy = (-1 - ww[0] * xx) / ww[1]
            plt.plot(xx, yy, linewidth=1, linestyle='--')
            plt.show()
        else:
            iris = datasets.load_iris()
            clf = Perceptron(alpha=0.1, tol=1e-3, random_state=0)
            clf.fit(iris.data, iris.target)
            print("Score:%s" % clf.score(iris.data, iris.target))
    elif choose == 2:  # Naive Bayes
        # data: iris 3 class
        iris = datasets.load_iris()
        clf = GaussianNB()
        # print(iris.data, iris.target)
        # 只使用两个特征
        X = np.array(iris.data)[:, 0:2]
        # print(data)
        # 数据分类
        x0 = []
        x1 = []
        x2 = []
        for i in range(len(X)):
            if iris.target[i] == 0:
                x0.append(X[i])
            elif iris.target[i] == 1:
                x1.append(X[i])
            else:
                x2.append(X[i])
        res = clf.fit(X, iris.target)
        print(res)
        y_pred = res.predict(X)
        plt.figure(num=2)
        x0 = np.array(x0)
        x1 = np.array(x1)
        x2 = np.array(x2)
        plt.scatter(x0[:, 0], x0[:, 1], color='red', label='0')
        plt.scatter(x1[:, 0], x1[:, 1], color='blue', label='1')
        plt.scatter(x2[:, 0], x2[:, 1], color='green', label='2')
        e = []
        for i in range(len(X)):
            if y_pred[i] != iris.target[i]:
                e.append(X[i])
        e = np.array(e)
        plt.scatter(e[:, 0], e[:, 1], label='mislabel', marker="x", color='black')
        plt.title("totol mislable:%s" % (iris.target != y_pred).sum())
        print("totol mislable:%s" % (iris.target != y_pred).sum())
        plt.legend()
        plt.show()
    elif choose == 3:  # 决策树
        # data: iris 3 class
        iris = datasets.load_iris()
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_leaf_nodes=5)
        clf = clf.fit(iris.data, iris.target)
        print(clf)
        dot_data = tree.export_graphviz(clf, out_file=None,
                                        feature_names=iris.feature_names,
                                        class_names=iris.target_names,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = graphviz.Source(dot_data)
        graph.render('iris')
    else:
        iris = datasets.load_iris()
        print(iris)
        X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                            test_size=0.33, random_state=42,
                                                            shuffle=True)

        clf = MLPClassifier(solver='sgd', alpha=1e-5, activation='relu',
                            hidden_layer_sizes=(7,), random_state=1,
                            learning_rate_init=0.15, max_iter=500, n_iter_no_change=10,
                            verbose=True)
        clf.fit(X_train, y_train)
        print(clf)
        print("Training set score: %f" % clf.score(X_train, y_train))
        print("Test set score: %f" % clf.score(X_test, y_test))
