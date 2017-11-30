# Networks_Programming
Tasks: 1. Read in an input file called ‘input.txt’. The input file will contain n lines. Each line is in the format of 5 non-negative integers that the first four are separated by a dot and the last one is separated with a colon, no space is included. Example of such a line is: ‘127.0.0.1:8080’ 2. Create an output file called ‘output.txt’. 3. The first two lines in your output file should be your name and your UIN respectively. 4. For each line you read from the input file, you need to do the following: a. Copy the current line exactly to the output file b. Use the colon as a separator to split the line into two parts: addr, and prt c. If the input line has any error such as: i. Contains less or more than 5 integers ii. Contains inputs are not integers iii. Contains negative integers iv. Dots and Colon are not in right place You generate ‘Error in Input Line’ d. Otherwise, generate another line with following format:  ‘Address:addr, Port:prt’ 5- At the end of the File print a summary containing the number or lines read and number of errors found as shown in the example next. 

Name : Nandith Reddy Malapati    UIN : 01066678

1) Save Prog1.py on any of the directory in the machine. 
2) Open command prompt and change current directory to where the prog1.py exits 
3) Enter "python prog1.py" in the cmd
4) The output.txt file will be generated in the directory of Prog1.py
