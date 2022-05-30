# ParseDBLP_with_SimpleCode
Parse and extract value / contents of 3.3 GB DBLP dataset (https://dblp.uni-trier.de/xml) using only 70 lines of python code

# requirement

The lib of xml.etree.ElementTree is needed.

# The motivation of this code

The DBLP dataset is 3.3GB. So we will meet out of memory problem if we use an ordinary way to parse the dataset, which reads all data to the memory then parse the data.
Our solution is to use "iterparse" that reads and parse /extract the xml file line by line without having the aforemention problem.

# Challenge
It is difficult to know which line is the end for a TAG tree if reading the file line by line. Our solution is to use a stack data structure. More details can be found from the code comments. 

# Before the parse:
![image](https://user-images.githubusercontent.com/14246364/170906527-00724c5f-8f1c-40a3-a4c8-7661ed415ae2.png)

# Execution result:

![image](https://user-images.githubusercontent.com/14246364/170906588-3b43e6eb-c052-4c2f-a7e4-154636e0c293.png)

