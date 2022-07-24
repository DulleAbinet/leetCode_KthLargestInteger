class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ele_list = [int(x) for x in nums]
        for i in range(1,len(ele_list)):
            j = i 
            while ele_list[j-1] < ele_list[j] and j>0:
                ele_list[j-1],ele_list[j] = ele_list[j],ele_list[j-1]
                j-=1
                
        return str(ele_list[k-1])
