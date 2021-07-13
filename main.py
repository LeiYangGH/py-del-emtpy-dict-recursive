import json
from pprint import pprint
from raw import data

DELETE = 'D'


def mark_d_delete(d):
    if DELETE in d:
        return 0
    else:
        d[DELETE] = True
        return 1


def visit_l(parent_d, l):
    # how many items are marked as to be deleted
    del_cnt = 0
    # if list is empty, parent dict should delete
    if parent_d and l and all(DELETE in x for x in l):
        del_cnt += mark_d_delete(parent_d)
    for d in l:
        if DELETE in d:
            continue
        sections = d['sections']
        if sections:
            if all(DELETE in se for se in sections):
                del_cnt += mark_d_delete(d)
            for sec in sections:
                if DELETE in sec:
                    continue
                if not sec['sections'] and sec['value'] == 'None':
                    del_cnt += mark_d_delete(sec)
                del_cnt += visit_l(sec, sec['sections'])
        elif d['value'] == 'None':
            del_cnt += mark_d_delete(d)
    return del_cnt


def remove_d_if_marked(l):
    deleted = False
    index = len(l) - 1
    # removing items while iterating is dangerous
    # iterating reversed indexes is better
    while index >= 0:
        if DELETE in l[index]:
            del l[index]
            deleted = True
        index -= 1
    return deleted


def delete_empty(l):
    remove_d_if_marked(l)
    for d in l:
        sections = d['sections']
        if sections:
            delete_empty(sections)

# loop until no more item marked as delete
while visit_l(None, data):
    pass
# pprint(data) # debug
# loop until no more item deleted
while delete_empty(data):
    pass
pprint(data)

# print(json.dumps(data))
