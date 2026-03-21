dict1 = {
    "name": "Dan",
    "city": "Tel Aviv",
    "job": "Dev"
}

dict2 = {
    "name": "Daniel",
    "city": "TA",
    "country": "Israel"
}
def two_dictionaries():
    """
    It creates a merged dictionary by doing the following:
    If a key exists in both dictionaries, compares the length of the values.
    If the length of the values in both dictionaries are identical, or dict1 is longer, it takes dict1 data
    If it only exists in one dictionary it takes that
    :return:
    """

    merged = {}

    for key in dict1:
        if key in dict2:
            if len(dict1[key]) >= len(dict2[key]):
                merged[key] = dict1[key]
            else:
                merged[key] = dict2[key]
        else:
            merged[key] = dict1[key]

    for key in dict2:
        if key not in merged:
            merged[key] = dict2[key]
    return merged

print(two_dictionaries())
