import numpy as np
from sklearn.metrics import silhouette_score

def cal(path,l, delimiter='\t'):
    fp = open(path, 'r', encoding='utf-8')
    string = fp.read()  # string是一行字符串，该字符串包含文件所有内容
    fp.close()
    row_list = string.splitlines()  # splitlines默认参数是‘\n’
    print("按行分割完成")
    data = [[float(i) for i in row.strip().split(delimiter)] for row in row_list]
    print("数组计算完成")
    # label用来存放每个样本的簇标签
    labelfc = []
    for i in range(len(data)):
        labelfc.append(int(data[i][0]))
    print("存放标签完成")
    datafc = np.array([[row[i] for i in range(0, l) if i != 0] for row in data])
    averageSilhouette_fc = silhouette_score(datafc, labelfc, metric='euclidean')
    print(path)
    print("averageSilhouette")
    print(averageSilhouette_fc)

cal('/home/lss/workspace/honghong/kdd2/k1.txt',42)
cal('/home/lss/workspace/honghong/USCensus/3k1.txt',69)
