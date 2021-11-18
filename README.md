# Object Oriented Programming
## Assignment 1

### Part One


### Survey Links:

_Project 1_

In this project the writer claims that people wait for the elevator for too long, that the time  getting to the destination is too long, and that the electricity usage is rather large.
Therefore, he wants to develop his idea, in which every building has a floor keypad. The passengers choose their destinations and the system assigns them elevators to get into accordingly.

_Project 2_

The writer of this project works in a very tall building with a slow elevator. He claims that on his way up to the penthouse, he can sometimes stop on the floors on the way. He suggests improving the system as follows: when passengers get into the list, they each state the floor they need to get to, and the group unanimously chooses floors to go to, in a way that minimizes the stops. The number of stops is limited to a number k.

_Project 3_

In this project the writers develop and run tests on a number of different algorithms in order to optimize the elevators’ system. In this case, the building has k elevators and i floors, allowing for one passenger to get on at a time. Every elevator has an endless capacity, and so does every floor. The writer’s aim is to find a policy in which, without any relevant preliminary knowledge, an elevator is assigned to each call, so that the waiting time and the time until reaching the destination floor is minimal.

### The problem:
In our project, we are given a csv form containing different elevator calls. Each call consists of source and destination floors, and of the time since the call was made.
We are also given a building. The building holds a number of elevators, and has a minimal and a maximal floor. Each elevator has different given speeds for movement, time of door opening and closing, starting time and stopping time.
Our aim is to assign the optimal elevator to every given call, taking all the data into consideration. We must write whichever algorithms and classes we see fit in order to achieve this.
Unlike in our previous assignment, this time we must write an Offline algorithm. This implies that the algorithm only starts running once it has all of the necessary data beforehand, whereas in our Online algorithm assignment, the algorithm would start before receiving all the floors in the calls list.

### Our Offline Algorithm:
First, we create a class of calls and a class of building, each with the accompanying variables.
We read from the calls file in order to use them. Similarly we did with the json file of the building. 
In the building class we created variables that were used during an algorithm. Such as, min floor, max floor and number of floors. In addition, we created a dictionary for each elevator so that we could also access its variables. We created another array called list to know what the position of each elevator at any given time. Inside the building class we created the elevator class with its variables: id, speed, CloseTime , StartTime, StopTime, OpenTime.

_Ex1 file:_ 

We read from the files of the calls and the building.
We created a two dimensional array, each cell has an elevator and in it all the stations that the elevator goes through. The purpose of this array is to see where the elevator is and what it did in the past to help current call and calculate which elevator is the best.  

_Distance function_

This function calculates the distance between a given floor and elevator.
We get the elevator, its current floor and source floor of the call.
Initially the stop variable can be the number of stops the elevator has passed.
We will create an elevator, and calculate the gap between the source floor and the current floor that the elevator is currently on.
We calculate the CloseTime , StartTime, StopTime, OpenTime times the number of stops the elevator went through, so we know that if the elevator passed through a lot of floors in the past it might be slower than another elevator, and we will connect it with the speed parts gap.
All these calculations help us find the most efficient elevator for our call in all respects.

_Allocate To function_

Initially we run through all the calls. If there is just one elevator - we'll put all the calls in the same elevator.
Otherwise, we create variables source and destination floors and temp variable which symbolizes an elevator index and checks if we have found a better elevator.
We will run in the range of elevators and be divided into cases of up or down:
If the call direction is up:
We will check if the current floor low source, we will check if the specific elevator j is more efficient and good for call than a temp elevator using the dist function and if so we will replace the temp with j.
We will add to stops array of this elevator (elevStops) the source and destination floors.
We will update the current floor of the elevator to be the destination floor and insert for call the elevator temp - i.e. the most efficient elevator for this call.
If the call direction is down:
We will check if the current floor has a higher source, we will check if the specific elevator j is more efficient and good for call than a temp elevator using the dist function and if so we will replace the temp with j.
And again we will do the same process as in the case of up.


At the end of the whole process after we have assigned an elevator for every call, we can write to an file out.csv and see the results and to which elevator each call was sent.




### Project UML Diagram:

<img width="640" alt="UML" src="https://user-images.githubusercontent.com/76524924/142403545-bfd14015-7178-4f2a-aaa2-fe2af01e8aa0.png">


