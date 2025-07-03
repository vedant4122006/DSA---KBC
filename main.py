questions=[
    ["1. Which data structure uses LIFO (Last In, First Out) principle?",
    "A) Queue",
    "B) Stack",
    "C) Array",
    "D) Linked List",
    2]
    ,
    ["2. What is the time complexity of searching an element in a balanced Binary Search Tree (BST)?",
     "A) O(n)",
     "B) O(log n)",
     "C) O(n log n)",
     "D) O(1)",
     2]
    ,
    ["3. Which of the following is the correct way to implement a queue in Python using collections?",
     "A) queue = list()",
     "B) queue = set()",
     "C) from collections import deque; queue = deque()",
     "D) queue = dict()",
     3]
    ,
    ["4. Which algorithm is used in the sorted() function in Python by default?",
     "A) Merge Sort",
     "B) Quick Sort",
     "C) Timsort",
     "D) Bubble Sort",
     3]
    ,
    ["5. Which of the following is a characteristic of a linked list?",
     "A) Elements are stored in contiguous memory locations",
     "B) Insertion and deletion are expensive",
     "C) Each node contains a data part and a pointer",
     "D) Random access is fast",
     3]
    ,
    ["6. Which data structure is typically used for implementing a priority queue?",
     "A) Stack",
     "B) Array",
     "C) Heap",
     "D) Queue",
     3]
           ]

price=["100,000","200,000","400,000","800,000","1,600,000","3,200,000"]


print('''To answer select 
        A -> 1
        B -> 2
        C -> 3
        D -> 4''')

print("\n")

p=0

for Q in questions:
    print(Q[0])
    print(f"{Q[1]}")
    print(f"{Q[2]}")
    print(f"{Q[3]}")
    print(f"{Q[4]}")
    
    try:   
        a=int(input("Your answer :"))
        
        if (Q[5]==a):
            print("Your answer is correct")
            print(f"Here is your price : {price[p]}")
            p+=1
            print("\n")
            
            a=str(input("Do you want to continue the game? (y/n) : "))
            if a=="y":
                continue
            else:
                break
            
        else:
            print("Sorry but your answer is wrong, Better luck next time....")
            print(f"the answer was {Q[5]}")
            break    
        
    except:  
        print('''Please only select from
        A -> 1
        B -> 2
        C -> 3
        D -> 4''')
        break




    
    
    
