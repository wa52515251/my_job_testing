# import logging
# def between(input_num,small_num,large_num):
#     return small_num <= input_num <= large_num
#
# def output_bonus():
#     input_num=18
#     ann=[0,10,20,40,80,100]
#     rat=[0.1,0.075,0.05,0.03,0.015,0.01]
#     for i in range(0,5):
#         if between(input_num,ann[i],ann[i+1]):
#             j=i+2
#     for k in (0,j):
#         bonus_1 += (ann[k+1]*rat[k])
#     bonus_2 += (input_num*rat[j-2])
#
# output_bonus()

try_num=0
while try_num !=3:
    user = input("请输入用户名： ")
    user_list = ['alex','bob','sb']
    passwd_list = ['123','234','345']
    if user in user_list:
        passwd = input("请输入密码： ")
        passwd_num = user_list.index(user)
        if passwd == passwd_list[passwd_num]:
            print("登陆成功")
            break
        else:
            print("错误的用户名或密码！")
            if try_num == 3:
                print("您已错误三次，请稍后再试！")
    else:
        print("错误的用户名或密码！")
    if try_num == 3:
        print("您已错误三次，请稍后再试！")
        break
    try_num += 1

