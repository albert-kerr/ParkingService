# Design

When approaching this problem, I made the following assumptions:
* You take in all car events at once via a file
* This system can be extendable to include more employees

To optimise the amount of profit we need some type of data structure for
managing the available employees, and the current cars to park. I have decided
to use a priority queue and queue respectively to handle this work.

The priority queue of employees would be sorted based on the commission, so an
available worker would pick the highest commission employee to perform the task.

Since the scale of this task is quite small, I've opted to using simple in-built
queues in Python to achieve this behaviour and used multithreading to achieve
the behaviour of workers.

To simulate the employees being busy, I have used a 3rd queue, so the code
doesn't pick the employee with the highest commission for every car.  

![](images/parking.png)

Future Enhancements:
* Keep track of total profit so far
* Change design to use external workers and task queues instead of in-built data
structures