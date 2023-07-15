print('=== Task1 ===')
def find_and_print(messages):
    """
        超過17歲的敘述有以下4種：
        1. I'm 18 years old.
        2. I'm a college student. (高中畢業為17~18歲)
        3. I am of legal age in Taiwan.
        4. I will vote for Donald Trump next week (美國可投票年齡為18歲) 
        所以只要有說出任一句上列的敘述，就判定為超過17歲
    """
    judges = [
        'I\'m 18 years old.',
        'I\'m a college student.',
        'I am of legal age in Taiwan.',
        'I will vote for Donald Trump next week'
        ]
    for name in messages:
        for judge in judges:
            if judge in messages[name]:
                print(name)
                break
    
find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
})

print('=== Task2 ===')
def calculate_sum_of_bonus(data):
    """
    獎金的計算規則：
    1. 基本的獎金為薪資(salary)的0.02倍
    2. 員工表現(performance)：
       若表現為above average，則獎金+1000TWD；
       若表現為average，則獎金+500TWD；
       若表現為below average，則獎金-500TWD；
    3. 職位(role)：
       若職位為Engineer，則獎金為前兩項的總合再乘以3
       若職位為CEO，則獎金為前兩項的總合再乘以2
       若職位為Sales，則獎金為前兩項的總合再乘以2
    """
    bonus_sum = 0
    for employee in data["employees"]:
        bonus = 0
        salary = employee['salary']
        performance = employee['performance']
        role = employee['role']
        # 薪水
        if type(salary) == str:
            if 'USD' in salary:
                salary = int(salary[:-3])*30
            elif ',' in salary:
                salary = int(salary.replace(',',''))
        bonus += salary*0.02
        # 表現
        if performance == 'above average':
            bonus += 1000
        elif performance == 'average':
            bonus += 500
        else:
            bonus -= 500
        # 職位
        if role == 'Engineer':
            bonus *= 3
        else:
            bonus *= 2
        bonus_sum += bonus
    print(bonus_sum)

calculate_sum_of_bonus({
    "employees":[
        {
            "name":"John",
            "salary":"1000USD",
            "performance":"above average",
            "role":"Engineer"
        },
        {
            "name":"Bob",
            "salary":60000,
            "performance":"average",
            "role":"CEO"
        },
        {
            "name":"Jenny",
            "salary":"50,000",
            "performance":"below average",
            "role":"Sales"
        }
    ]
})

print('=== Task3 ===')
def func(*data):
    from collections import defaultdict
    mid_name_dic = defaultdict(int)
    special_name = 'None'
    for name in data:
        mid_name_dic[name[1]] += 1
    for mid_name in mid_name_dic:
        if mid_name_dic[mid_name] == 1:
            special_name = mid_name
            break
    if special_name == 'None':
        print('沒有')
    else:
        for name in data:
            if name[1] == special_name:
                print(name)
                break

func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

print('=== Task4 ===')
def get_number(index):
    def get(index):
        if index == 0:
            return 0
        elif index%2 == 0:
            return get(index-1) - 1
        else:
            return get(index-1) + 4
    print(get(index))

get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15

print('=== Task5 ===')
def find_index_of_car(seats, status, number):
    candidate=[]
    for i in range(len(status)):
        if status[i]==1:
            if seats[i]>=number:
                candidate.append(i)
    candidate=sorted(candidate,key=lambda k:abs(seats[k]-number))
    if candidate==[]:
        print(-1)
    else:
        print(candidate[0])

find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
