
def map_ids(dataframe):
    _dict = {}
    for index, row in dataframe.iterrows():
        _dict[row['id_1']] = row['id_2']
    return _dict
