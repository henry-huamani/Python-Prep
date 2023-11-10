import sys
import datetime

if len(sys.argv) == 4:
      humedad = sys.argv[1]
      temperatura = sys.argv[2]
      lluvia = sys.argv[3]
      f = open('clase09_ej2_mysolution.csv','a')
      now = datetime.datetime.now().replace(microsecond=0)
      timestamp = int(datetime.datetime.timestamp(now))
      f.write(f'\n{timestamp},{humedad},{temperatura},{lluvia}')
      f.close()
      print('Success!')
else:
    print('The params need to be 3: [humedad, temperatura, lluvia]')
