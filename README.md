# Summative Task

## Overall goal

My summative task will be a combination of physics and software curriculums. The project will be a simulation of a rocket launching off of an earth-like planet, with the same radius and mass, but with no atmosphere.

## Sub-goals

* Accurately calculates the velocity, acceleration, and position vectors of a rocket, as it takes off
* Displays that data graphically, over time.

# Installing
## Mac
* In terminal run this command:
* `pip install rosshill-physics`
* If that doesn't work, make sure Python is installed by running `python -v` in terminal.
* If Python is not installed, download it here: https://www.python.org/downloads/release/python-2711/

# Usage
## Mac
* In terminal, enter: `physics`

# Reflection
* What (if anything – although there is probably at least something) does the user need to know about what your program does?

Rocket's can be tricky to simulate, in that if the values the user input aren't within a small margin of error, the rocket could easily crash into the ground. As such, it can take some trial and error to find values that work.

* What (if anything) does the user need to know to operate your program (keystrokes, et cetera)?

Once installed, type `physics` into the terminal. The rest is fairly self-explanitory. As of right now, the colored text output is only compatible with OS X.

* How does your program show evidence of your understanding of object-oriented programming concepts like encapsulation and inheritance?

My code is held in three different files, with the two classes "rocket" and "graph", which hold the functions for calculating the rocket's vectors, and graphing those vectors, respectively.

* What evidence can you provide that your program is human-readable?

[These lines](https://github.com/Rosshill98/summative-task/blob/master/physics/rocket.py#L25-L40) are one example of code that has been very broken-down using piece-wise refinement, such that each function performs one specific calculation.

* For example, where have you used: descriptive function names, meaningful variable names, comments that describe the intention of a block of code

[This function](https://github.com/Rosshill98/summative-task/blob/master/physics/rocket.py#L29-L34) has a descriptive function name, with comments for each line because I thought it might be confusing for someone unfamiliar with physics.

* What is the most important algorithm, or algorithm(s), in your program? That is, where is the "core idea" of your program? Explain how this works.

The algorithm I used was the incrementation of time, and that time being passed to various functions which returns a value given time. For instance, the velocity function is passed time, and the velocity changes depending on the time that is passed.

* How have you made your program easy to use?

It is now a self-contained program, which can be easily installed using Python's package manager, "Pip". It has very human-readable prompts for the user, to get the rocket's specification.

* How have you made correct use of source control?
For example, show that you have:
    made frequent commits
    kept commits "atomic" (i.e.: one accomplishment per commit, rather than a batch of things all committed at once)
    descriptive commit message
    
    [Here](b49969a536a1e328e351db1975b52147788c31e2) is an example of a commit which achieved a single task, with a descriptive commit message. Looking through my commits, you can see that I have been committing consistantly over the course of this project, and my commit messages are accurate and descriptive.
