#Exam Questions <img src="../../Resources/exam.png" width=50px alt="Tick Sheet">

##Instructions
Edit this document and answer the questions in the sections surrounded by ```.

There are 30 marks available and are awarded grades as follows:

|Score|Grade|
|-----|-----|
|<6|U|
|6+|G|
|9+|F|
|12+|E|
|15+|D|
|18+|C|
|21+|B|
|24+|A|
|27+|A*|


##Data Representation

###1 - Why do we represent data using binary when using computers *(1 mark)*

```
Computers can only understand binary to run commands.
```
###2 - How would we represent the number 147 in binary? *(1 mark)*
```
10010011
```
###3 - Can you convert the hexadecimal number **b5** to denary, there is a mark for you working. *(2 marks)*
```
b5
1011 0101
181
```
###4 - Here is a function written is **pseudocode**.
```
FUNCTION validUser (users , user)
    FOR x <-1 to LEN(users)
        IF users[x] = user
			RETURN True
		ENDIF
	ENDFOR
	RETURN False
ENDFUNCTION
```

(a) What type of data is **users**? **(1 mark)**
```
The data type of users is an array
```

(b) What type of data is returned by this function? **(1 mark)**
```
The type of data returned by the function is boolean
```

##Errors
###6 - This program is supposed to find the mean of a list of numbers and print it out for the user:
```
line1:		tot <- 0
line2:		nums <- [1,6,4,2,5,3]
line3:		FOR x <- to LEN(nums)
line4:			tot <- nums[x]
line5:		ENDFOR
line6:		mean <- tot
line7:		OUTPT mean
```

(a) On which line is there a **syntax** error? **(1 mark)**
```
Line 7
```

(b) What is meant by a **syntax** error? **(1 mark)**
```
A syntax error is where the computer cannot understand the code, usually due to a misspelt keyword
```

(c) Identify a logical error in the program and suggest how this might be fixed. **(2 marks)**
```
The for loop is itterating through the list of numbers, but instead of adding the number to the total, the program sets the value of tot to the current number in the itteration
```

(d) Describe and give an example of the 3rd kind of programming error. **(2 marks)**
```
An arithmetic error is where the programmer asks the computer to do a taks which is impossible for a computer to do
```

##Algortithms
###7 - Write an **algorithm** that if given a list of numbers could find the largest. Try to use [pseudocode](http://filestore2.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF).
```
numbers <- [53,8,23,63,85,9,12,98,2,87,96]
highest <- 0
for x <- 1 to len(numbers) DO
	IF numbers[x] > highest THEN
		highest <- numbers[x]
OUTPUT "The highest number is " + highest
```

##Networking
###8 - Research the following methods (*topologies*) for connecting devices to a network. In each case give a description and at least 1 advantage and 1 disadvantage.

**Bus Topology (6 marks)**
```
Describe:
The bus topology involves all the computers, printers, scanners, and the server connecting to one main 'bus' cable.  At either end of the bus are Terminators which prevent the signal from being reflected back down the cable.

Advantages:
• Easy to install.
• Cheap to install becuase not a lot of cabling is required.

Disadvantages:
• If the bus cable fails to function, the whole network effectively stops working.
• An addition of more nodes will affect the performance of the network - it will become slower due to data collisions.
• Because all of the nodes can see all of the data, there is little security in a bus topology.
```

**Ring Topology (6 marks)**
```
Describe:
In a ring topology, each device is connected to two other devices, with all the devices in a ring formation.  Each packet of data on the network travels in a single direction, and each device recieves the packet and passes it on until it reaches its destination.

Advantages:
• Can transfer data quickly, even if there are a large number of devices on the network.  This is becuase the data packet only travels in a single direction, so there are no data collisions.

Disadvantages:
• If a single device becomes faulty and does not function, the whole network will effectively stop working.
• If the main cable becomes faulty and does not function, the whole network effectively stops working.
```

**Star Topology (6 marks)**
```
Describe:
The star topology involves each device on the network having its own cable to a device known as a switch or hub - a switch only sends a packet of data to the destination device, whereas a hub sends every packet of data to every device

Advantages:
• Very reliable because if one of the cables or devices fails to function, the rest of the devices are unaffected (unless the faulty cable is the one going to the server, or the faulty device is the server).
• High performance, becuase no data collisions occur.

Disadvantages:
• Uses the most cabling out of the three topologies, so is the most expensive to install, due to the cost of cabling.
• Hubs or switches are required, so the network costs extra money when compared to a topology with no switch or hub.
• If a hub or switch fails to function, none of the devices on the network will be able to communicate becuase the switch or hub is the centre of the network.
```
