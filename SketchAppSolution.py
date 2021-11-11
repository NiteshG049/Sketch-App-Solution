a = [int(i) for i in input("Enter the List:").split(" ")]
target = int(input("Enter the Target Number:"))
def search(nums,target)-> int:
	first = 0
	last = len(nums)-1
	while first <= last:
		mid = int((first+last)/2)
		if nums[mid] == target:
			return mid
		if target<nums[mid]:
			last = mid-1
		elif target>nums[mid]:
			first = mid+1
	return mid+1
print(search(a,target))



