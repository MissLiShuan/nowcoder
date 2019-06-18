'''
题目描述:
    
六一儿童节，老师带了很多好吃的巧克力到幼儿园。每块巧克力j的重量为w[j]，对于每个小朋友i，
当他分到的巧克力大小达到h[i] (即w[j]>=h[i])，他才会上去表演节目。
老师的目标是将巧克力分发给孩子们，使得最多的小孩上台表演。可以保证每个w[i]> 0且不能将多块巧克力分给一个孩子或将一块分给多个孩子。

输入描述:
    
第一行：n，表示h数组元素个数
第二行：n个h数组元素
第三行：m，表示w数组元素个数
第四行：m个w数组元素

输出描述:
    
上台表演学生人数

示例1
 
输入

3 
2 2 3
2
3 1
 
输出

1
'''

n = int(input())#输入n，表示h列表元素个数
h = [int(x) for x in input().split()]#n个h列表元素
m = int(input())#输入m，表示w列表元素个数
w = [int(x) for x in input().split()]#m个w列表元素
num = 0

for i in range(n):  #遍历小朋友个数  
    wmax = max(w) # max(w)表示最大的巧克力重量  
    print(wmax)
    t = h[i] #h[i]表示每个小朋友分到的巧克力大小   
    res = t    
    while res<=wmax: #当小朋友i分到的巧克力大小res大于最大巧克力重量时，迭代停止       
        if res in w:            
            w[w.index(res)] = -1            
            num += 1            
            break        
        else:            
            res += 1
print(num)
