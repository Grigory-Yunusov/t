

my_dict = {"Grigi": "12345", "gosha": "1234567", "Georg": "0000000"}


# print(my_dict)
# def update_user(name, telephone):
#     for kay in my_dict.values():
#         if kay == name:
#             my_dict.pop(name)
#         my_dict[name] = telephone
#
# update_user("Grigi","1010101010011001" )
# print(my_dict)



# def save_user(name, telephone):
#     my_dict[name.title()] = telephone
#
# save_user("selime", "888888888888")
# print(my_dict)

# def get_all_users():
#     my_dict.items()
#     print(my_dict)
# get_all_users()

def get_telephone_user(name):
    for kay in my_dict:
        if kay == name:
            print(my_dict.get(name))

#
# def get_telephone_user(name):
#     for kay, val in my_dict.get():
#         if name == kay:
#             print(val)



get_telephone_user("Georg")
