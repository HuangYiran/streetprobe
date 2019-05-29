def load_json_to_pd(li):
    """
    li should be dictionary
    output Dataframe with only one record
    """
    assert(type(li) == dict)
    dict_out = []
    li_name = []
    li_value = []
    keys = li.keys()
    for key in keys:
        if type(li[key]) == dict:
            dict_out.append(load_json_to_pd(li[key])) # forget father's name
        elif type(li[key]) == list:
            li_name.append(key)
            li_value.append(load_jsonlist_to_pd(li[key]))
        else:
            li_name.append(key)
            li_value.append(li[key])
    dict_out.append(pd.DataFrame([li_value], columns = li_name))
    return pd.concat(dict_out, axis = 1)

def load_jsonlist_to_pd(li):
    """
    li should be list of dict
    """
    assert(type(li) == list)
    out = []
    for item in li:
        tmp = load_json_to_pd(item)
        out.append(tmp)
    return pd.concat(out, axis = 0).reset_index().iloc[:, 1:]
