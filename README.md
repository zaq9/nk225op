#nk225op 
------

`nk225op` is module for fetching latest NK225(Nikkei225) Options Data from JPX Server.

`nk225op`  はJPX(日本証券取引所)のサーバーから、最新の日経２２５オプション清算値を取得するモジュールです。

------

> ブラウザでお気軽に試す場合　⇒　 [Jupyter Notebook example on Google Colab](https://colab.research.google.com/github/zaq9/nk225op/blob/master/doc/eg_nk225op.ipynb)



## Demo:　 (２月限と３月限　権利価格　20500～20750 の清算値とIVデータ表示)

```python
from nk225op import nk225op as nk
nk([201902,201903] , [20500,20750])
```

### Output:

| lb         | PRICE | IV          |
| ---------- | ----- | ----------- |
| 02/C20500  | 340   | 18.3289     |
| 02/C20625  | 260   | 17.5826     |
| 02/C20750  | 195   | 17.2045     |
| .......... | ...   | (以下省略） |




## Install:　(Google Colaboratory 上での利用方法 )

```
!pip install nk225op
```

> ブラウザでお気軽に試す場合　⇒　 [Jupyter Notebook example on Google Colab](https://colab.research.google.com/github/zaq9/nk225op/blob/master/doc/eg_nk225op.ipynb)

------

### ※ローカル環境にInstallする場合   ``` pip install nk225op ```
#### Requirement

- Pandas
- bs4

---------



## 利用できる関数:

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
    """JPXサーバ内にある最新の清算値CSVファイルへのPATHを返す"""

def csv_to_df(csv_path, max_maturity_day=90):
	"""
	清算値CSVファイルをDataFrameに変換
	Parameters
	----------
	csv_path : str
	max_maturity_day :  int , default 90
		最大、SQ期日が何日後までのデータを取得するか（規定値９０日後）
	Returns
	-------
	DataFrame
	"""

```