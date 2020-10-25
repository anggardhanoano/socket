# Client Worker Nodes

client worker node based on python with socket programming.

## How It works

the worker contains of 4 threads that ready to accept task from client. every task that client gives, will immedieatly assigned to worker via load balancer(own implemented). right now only 4 unique task that worker can do. but it's very possible to add more task in the future. just add more task in etc/task.py and register it in etc/threads.py

## How To Run

just run the inquirer.py, and the cli will guide you :). don't forget to assign the ip and port of your workers in client.py
