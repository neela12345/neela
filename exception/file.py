try:
   f=open('filedemo.txt')
   f.write('ammu and neela are good sisters')
except:
    print('something went wrong')
finally:
   f.close()
