# def hello():
#     print('Hello')
#
# hello()


# def hello(name):
#     print('Hello', name)
#
# hello('Ivan')

# def hello(name='Незнакомец'):
#     print('Hello', name)
#
# hello('Ivan')
# hello()

# def my_append(el, my_list=[]):
#     my_list.append(el)
#     print(my_list)

# def my_append(el, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(el)
#     print(my_list)
#
#
# my_append(el='Ivan1')
# my_append(el='Ivan2')
# my_append(el='Ivan5', my_list=[])
# my_append(el='Ivan3')
# my_append(el='Ivan4', my_list=[])

# import requests
#
#
# def get_response(url, method='GET'):
#     if method == 'GET':
#         return requests.get(url).status_code == 200
#     elif method == 'POST':
#         return requests.post(url).status_code == 200
#
#
# response = get_response('https://ya.ru', 'POST')
# print(response)
# response = get_response('https://gb.ru')
# print(response)
# my_list = ['1', '2', '3']
# print(type(my_list[0]))
# my_list = list(map(int, my_list))
# print(my_list[0])


# def my_map(fun, iter):
#     for i in iter:
#         yield fun(i)
#
#
# my_list = list(my_map(int, my_list))
# print(my_list[0])
# print(type(my_list[0]))
# my_list = ['Ivan', 'Moscow'] #get_user(id=4)
# print(my_list[0])
# my_dict = {'name': 'Ivan', 'city': 'Moscow'} #get_user(id=4)
# print(my_dict)
# print(my_dict.get('named', 'Неизвестный пользователь'))
# print(my_dict['namef'])
# my_dict.setdefault('name', None)
# print(my_dict)
# my_dict['name'] = 'Dmitriy'
# print(my_dict)
# counter = my_dict.setdefault('counter', 0)
# print(counter)
# my_dict['counter'] = counter + 1
# print(my_dict)
# counter = my_dict.setdefault('counter', 0)
# print(counter)
# my_dict['counter'] = counter + 1
# print(my_dict)

# users = {
#    1: {
#        'name': 'Ivan',
#        'city': 'Moscow',
#        'phones': [1231321, 12313213215]
#    },
#    2: {
#        'name': 'Dmitriy',
#        'city': 'Moscow',
#    }
# }
#
# if users.get(2) is not None and users.get(2).get('phones') is not None:
#     phones = users.get(1)['phones']
#     print(phones)
#
#
# if users.get(3).get('phones') is not None and users.get(3) is not None:
#     phones = users.get(1)['phones']
#     print(phones)
#

users = {
   1: {
       'name': 'Ivan',
       'city': 'Moscow',
       'phones': [1231321, 12313213215]
   },
   2: {
       'name': 'Dmitriy',
       'city': 'Moscow',
   }
}

# print(users.keys())
# for key in users.keys():
#     print(users[key])

# print(1 in users.keys())
# print(7 in users.keys())

# print(users.pop(1), users, sep='\n')

# for key, value in users.items():
#     print(key, value, sep='\n')
# print(users.values())

# def my_append(*args):
#     l = []
#     l.extend(args)
#     print(l)

# my_append(1,2,3,4,5,6,7)


