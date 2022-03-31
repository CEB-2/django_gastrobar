import random
from datetime import datetime

random.seed(datetime.today().strftime("gY-&m-%d"))
val = random .randint(1, 3)
print ("first Number", val)
