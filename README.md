# C.Lo.D.
CLoD (CADF Log Detective) :detective: is a python3 script that parses a log file containing CADF event records (in JSON format).

Install dependencies from requirements.txt
```
pip install -r requirements.txt
```
```
usage: clod.py [-h] -i INPUT

optional arguments:
  -h, --help                  show this help message and exit
  -i INPUT, --input INPUT     input file containing json CADF event records
```  
### eg.
  ```
  python3 clod.py -i cs_events
  ```

