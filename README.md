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
  
  #### Executing CloD for OpenStack events file (raw_cadf_sample) and for CloudStack events file (cs_events)
  ![Executing CLod](https://github.com/ndalezios/clod/blob/master/images/1.png)
  
  #### Using a MongoDB client (robo3T) to view Collections 
  ![Viewing CADF Records](https://github.com/ndalezios/clod/blob/master/images/2.png)



