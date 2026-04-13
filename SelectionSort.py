nums=[5,3,8,6,7,2,1,4,12,455,90,9,60]

def selection_sort(nums):
    for i in range(len(nums)):
        min_index=i

        for j in range(i+1,len(nums)):
            if nums[j]<nums[min_index]:
                min_index=j

        temp=nums[i]
        nums[i]=nums[min_index]
        nums[min_index]=temp

        print(nums)

selection_sort(nums)
print(nums)

