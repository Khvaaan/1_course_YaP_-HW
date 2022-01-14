
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
for count in range(1, 102, 5):
    print('neib_count =', count)
    iris_dataset = load_iris()
    # print(type(iris_dataset))
    
    # print('{}'.format(iris_dataset.keys()))
    
    # print(iris_dataset['DESCR'])
    
    # print(iris_dataset['data'])
    
    # print(iris_dataset['target'])
    
    # print(iris_dataset['target_names'])
    
    # print(iris_dataset['feature_names'])
    
    #train_test_split разбивает данные на две части в соотношении 1/4
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],iris_dataset['target'], random_state=0)
    
    # print(X_train.shape)
    # print(X_test.shape)
    # print(y_train.shape)
    # print(y_test.shape)
    X_train
    
    
    iris_dataframe=pd.DataFrame(X_train, columns = iris_dataset.feature_names)
    iris_dataframe
    
    diagr=pd.plotting.scatter_matrix(iris_dataframe, c =y_train, figsize=(15,15), marker='o', hist_kwds={'bins':20}, s =60, alpha=.8)
    
    #импорт функции классификатора к-ближайших соседей
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=count)
    
    #обучение модели
    knn.fit(X_train, y_train)
    
    X_new = np.array([[3,5,1,0.5]])
    
    #прогноз модели
    prediction = knn.predict(X_new)
    # print(prediction)
    # print('predicted label = {}'.format(iris_dataset['target_names'][prediction]))
    
    #прогноз модели
    y_pred=knn.predict(X_test)
    # print('Прогнозы для тестового набора \n {}'.format(y_pred))
    # print('Метки тестового набора \n {}'.format(y_test))
    
    #расчет accuracy "вручную"
    a = 0
    for i in range(len(y_pred)):
        if y_pred[i]==y_test[i]:
            a+=1
    print('accuracy = ', a/len(y_pred)*100, '%' )
    print('\n')
    
    #расчет accuracy "с помощью метода knn.score"
    #print('accuracy: {:.2f}'.format(knn.score(X_test, y_test))
    
    #расчет параметров precision, recall, F1-score
    from sklearn.metrics import precision_recall_fscore_support
    precision_recall_fscore_support(y_test, y_pred, average='macro')
    
    # from dataset import load_svhn
    # import numpy as np
    # import pandas as pd
    # import matplotlib.pyplot as plt
    # from sklearn.model_selection import train_test_split
    
    # train_X, train_y, test_X, test_y = load_svhn("data", max_train=1000, max_test=100)
    
    #выведем изображения для наглядности

    # plot_index = 1
    # for i in range(100):
    #     plt.subplot(10, 10, plot_index)
    #     image = train_X[i]
    #     plt.imshow(image.astype(np.uint8))
    #     plt.axis('off')
    #     plot_index += 1
    
    
    # Предобработка данных для бинарной классификации
    #binary_train_mask = (train_y == 0) | (train_y == 9)
    #binary_train_X = train_X[binary_train_mask]
    #binary_train_y = train_y[binary_train_mask]
    
    #binary_test_mask = (test_y == 0) | (test_y == 9)
    #binary_test_X = test_X[binary_test_mask]
    #binary_test_y = test_y[binary_test_mask]
    
    # Преобразование в одномерный массив [num_samples, 32*32*3]
    
    # train_X = train_X.reshape(train_X.shape[0],-1)
    # test_X = test_X.reshape(test_X.shape[0],-1)