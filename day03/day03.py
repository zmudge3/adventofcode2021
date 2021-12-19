#!/usr/bin/env python3

def calc_gamma_epsilon(nums):
    l = [0]*len(nums[0])
    count = 0
    for num in nums:
        for i in range(len(num)):
            l[i] += int(num[i])
        count += 1
    gamma = "".join("0" if n/count < 0.5 else "1" for n in l)
    epsilon = "".join("1" if n == "0" else "0" for n in gamma)
    return (gamma, epsilon)

nums = []
with open("input.txt", "r") as f:
    for line in f:
        nums.append(line.rstrip())

gamma,epsilon = calc_gamma_epsilon(nums)
consumption = int(gamma,2) * int(epsilon,2)
print(consumption)

ogr_list = nums
for i in range(len(nums[0])):
    if len(ogr_list) == 1:
       break 
    l = []
    gamma = calc_gamma_epsilon(ogr_list)[0]
    for num in ogr_list:
        if num[i] == gamma[i]:
            l.append(num)
    ogr_list = l

csr_list = nums
for i in range(len(nums[0])):
    if len(csr_list) == 1:
       break 
    l = []
    epsilon = calc_gamma_epsilon(csr_list)[1]
    for num in csr_list:
        if num[i] == epsilon[i]:
            l.append(num)
    csr_list = l

life_support_rating = int(ogr_list[0],2) * int(csr_list[0],2)
print(life_support_rating)
