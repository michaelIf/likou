# 1491
# 暴力解法
def average(salary):
    salary.sort()
    salary.pop()
    salary = salary[1:]
    return sum(salary)/len(salary)

salary = [4000,3000,1000,2000]
print(average(salary))


# 更好的解法
def way2(salary):
    return (sum(salary)-max(salary)-min(salary))/(len(salary)-2)