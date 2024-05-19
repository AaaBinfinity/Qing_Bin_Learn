
nums = [int(input(f"请输入第{i+1}个整数: ")) for i in range(5)]

for i, num in enumerate(nums):
    print(f"下标 {i}: 值 {num}")

avg = sum(nums) / len(nums)

list2 = [num for num in nums if num > avg]

print(f"平均值: {avg}")
print(f"列表list2: {list2}")
