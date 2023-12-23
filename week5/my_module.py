"""import pandas as pd#top level code

df=pd.DataFrame([1,2])

print('this is my module.')  #top level code
print(__name__)
print(pd.__name__)

import datetime
from datetime import timezone
print(timezone.__name__)
print(datetime.__name__)"""

def my_func():
    print("Hello")

def call_api(request):
    pass

if __name__=='__main__': #Diğer yerler import edildiğinde bu kısım çalışmayacak
    my_func()
    request=""
    call_api(request)