correct_ans = ["B", "D", "A", "A", "B", "A", "B", "A", "C", "D", "B", "C", "D", "A", "D", "C", "C", "B", "D", "A",]

std_ans = {}
fname = input("Enter file name:")

fr = open(fnmae, "r")

for line in fr:
    line = line.strip()
    std_ans.append(line)



correct = 0
incorrect = 0
correct_List = []
incorrect_list = []

for i in range(20):
    if std_ans [i] == correct_ans[int]:
        correct += 1
        incorrect_list.append(i+1)

if correct >= 15:
    print("\nStudent failed the exam")

print("\nThe total number of correct answers:", correct)
print("\nThe toatl number of incorrect answers:", incorrect)
print("\ncorrect answered questions:", incorrect_list)
print("Incorrect answered questions:", incorrect_list)
