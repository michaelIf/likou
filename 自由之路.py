# 动态规划


def findRotateSteps(ring,key):
    from collections import defaultdict as d
    choices = d()
    for k in key:
        if k in choices:
            continue
        else:
            choices[k] = []
            for ri, r in enumerate(ring):
                if r == k:
                    choices[k].append(ri)
    counter = [{0: 0}]
    path = d()
    for keyi in range(len(key)):
        counter.append({})
        for choice in choices[key[keyi]]:
            temp = []
            for start in counter[keyi].keys():
                previous_choice = counter[keyi][start]
                s = str(start) + '-' + str(choice)
                if s not in path:
                    d1 = abs(choice - start)
                    d2 = abs(len(ring) - d1)
                    newc = min(d1, d2)
                    path[s] = newc
                temp.append(previous_choice + path[s])
            counter[keyi + 1][choice] = min(temp) + 1
    final = min(counter[-1].values())
    return final