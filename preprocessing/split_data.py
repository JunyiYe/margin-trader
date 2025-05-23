from finrl.meta.preprocessor.preprocessors import data_split

def split_data_by_date(data, train_range, test_range, trade_range):
    train = data_split(data, train_range[0], train_range[1])
    test = data_split(data, test_range[0], test_range[1])
    trade = data_split(data, trade_range[0], trade_range[1])
    return train, test, trade
