import pymongo

client = pymongo.MongoClient('localhost', 27017)
test = client['test']
stu = test['stutest']

group_list = []
for i in stu.find().limit(10000):
    # print(i['result']['type'])
    group_list.append(i['result']['type'])
    # print(list(set(group_list)))
group_index = list(set(group_list))
print(group_index)
