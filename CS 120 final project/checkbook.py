
def setup():  #ONLY & ALWAYS RUN THIS ON FIRST USE OF PROGRAM
    '''
    initializes checkbook log
    '''
    f = open("checkbook_log.txt","w")
    f.write("### date $ note ; withdrawl , deposit ###\n")
    f.close



def read_line(line):
    '''
    reads information from checkbook log to use for computations.
    '''
    f = open("checkbook_log.txt","r")
    sp0 = line.find('$')
    sp1 = line.find(';')
    sp2 = line.find(',')
    if sp1 != -1:
        date = str(line[:sp0])
        note = str(line[sp0+1:sp1])
        withdrawl = float(line[sp1+1:sp2])
        deposit = float(line[sp2+1:-1])
    else:
        print("ERROR: spacer not found")
        return None
    f.close()
    return date,note,withdrawl,deposit



def writeline(date,note,withdrawl,deposit):
    '''
    writes information to file
    '''
    f = open("checkbook_log.txt","a+")
    f.write("{}${};{},{}\n".format(date,note,withdrawl,deposit))
    f.close()



def depositTotal():
    '''
    calculates total of the deposits and displays it to user
    '''
    f = open("checkbook_log.txt","r")
    line = f.readline()
    dtot = 0
    for line in f:
        sp0 = line.find('$')
        sp1 = line.find(';')
        sp2 = line.find(',')
        if sp1 != -1:
            date = str(line[:sp0])
            note = str(line[sp0+1:sp1])
            withdrawl = float(line[sp1+1:sp2])
            deposit = float(line[sp2+1:-1])
        else:
            print("ERROR: spacer not found")
            return None
        dtot += deposit
    f.close()
    return dtot



def withdrawlTotal():
    '''
    calculates total of the withdrawls and displays it to user
    '''
    f = open("checkbook_log.txt","r")
    line = f.readline()
    wtot = 0
    for line in f:
        sp0 = line.find('$')
        sp1 = line.find(';')
        sp2 = line.find(',')
        if sp1 != -1:
            date = str(line[:sp0])
            note = str(line[sp0+1:sp1])
            withdrawl = float(line[sp1+1:sp2])
            deposit = float(line[sp2+1:-1])
        else:
            print("ERROR: spacer not found")
            return None
        wtot += withdrawl
    return wtot
    f.close()



def majorWithdrawls(x):
    '''
    Finds and prints out all transactions with withdrawls over amount 'x'
    '''
    f = open("checkbook_log.txt","r")
    line = f.readline()
    print("---Date----+---------Note--------------+-----------Withdrawl----------+----------Deposit-------------+")
    for line in f:
        sp0 = line.find('$')
        sp1 = line.find(';')
        sp2 = line.find(',')
        if sp1 != -1:
            date = str(line[:sp0])
            note = str(line[sp0+1:sp1])
            withdrawl = float(line[sp1+1:sp2])
            deposit = float(line[sp2+1:-1])
        else:
            print("ERROR: spacer not found")
            return None
        if withdrawl > x:
            print("{}   |   {}      |        {}        |        {}        |".format(date,noteOutputFormat(note),numOutputFormat(withdrawl),numOutputFormat(deposit)))
    print("-----------+---------------------------+------------------------------+------------------------------+")
    f.close()



def majorDeposits(x):
    '''
    Finds and prints out all transactions with deposits over amount 'x'
    '''
    f = open("checkbook_log.txt","r")
    line = f.readline()
    print("---Date----+---------Note--------------+-----------Withdrawl----------+----------Deposit-------------+")
    for line in f:
        sp0 = line.find('$')
        sp1 = line.find(';')
        sp2 = line.find(',')
        if sp1 != -1:
            date = str(line[:sp0])
            note = str(line[sp0+1:sp1])
            withdrawl = float(line[sp1+1:sp2])
            deposit = float(line[sp2+1:-1])
        else:
            print("ERROR: spacer not found")
            return None
        if deposit > x:
            print("{}   |   {}      |        {}        |        {}        |".format(date,noteOutputFormat(note),numOutputFormat(withdrawl),numOutputFormat(deposit)))
    print("-----------+---------------------------+------------------------------+------------------------------+")
    f.close()

def dateTransactions(x):
    '''
    Finds and prints out all transactions from specified date 'x'
    '''
    f = open("checkbook_log.txt","r")
    line = f.readline()
    print("---Date----+---------Note--------------+-----------Withdrawl----------+----------Deposit-------------+")
    for line in f:
        sp0 = line.find('$')
        sp1 = line.find(';')
        sp2 = line.find(',')
        if sp1 != -1:
            date = str(line[:sp0])
            note = str(line[sp0+1:sp1])
            withdrawl = float(line[sp1+1:sp2])
            deposit = float(line[sp2+1:-1])
        else:
            print("ERROR: spacer not found")
            return None
        if date == x:
            print("{}   |   {}      |        {}        |        {}        |".format(date,noteOutputFormat(note),numOutputFormat(withdrawl),numOutputFormat(deposit)))
    print("-----------+---------------------------+------------------------------+------------------------------+")
    f.close()

def balance():
    '''
    Displays net balance of the checkbook log
    '''
    x = depositTotal() - withdrawlTotal()
    return x
    f.close()

def noteOutputFormat(note):
    '''
    Formats the note to being a consistent length
    '''
    length = len(note)
    opplen = int((18-length)/2)
    output = ""
    if length > 18:
        output = note[:15]+"..."
    if length < 18:
        output = " "*opplen+note+" "*opplen
    if len(output) == 17:
        output = output+" "
    if length == 18:
        output = note
    return output
        
def numOutputFormat(amt):
    '''
    Formats the withdrawl or deposit amt to a consistent length
    '''
    st = str(amt)
    length = len(st)
    opplen = int((14-length)/2)
    output = ""
    if length > 14:
        output = st[:14]
    if length < 14:
        output = " "*opplen+st+" "*opplen
    if len(output) == 13:
        output = output+" "
    if length == 14:
        output = st
    return output

def outputLog():
    '''
    Writes all data in checkbook log to a Neatly formatted output table
    '''
    f = open("checkbook_log.txt","r")
    j = open("chck_output.txt","w")
    j.write("---Date----+---------Note--------------+-----------Withdrawl----------+----------Deposit-------------+\n")
    f_line = f.readline()
    for f_line in f:
        sp0 = f_line.find('$')
        sp1 = f_line.find(';')
        sp2 = f_line.find(',')
        if sp1 != -1:
            date = str(f_line[:sp0])
            note = str(f_line[sp0+1:sp1])
            withdrawl = float(f_line[sp1+1:sp2])
            deposit = float(f_line[sp2+1:-1])
        else:
            print("ERROR: spacer not found")
            return None
        j.write("{}   |   {}      |        {}        |        {}        |\n".format(date,noteOutputFormat(note),numOutputFormat(withdrawl),numOutputFormat(deposit)))
    j.write("-----------+---------------------------+------------------------------+------------------------------+\n")
    j.write("Total      |                           |        {}        |        {}        |\n".format(numOutputFormat(withdrawlTotal()),numOutputFormat(depositTotal())))
    j.write("-----------+---------------------------+------------------------------+------------------------------+\n")
    f.close()
    j.close()
        

