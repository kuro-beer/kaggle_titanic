print('loaded: texthandling.py')
import pandas as pd

def FlagWords(text_df, words, independent=False):
    flags_df = pd.DataFrame(columns=words)
    
    for text in text_df:
        _list = []
        for word in words:
            if word in text:
                _list.append(word)
                if independent == True:
                    break

        _tmp_df = pd.DataFrame([[int(i in _list) for i in words]], columns=words)
        flags_df = flags_df.append(_tmp_df, ignore_index=True)
    flags_df = flags_df.astype('int')
    return flags_df






