import random

# Təsadüfi n sayda tam ədəd əldə et
n = int(input("Tam ədədlərin sayını daxil edin: "))
original_list = [random.randint(1, 5) for _ in range(n)]

# 4-ə vuraraq yeni siyahı yarat
multiplied_list = [x * 4 for x in original_list]

# 10-dan böyük elementlərin cəmini hesabla
sum_of_greater_than_10 = sum(x for x in multiplied_list if x > 10)

# Nəticəni çap et
print("Təsadüfi ədədlər:", original_list)
print("4-ə vurulmuş siyahı:", multiplied_list)
print("10-dan böyük elementlərin cəmi:", sum_of_greater_than_10)
