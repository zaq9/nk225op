# nk225op
Module for fetching latest NK225 Options Data

[Jupyter Notebook example on Google Colab](https://colab.research.google.com/github/zaq9/nk225op/blob/master/doc/eg_nk225op.ipynb)


## Install:( Google Colaboratory)

```
!pip install nk225op
```



## Example:

```python

#ex01 :　最新の日経２２５清算値データを取得
#（２月限と３月限、　権利価格20500～20750）


from nk225op import nk225op as nk

nk([201902,201903] , [20500,20750])


```

## Output:

| lb        | PRICE | IV      |
| --------- | ----- | ------- |
| 02/C20500 | 340   | 18.3289 |
| 02/C20625 | 260   | 17.5826 |
| 02/C20750 | 195   | 17.2045 |


#パラメータ等詳細：

```python

def nk225op(maturities=None, strike_range=None):
	"""Download latest Options DATA(NK255) from JPX
	:param maturities: List
		#eg1(monthly type): [201902]
		#eg2(weekly type): [20190125]
		#eg3: [201902 , 201903 , 20190125]
	:param strike_range: List
		#eg: [19000,20000]
	:return: DataFrame
		OptionsPriceList :
	Examples
	--------
	>>>  nk225op([201902],[20500, 21000])
	"""

```


	

```python

def latest_csv_path():
    """
    :return: str :JPXサーバ内にある最新の清算値CSVファイルへのPATH
    """

def csv_to_df(csv_path):
	"""
	:param csv_path: str
	:return: DataFrame
		清算値CSVファイルをDataFrameに変換（SQが90日以内の日経225オプション関連情報のみを抽出）
	"""


```

