    #Function with three parameters using equality. 
def function(para1,para2,para3):
  para1=int(input("enter any number"))
  para2=int(input("enter any number"))
  para3=int(input("enter any number"))
  if para1==para2:
    return True
  if para1==para3:
    return True
  if para2==para3:
    return True
  return False

Para1=0
Para2=0
Para3=0

function("para1", "para2", "para3")
