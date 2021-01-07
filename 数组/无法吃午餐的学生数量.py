# 1700
# author Yannis
def countStudents(students, sandwiches):
    count = [0] * 2
    for i in students:
        count[i] += 1
    for j in range(len(sandwiches)):
        if count[sandwiches[j]] == 0:
            break
        count[sandwiches[j]] -= 1
    return sum(count)


