# Application-of-OPTIMAL-Page-replacement-algorithm
  this is Application of OPTIMAL Page replacement algorithm use python language wiht pandas library and tkinter library.
<br />

# Installation
  Use the package manager pip to install foobar in terminal.
  pandas library
  ```bash
pip install pandas
```
tkinter library
```bash
pip install tk
```

# Optimal Page Replacement Algorithm
>  "Optimal page replacement algorithm" is the most desirable page replacement algorithm that we use for replacing pages. This algorithm replaces the page whose demand in the future is least as compared to other pages from frames (secondary memory). The replacement occurs when the page fault appears. The purpose of this algorithm is to minimize the number of page faults. Also, one of the most famous abnormalities in the paging technique is "Belady's Anomaly", which is least seen in this algorithm.
  <br />
  example Algorithm :
  
  ![image](https://user-images.githubusercontent.com/94011063/231655763-78010658-702e-4992-ab70-29bc354d82d7.png)
  
   From the picture the page replacement algorithm aims to reduce page faults as much as possible. To do this, this algorithm searches for the page from reference, which is not going to be used earliest, and considers this page useless for that instant of time. And that page is replaced by the new page in the frame. Suppose we have a reference page ( 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3) and number of frames is 4. The first pages(7,0,1,2) will be loades into first 4 frames.
   <br />
   <br />
   after that, we need to load page '0' but it is already present in frames, so there will be a "Hit". Then page '3' needs to be loaded but it is not available in frames so, the algorithm will go through the reference and search for that page that is not going to be used in the future early. Here, page 7 is not going to be used in the future and hence the algorithm will replace 'page 7' with 'page 3'. It will be again a "Miss". Now, the system will call for page 3, and it is already present so there will be a "Hit". After that, we need to load 'page 4' but it is not present in the frames. So, the algorithm will again start searching for the page which is in the least demand in the future i.e.- 'page 1'. So, page 1 will be replaced by 'page4' in the frame.
   <br />
   <br />
  [reference information](https://www.scaler.com/topics/optimal-page-replacement-algorithm/)
  <br />
  <br />
  # Code Optimal Page Replacement Algorithm
  in file optimal_pages.py
  * import
  ```
  import pandas as pd

df = pd.read_csv('PR1.csv' ,header=None).to_numpy()

pages = []
for pnum in list(df):
    pages.append(pnum[0])
  ```
  * algorithm
  ```
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
                    frams[j] = pages[i]
                    break
                else:
                    check_optimal[j] = pages[i+1:].index(frams[j])
            if pages[i] not in frams:
                frams[check_optimal.index(max(check_optimal))] = pages[i]
        else:
            frams[max_fram] = pages[i]
            max_fram += 1
        
    else:
        page_falt.append(" ")
        
    total_frams.append([])
    for t in list(frams):
        total_frams[-1].append(t)
  ```
  * print 
 ```
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
print(num_falt , end="")
print(" pages falut")
 ```
