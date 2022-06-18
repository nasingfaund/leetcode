def find(logs, n):
    logs.sort(key=lambda x: x[0])
    personGroup = dict(enumerate(range(n)))
    group_set_map = {i: {i} for i in range(n)}
    for timestamp, person1, person2 in logs:
        person1, person2 = min(person1, person2), max(person1, person2)

        group1 = personGroup[person1]
        group2 = personGroup[person2]

        if group1 != group2:
            person1_group = group_set_map[group1]
            person2_group = group_set_map[group2]
            if group1 < group2:
                person2_group.update(person1_group)
                for p in person1_group:
                    personGroup[p] = group2
                group_set_map.pop(group1)
            else:
                person1_group.update(person2_group)
                for p in person2_group:
                    personGroup[p] = group1
                group_set_map.pop(group2)
            if len(group_set_map) == 1:
                return timestamp
    return -1
