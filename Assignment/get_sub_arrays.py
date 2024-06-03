
# Method to get the number of odd elements within the subarray equal to 3.
def find_sub_array(arr):
    n = len(arr)
    result = []
    
    for i in range(n):
        odd_count = 0
        for j in range(i,n):
            if arr[j]%2 !=0:
                odd_count+=1
                
            if odd_count ==3:
                result.append(arr[i:j+1])
            elif odd_count > 3:
                break
            
    return result     
  
arr = [1,2,1,2,1,1,5]
# arr = [1,2,1,2,1,1,5,4,6,7]
# arr = [3,4,1,8,9,1,5,6,10,13]
data = find_sub_array(arr)
print("Subarrays containing odd elements equal to 3 are:")
for subarrays in data:
    print (subarrays)