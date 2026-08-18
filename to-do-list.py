tasks=[]
quit=False

def add(task):
  tasks.append(task)

def view():
  i=0
  while(i<len(tasks)):
    print(tasks[i])
    i+=1

while not quit:
  action=input("would you like to add, view or quit?")
  if (action=="add"):
    add(input("what task would you like to add?"))
  elif (action=="view"):
    view()
  elif (action=="quit"):
    quit=True
  else:
    print("Error. Enter valid command.")
  
