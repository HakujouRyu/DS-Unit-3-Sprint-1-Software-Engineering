# Part 7 - Questions (and your Answers)

Acme Corporation isn't just a few .py files. If you want to grow in your career here, you'll have to answer the following:

## What, in your opinion, is an important part of code reviews? That is, what is something you pay attention to when you review code, and that you appreciate when others do the same for your code?


### Answer: The thing I look for most is readability. What I mean by that is a number of things, with one of them being following the agreed-upon style guide, which could be PEP8 or a number of others. Another part of readability would be variable names; They must be explicit in their name. A third piece to readability would be comments and docstrings; They must be detailed. Lastly, functions should do one thing well more so than a number of things ok. 


## We have an awful lot of computers here, and it gets pretty confusing with slightly different things running on all of them. How could containers help us improve this situation? Docker can run their own environments they are separate from the operating system.

### Answer: Docker is designed to be stateless. Meaning that so long as you can run Docker, you can run a container of a specific image cleanly and reliably every time, no matter the machine. The container (ideally) has the bare minimum dependencies to be a small package that is easily distributed and deployed over any number of local hosts.