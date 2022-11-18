import sys
class optimal:
    def main(self,raw,num_pages):
        pagesi = raw.rstrip()
        pages = []
        for i in range(0,len(pagesi),4):
            if (i+1 < len(pagesi)):
                if pagesi[i+1] != ' ':
                    pages.append(pagesi[i] + pagesi[i+1])
                else:
                    pages.append(pagesi[i])
            else:
                pages.append(pagesi[i])
        """
        pages = []
        for pnum in list(df):
            pages.append(pnum)
        """
        totality_pages = len(pages)
        frams = []
        total_frams = []
        page_falt = []
        num_falt = 0
        max_fram = 0
        frams = [None for i in range(num_pages)]
        check_optimal = [None for i in range(num_pages)]
        for i in range(0,totality_pages):
            if pages[i] not in frams:
                page_falt.append("fault")
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
                page_falt.append("          ")
        
            total_frams.append([])
            for t in list(frams):
                total_frams[-1].append(t)

        return num_falt,pages,page_falt,total_frams,totality_pages