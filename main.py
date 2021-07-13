import json
from pprint import pprint
from raw import data

DELETE = 'D'


def mark_d_delete(d):
    if 'item' in d and d['item'] == 'Equity':
        print('*' * 70)
    if DELETE in d:
        return 0
    else:
        d[DELETE] = True
        print('deleted')
        return 1


def visit_l(parent_d, l):
    print('visit_l')
    deleted = 0
    if parent_d and l and all(DELETE in x for x in l):
        deleted += mark_d_delete(parent_d)
    for d in l:
        if DELETE in d:
            continue
        if 'item' in d:
            print(d['item'])
        sections = d['sections']
        if sections:
            if all(DELETE in se for se in sections):
                deleted += mark_d_delete(d)
            for sec in sections:
                print(sec['item'])
                if DELETE in sec:
                    continue
                if (not sec['sections']) and sec['value'] == 'None':
                    deleted += mark_d_delete(sec)
                deleted += visit_l(sec, sec['sections'])
        elif d['value'] == 'None':
            deleted += mark_d_delete(d)
    return deleted


def remove_d_if_marked(l):
    deleted = False
    index = len(l) - 1
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


d = 1
while d > 0:
    print(d)
    d = visit_l(None, data)
pprint(data)
while delete_empty(data):
    pass
pprint(data)

# print(json.dumps(data))
