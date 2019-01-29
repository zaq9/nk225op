# nk225op
Module for fetching latest NK225 Options Data

最新の日経２２５清算値データをJPXサーバから取得する。

 [Jupyter Notebook example](https://github.com/zaq9/nk225op/blob/master/doc/eg_nk225op.ipynb)



## Install:( Google Colaboratory)

```
!pip install git+https://github.com/zaq9/nk225op
```



## Example:

```python

#ex01 :　最新の日経２２５清算値データを取得
#（２月限と３月限、　権利価格20500～20750）


from nk225op import nk225op as nk

nk([201902,201903] , [20500,20750])


```

## Output:

lb			PRICE	IV
02/C20500	340	18.3289
02/C20625	260	17.5826
02/C20750	195	17.2045
03/C20500	545	17.5902
03/C20625	470	17.2074
03/C20750	395	16.6239
02/P20500	175	18.2976
02/P20625	225	17.9199
02/P20750	300	18.6512
03/P20500	410	18.1875
03/P20625	460	17.7986
03/P20750	515	17.4041

