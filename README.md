# Data-mining Homework1
##	 FP-Growth

首先，在FP_Growth.py的code中，我設計與老師範例(FP Growth Example.pdf)相同的Item Table內容，如下:
![](https://i.imgur.com/M8jlNIq.png)


Sample data的code為:
```python=
def loadSimpDat():   #生成itemsets
    simpDat = [['Bread', 'Milk', 'Beer'],
               ['Bread', 'Coffee'],
               ['Bread', 'Egg'],
               ['Bread', 'Milk', 'Coffee'],
               ['Milk', 'Egg'],
               ['Bread', 'Egg'],
               ['Milk', 'Egg'],
               ['Bread', 'Milk', 'Egg', 'Beer'],
               ['Bread', 'Milk', 'Egg']]
    return simpDat
```
將Min-support設定為2、產生FP-tree後，可以得知範例的Tree-node與count跟code執行結果相同: