
from multiprocessing import Queue
from rich.console import Console
from rich.table import Table
from subprocess import Popen, PIPE, STDOUT
from multiprocessing import  Process
from functools import partial


def run(fileName, q:Queue,*args):
    user_input = "\n".join(args).encode()

    p = Popen(['python3.8', fileName], stdout = PIPE, stdin = PIPE, stderr=STDOUT)

    stdout , stderr = p.communicate(user_input)
    q.put(stdout.decode())


def parallelRun(*args):

    q1 = Queue()
    #harcoding filenames because only two
    p1 = Process(target= partial(run, "my.py",q1,*args))
    p1.start()

    q2 = Queue()
    p2 = Process(target=partial(run, "answer.py", q2,*args))
    p2.start()

    p1.join()
    p2.join()
    return q1.get().split('\n') ,q2.get().split('\n')

def equateInputOutput(isSame:bool, *args,linesExtra = 0,):
    """
    isSame -> means if no oflines in output and input are same or not
    for isSame True means same lines in output and input
    args --> lines of input
    """
    args = list(args)
    if isSame == False:
        for i in range(linesExtra):
            del args[0]
    return args
def printDecorateTextCompare(final_list):
    console = Console()
    table = Table()

    table = Table(show_header=True, header_style='bold #2070b2',title='[bold]RESULTS')
    table.add_column("Input", justify='center')
    table.add_column("Your answer", justify='center')
    table.add_column("Right Answer", justify='center')

    i = 0
    for x,y,z in zip(final_list[0], final_list[1], final_list[2]):
        table.add_row(x,y,z)
        i+=1
    console.print(table)

def main():
    linesExtra = 0
    isSame = bool(int(input("Please enter 1 if  number of lines in input will be equal to number of lines in output else 0\t")))
   
    if isSame == False:
        linesExtra = int(input("Please enter extra lines in input\t"))
    

    automate_input = input("Press 1 for automatic input or 0 for manual input\t")
    
    # Automate input
    if automate_input == "1":

        # taking range of input
        start , stop = input("Please enter range of input separated by space\nNote: Both numbers will be inclusive\t").split()
        inp = list(range(start, stop))

        # taking output of both file
        my, answer = parallelRun(*inp)
        

        # preparing list
        inpEqualLines = equateInputOutput(isSame, linesExtra=linesExtra,*inp)
      
        
        printDecorateTextCompare([inpEqualLines, my,answer])
    elif automate_input == "0":
        
        print("Enter the inputs\t")
        ls =[]

        while True:
            s = input()
            if s:
                ls.append(s)
            else:
                break
        
        
        my, answer = parallelRun(*ls)
       
       
        inpEqualLines = equateInputOutput(isSame, linesExtra=linesExtra, *ls)
        


        
        printDecorateTextCompare([inpEqualLines, my,answer])

if __name__ == "__main__":
    main()
