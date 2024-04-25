import sys
input_file = sys.argv[1]
assignment3 = open(input_file, 'r')
output = open("output.txt.txt", "w")
all_lines=[]
categories={}
tickerNumberStudent=0
tickerNumberFull=0
tickerNumberSeason=0
for line in assignment3:
    b= line.split()
    all_lines.append(b)
for line in all_lines:     
    if line[0]=="CREATECATEGORY":
      def CREATECATEGORY():
        numbers=line[2].split("x")
        rows = int(numbers[0])
        columns = int(numbers[1])
        seatnumber= rows*columns
        n = int(numbers[1])
        category =[]
        while int(n)>0:
          t= chr(64+n)
          k= str(" "+"X")*columns
          category.append(t+k)
          n = n-1 
        categories[line[1]]=category
        output.write("the category " + str(line[1]) + " having " + str(seatnumber) + " seats has been created" + "\n")
      CREATECATEGORY()
    if line[0] == "SELLTICKET":
      def SELLTICKET():
        for words in line:
              group1 = ''
              group2 = ""
              index2 = 0
              index3 = 0
              itsindex1 = 0
              itsindex2 = []       
              if line.index(words)>3:
                if len(words) == 2:                 
                 group1 += words[0]
                 itsindex1+=int(words[1])
                elif len(words) > 2:
                  group2 += words[0]
                  index2 += int(words.split("-")[0][1:])
                  index3 += int(words.split("-")[1])+1                  
                  for indexx in range(index2, index3):
                    itsindex2.append(indexx)                             
              for ttt in categories.get(line[3]):     
                  newnewlist = []            
                  if ttt[0] == group1:
                    newlist = ttt.split()
                    if itsindex1<len(newlist):
                     if newlist[itsindex1] == "X":
                      if line[2]== "student":
                          newlist[itsindex1] = "S"
                          newnewlist = " ".join(newlist)
                      if line[2]== "full":
                          newlist[itsindex1] = "F"
                          newnewlist = " ".join(newlist)
                      if line[2]== "season":
                          newlist[itsindex1] = "T"
                          newnewlist = " ".join(newlist)
                     else:
                      output.write("Warning: The seats "+ words +" cannot be sold to "+ line[1]  +" due some of them have already been sold" + "\n")
                    else:
                      output.write("Error: The category "+ line[3] +" has less column than the specified index " + str(group1)+str(itsindex1)+"!"+ "\n")
                  if not newnewlist == []:
                    kkk = categories.get(line[3]).index(ttt)
                    categories.get(line[3])[kkk] = newnewlist
                    output.write("Success: " + line[1] + " has bought " + words +" at " + line[3] + "\n")
                  if ttt[0] == group2:
                    newlist= ttt.split()
                    for numbersinlist in itsindex2:
                      if index3 < len(newlist):  
                       if line[2]== "student":
                        if newlist[numbersinlist] == "X":
                         newlist[numbersinlist] = "S"
                         newnewlist = " ".join(newlist)
                        else:
                          minitsindex2 = min(itsindex2)
                          maxitsindex2 = max(itsindex2)
                          output.write("Warning: The seats "+ group2 + str(minitsindex2) + "-" + str(maxitsindex2) +" cannot be sold to "+ line[1]  +" due some of them have already been sold"+ "\n")
                          break
                       if line[2] == "full":
                        if newlist[numbersinlist] == "X":
                          newlist[numbersinlist] = "F"
                          newnewlist = " ".join(newlist)
                        else:
                          minitsindex2 = min(itsindex2)
                          maxitsindex2 = max(itsindex2)
                          output.write("Warning: The seats "+ group2 + str(minitsindex2) + "-" + str(maxitsindex2) +" cannot be sold to "+ line[1]  +" due some of them have already been sold"+ "\n")
                          break
                       if line[2] == "season":
                        if newlist[numbersinlist] == "X":
                          newlist[numbersinlist] = "T"
                          newnewlist = " ".join(newlist)
                        else:
                          minitsindex2 = min(itsindex2)
                          maxitsindex2 = max(itsindex2)
                          output.write("Warning: The seats "+ group2 + str(minitsindex2) + "-" + str(maxitsindex2) +" cannot be sold to "+ line[1]  +" due some of them have already been sold")
                          break
                      else:
                        output.write("Error: The category " + line[3] + " has less column than the specified index " + group2 + str(index2) + "-" + str(index3-1) + " !" + "\n")
                        break
                    if not newnewlist == []:
                      kkk = categories.get(line[3]).index(ttt)
                      categories.get(line[3])[kkk] = newnewlist
                      output.write("Success: " + line[1] + " has bought " + words +" at " + line[3] + "\n")                 
      SELLTICKET()
    if line[0] == "CANCELTICKET":
      def CANCELTICKET():
        for words in line:
          group1 = ''
          itsindex1 = 0     
          if line.index(words)== 2:                
            group1 += words[0]
            itsindex1+=int(words[1:])
          for ttt in categories.get(line[1]):
            newnewlist = []
            if ttt[0] == group1:
              newlist = ttt.split()
              if itsindex1< len(newlist)-1:
               if not newlist[itsindex1] == "X":
                newlist[itsindex1] = "X"
                newnewlist = " ".join(newlist)
              else:
                output.write("Error: The category "+ line[1] +" has less column than the specified index " + str(group1)+str(itsindex1)+"!" +"\n")
            if not newnewlist == []:
               kkk = categories.get(line[1]).index(ttt)
               categories.get(line[1])[kkk] = newnewlist
               output.write("Success: "+ "The seat "+ group1 + str(itsindex1) + " at " + line[1] + " has been canceled and now ready to sell again" + "\n")
      CANCELTICKET()
    if line[0] == "BALANCE":
      def BALANCE():
        studenttickets=0
        fulltickets = 0
        seasontickets = 0
        for ttt in categories.get(line[1]):
          newlist = ttt.split()
          for i in newlist:
           if not i == newlist[0]:
            if i == "S":
              studenttickets+=1
            if i == "F":
              fulltickets+=1
            if i == "T":
              seasontickets+=1
        revenues = 10*studenttickets + 20*fulltickets + 250*seasontickets
        output.write("Sum of students = " + str(studenttickets) + " Sum of full pay = " + str(fulltickets) + " Sum of season tickets = " + str(seasontickets) + " and " + "Revenues = " + str(revenues) +"\n")
      BALANCE()
    if line[0] == "SHOWCATEGORY":
      def SHOWCATEGORY():
        output.write("Printing category layout of "+ line[1] + "\n\n")
        for ttt in categories.get(line[1]):
          output.write(ttt + "\n")
        newlist = ttt.split()
        output.write(" ")
        a =len(newlist)
        for j in range(a):
          output.write(" " + str(j))
        output.write("\n")
        output.write("category report of "+ line[1] + "\n")
        output.write("-------------------------------" + "\n")
      SHOWCATEGORY()    
