import time
      
def random_value(upper_limit):
    random_int = int(time.time() * 10000000)
    random_int %= upper_limit
    time.sleep(0.25) 
    return random_int
