try:
  print(x)
  '''x=30
  y=0
  print(x/y)'''  
except NameError:
    print('variable x is not defined')
except:
    print('other errors')
