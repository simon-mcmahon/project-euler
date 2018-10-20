# Project Euler Repository

Project Euler is a website dedicated to the presentation of intriguing problems which combine mathematical insight and computer coding. It provides a system where people can make an account, attempt the problem and try and submit a solution.

The purpose of this repository is to showcase the code I have written for Project Euler over the years. Note that some of it was written a **LONG** time ago and so the code may be a bit rough in places and not use the best variable naming or code conventions.

My user name was **thingamabob** and I have solved 84 of 638 problems (as of 20/10/2018).  

![Project Euler Profile](https://projecteuler.net/profile/thingamabob.png)

# Requirements and Setup

To play around with this repository, use the command:

`git clone https://github.com/simon-mcmahon/project-euler.git` in the directory you wish to copy the files.

Scripts inside the **progress_2015-2016 filder use **python 2.7**.  **Python 3.X** is used elsewhere.

Note that some problems in **progress_2018** depend on text files containing primes sourced from [here](http://www.primos.mat.br/2T_en.html).

External libraries are sometimes required, look at the script and install before use.

## Understanding the directories

| Directory or Sub-Directory | Purpose |
| :--- | :--- |
|progress_2015-2016 | Contains all of the python code written before 2016. Will definitely require python 2.7 to run. |
|   ⟶ incomplete | Home to the work in progress python scripts which I did not get around to completing. |
|   ⟶ [number] | My solution to some problems such as 22 or 42 required multiple .py files so these have their own sub-folder.|
|   ⟶ [number].py | The python code which solves the relevent Project Euler problem either by printing the correct answer or defining a variable equals it. |
|progress_2018 | Folder containing all problems attempted in or after the year 2018. |
|   ⟶ incomplete | Home to the work in progress python scripts which I did not get around to completing. |
|   ⟶ primes | Folder containing list of extracted txt files each containing 10 million primes for certain problems. Found (here)[http://www.primos.mat.br/2T_en.html	]  |
|   ⟶ [number].py | The python code which solves the relevent Project Euler problem either by printing the correct answer or defining a variable equals it. |
