import pandas as pd
import requests
from bs4 import BeautifulSoup

sv = 'https://www.jpx.co.jp'


def latest_csv_path():
	"""
	:return: str
		JPXサーバ内にある最新の清算値CSVファイルへのPATH
	"""
	req = requests.get(sv + "/markets/derivatives/jnet-derivative/index.html")
	soup = BeautifulSoup(req.content, 'html.parser')
	return soup.find(class_="component-file").a.get('href')


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
	"""
	:param csv_path: str
	:return: DataFrame
		報のみを抽出）
	"""
	colName = ("CODE", "NAME", "TYPE", "MATURITY", "STRIKE",
	           "PRICE", "TPRICE", "NK", "IV", "R", "TIME", "BASE")
	df = pd.read_csv(sv + csv_path, skiprows=3, encoding="SHIFT-JIS", names=colName)
	df = df.query(
		'BASE=="日経225"').query(
		f'TIME<={max_maturity_day} ').dropna()
	df = df.assign(
		PRICE=df.PRICE.astype(int),
		STRIKE=df.STRIKE.astype(int),
		lb=df['MATURITY'].astype(str).str[4:] + '/' + df.TYPE.str[0] + \
		   df['STRIKE'].astype(int).astype(str)).set_index(
		'lb')[["PRICE", "TYPE", "STRIKE", "MATURITY", "IV"]]
	return df


def query_df(df, maturities=None, strike_range=None):
	"""
	:param df: DataFrame
	:param maturities: List
	:param strike_range: List
	:return: DataFrame
	"""
	if (maturities is not None):
		df = df.query(f" MATURITY in {maturities}")
	if (strike_range is not None):
		strike_min = strike_range[0]
		strike_max = strike_range[1]
		df = df.query(f"{strike_min} <= STRIKE <= {strike_max}")
	return df.assign(STRIKE=df.STRIKE.astype(int))[['PRICE', 'IV']]


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
	return query_df(csv_to_df(latest_csv_path()), maturities, strike_range)
