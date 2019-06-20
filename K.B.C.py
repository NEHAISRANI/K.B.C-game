question_list = ["(1)How many continents are there?",
                "(2)What is the capital of India",
                "(3)NG mei kaun se course padhaya jaata hai?"]	

options=[["(1)Four","(2)Nine","(3)Seven", "(4)Eight"],	["(1)Chandigarh","(2)Bhopal", "(3)Chennai", "(4)Delhi"],
["(1)Software Engineering", "(2)Counseling", "(3)Tourism", "(4)Agriculture"]]

solution_list = [3, 4, 1]
index=0
ans_key = 0
more_index = 0
while index<len(options):
    print question_list[index]
    j=0
    while j<len(options[index]):
        print options[index][j]
        j=j+1
    user=input("enter your answer")
    if user==solution_list[ans_key]:
        print"congrats your answer correct"
    elif user==5050 and  more_index == 0:
        new_option = [["(1) seven","(2) four"],["(1)bhopal","(2) delhi"],["(1) softwere engineering","(2)tourism"]]   
        solution_key_list = [1,2,1]
        ans_i = 0
        s=0
        while s<len(new_option):
            print question_list[index]
            s = index
            ans_i  = ans_key
            z = 0
            while z<len(new_option)-1:
                print(new_option[s][z])
                z=z+1
            user1=input("enter any one")
            if user1==solution_key_list[ans_i]:
                print("hum jreet gye")
                break
            ans_i = ans_i+1
            s = s+1
        more_index =  more_index+1
    else:
        print"OOps! your answer  wrong"
        break
    index=index+1
    ans_key = ans_key+1

  
    
