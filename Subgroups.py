def subgroups(lst):
    if len(lst) == 1:
        return [lst,[]]
    subg = []
    subs = subgroups(lst[1:])
    subg += subs
    a = [lst[0]]
    for g in subs:
        subg.append(a + g)
    return subg