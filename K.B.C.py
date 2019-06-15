question_list = ["(1)How many continents are there?",
                "(2)What is the capital of India",
                "(3)NG mei kaun se course padhaya jaata hai?"]	

options=[["(1)Four","(2)Nine","(3)Seven", "(4)Eight"],	["(1)Chandigarh","(2)Bhopal", "(3)Chennai", "(4)Delhi"],
["(1)Software Engineering", "(2)Counseling", "(3)Tourism", "(4)Agriculture"]]

solution_list = [3, 4, 1]
i=0
while i<len(options):
    print question_list[i]
    j=0
    while j<len(options[i]):
        print options[i][j]
        j=j+1
    user=input("enterv your choice")
    if user==solution_list[i]:
        print"congrats your answer correct"
    else:
        print"OOps! your answer  wrong"
        break
    i=i+1