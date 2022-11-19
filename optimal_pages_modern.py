import pandas as pd

df = pd.read_csv('PR1.csv' ,header=None).to_numpy()

pages = []
for pnum in list(df):
    pages.append(pnum[0])

totality_pages = len(pages)
frams = []
total_frams = []
page_falt = []
num_falt = 0
print("Enter the number of frames: ")
#num_pages =  int(input())
num_pages = 3
max_fram = 0
frams = [None for i in range(num_pages)]
check_optimal = [None for i in range(num_pages)]
for i in range(0,totality_pages):
    if pages[i] not in frams:
        page_falt.append("page fault")
        num_falt+=1
        if None not in frams:
            for j in range(len(frams)):
                if frams[j] not in pages[i+1:]:
                    pages.reverse()
                    check_optimal[j] = pages.index(frams[j]) + totality_pages
                    pages.reverse()
                else:
                    check_optimal[j] = pages[i+1:].index(frams[j])
            frams[check_optimal.index(max(check_optimal))] = pages[i]
        else:
            frams[max_fram] = pages[i]
            max_fram += 1
        
    else:
        page_falt.append("          ")
        
    total_frams.append([])
    for t in list(frams):
        total_frams[-1].append(t)

for x in range(0,totality_pages):
    print(pages[x] , end="")
    print(" " , end="")
    print("-->  " , end="")
    print(page_falt[x], end="")
    print(" = " , end="")
    for p in total_frams[x]:
        print("[ " , end="")
        print(p, end="")
        print(" ]" , end="")
    print("")
print("with page all = " ,end="")
print(totality_pages)
print(num_falt , end="")
print(" pages falut")