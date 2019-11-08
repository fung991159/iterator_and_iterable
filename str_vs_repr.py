#Goal of "str" is to be readable
#Goal of "repr" is to be unambigious

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)

print(f'str(a): {str(a)}')  # str(a): 2019-11-08 06:54:34.718650+00:00
print(f'str(b): {str(b)}')  # str(b): 2019-11-08 06:54:34.718650+00:00

print(f'repr(a): {repr(a)}')    # repr(a): datetime.datetime(2019, 11, 8, 6, 54, 34, 718650, tzinfo=<UTC>)
print(f'repr(b): {repr(b)}')    # repr(b): '2019-11-08 06:54:34.718650+00:00'