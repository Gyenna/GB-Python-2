def num_translate(num):
    nums = {'one': "один", 'two': "два", 'three': "три", 'four': "четыре", 'five': "пять",
    'six': "шесть", 'seven': "семь", 'eight': "восемь", 'nine': "девять", 'ten': "десять"}
    if num in nums:
        print(nums[num])
    else:
        print('None')


num_translate('two')
