# def func(*args, **kwargs):
#     el_sum = 0
#     if args is None and kwargs is None:
#         pass
#     for i in args:
#         if type(i) == int:
#             el_sum += i
#     return el_sum
#
#
# print(func())
# print(func(1, 5, -3, 'abc', [12, 56, 'cad']))
# print(func(2, 4, 'abc', param_1=2))

# def adun_n(n):
#     if n == 0:
#         return 0
#     else:
#         return n + adun_n(n - 1)
#
#
# print('rez', adun_n(2))

# def adun_p(n):
#     if n == 0:
#         return 0
#     else:
#         if n % 2 != 0:
#             return adun_p(n-1)
#         else:
#             return n+adun_p(n-1)
#
#
# print('rez', adun_p(5))


# def adun_i(n):
#     if n == 0:
#         return 0
#     else:
#         if n % 2 == 0:
#             return adun_i(n - 1)
#         else:
#             return n + adun_i(n - 1)
#
#
# print('rez', adun_i(4))


def ret_int():
    n = []
    n = input('Introduceti un nr:')
    for i in range(0, len(n)):
        if n[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']:
            pass
        else:
            n = 0
            break
    n = int(n)
    return n


a = ret_int()
print(a)
