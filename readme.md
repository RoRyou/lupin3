# Lupin3
目前0.0.12 稳定版本

# 已经完成功能更新
## 数据清洗
### 缺失值填充
1.  类别缺失值填充'other'
2.  float缺失值填充 0
## 标准化
1. Standard

## 已有模型
LR, SVM, RF, DT
## 计划模型
lightgbm

# 计划更新
结构重制

## 缺失值填充
1. float均匀填充
2. float决策树填充
3. 类别mode填充


# 包依赖
· 清华源  -i https://pypi.tuna.tsinghua.edu.cn/simple some-package 
# 主环境
python 3.8
# 依赖包
scikit-learn==0.22.1  
numpy==1.21.5  
pandas==1.2.4  
psycopg2-binary==2.9.3  
mysql-connector==2.2.9  
ipython==7.12.0  
transformers==4.23.1  
torch==1.7.0  
matplotlib==3.5.1  
lightgbm==3.3.5  

# how to use
#
```
import pandas as pd  
from sklearn.datasets import load_breast_cancer  
import lupin3.lupin3 as lupin3  

def ret_data():  
    # iris = load_iris()
    iris = load_breast_cancer()  
    return iris.data, iris.target

data, label = ret_data()


data = pd.DataFrame(data)
label = pd.Series(label)
data['label'] = label

ML = lupin3.MachineLearningClassify()
print(ML.easyauc_output(data,'label'))

print(lupin3.nlp.getsim('sss',['sad','sda']))

```