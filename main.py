import json
from pprint import pprint
from raw import data


def delete_emtpy_from_l(l):
    len0 = len(l)
    l[:] = [d for d in l if 'value' in d and d['value'] != 'None' or d['sections']]
    cnt = len0 - len(l)
    for d in l:
        cnt += delete_emtpy_from_l(d['sections'])
    # cnt is how many dict are deleted
    return cnt


# loop until no new dict is deleted
while delete_emtpy_from_l(data):
    pass

pprint(data)
