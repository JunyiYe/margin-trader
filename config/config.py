from finrl.config_tickers import DOW_30_TICKER
from finrl.config import INDICATORS

"""
The ticker 'DOW' is absent from the dataset because it only began trading independently in 
April 2019 following its spin-off from DowDuPont. Therefore, the dataset contains 29 tickers. 
Note that the DOW_30_TICKER list is fixed and does not exactly reflect the actual constituents 
of the DJIA (Dow Jones Industrial Average), which change dynamically over time.
"""
DOW_30 = DOW_30_TICKER
INDICATOR_LIST = INDICATORS

TRAIN_START_DATE = '2009-01-01'
TRAIN_END_DATE = '2018-12-31'
TEST_START_DATE = '2019-01-01'
TEST_END_DATE = '2020-04-30'
TRADE_START_DATE = '2020-05-01'
TRADE_END_DATE = '2023-05-01'