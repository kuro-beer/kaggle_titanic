import pandas as pd

def FlagWords(text_df, words):
    flags_df = pd.DataFrame(columns=words)
    
    for text in text_df:
        _list = []
        for word in words:
            if word in text:
                _list.append(word)
        _tmp_df = pd.DataFrame([[int(i in _list) for i in words]], columns = words)
        flags_df = flags_df.append(_tmp_df, ignore_index=True)
    return flags_df

