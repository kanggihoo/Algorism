


dict = {
    "A+":	4.5,
"A0":	4.0,
"B+": 	3.5,
"B0": 	3.0,
"C+": 	2.5,
"C0": 	2.0,
"D+": 	1.5,
"D0": 	1.0,
"F": 0.0
}
arr1 = []
arr2 = []
for _ in range(20):
    subject , degree , level= input().split()
    if not level =="P":
        degree = float(degree)
        score = dict[level]
        arr1.append(degree*score)
        arr2.append(degree)
print(sum(arr1) / sum(arr2))
        
    
    
    