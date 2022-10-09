with open('abc.txt','r') as file:
    file_line=file.readlines()

dict={}
list_score=[]
final_score=[]

for i in file_line:
    pirnt(i)
    name=i[:-4]
    score=int(i[-4:-1])
    print(name)
    print(score)
    dict[score]=name
    list_score.append(score)

list_score.sort(reserve=True)

for i in list_score:
    result=dict[i]+str(i)+'\n'
    final_score.append(result)

print(final_score)

winner_new = open('winner_new.txt','w',encoding='utf-8') 
winner_new.writelines(final_score)
winner_new.close()