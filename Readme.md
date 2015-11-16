Airport Challenge in Python
=================

Introduction
---------
In Week 1 of the Makers Academy Course, a challenge is issued to model and airport in Ruby. This Repo aims to do just that but in Python instead. Click [here](https://github.com/jonathansayer/airport_challenge) to see the ruby version.

The user stories are as follows:

```
As a pilot
So that I can arrive at my specified destination
I would like to land my plane at the appropriate airport

As a pilot
So that I can set off for my specified destination
I would like to be able to take off from the appropriate airport

As an air traffic controller
So that I can avoid collisions
I want to be able to prevent airplanes landing when the airport if full

As an air traffic controller
So that I can avoid accidents
I want to be able to prevent airplanes landing when the weather is stormy
```

How I Tackled the Challenge
-------
The first step was to learnt the python specific testing suites. For this challenge I used the unittest suite. Once I had mastered the testing suite, I firstly developed the plane class. This is a simple class which knows if the plane is flying or not. The airport class was next which would land a plane, store it and then release it again, depending on the weather. The weather class was developed last. The class generates a random number which determines the weather.

Difficulties
-----
This is my first ever Python program, so the first challenge was to learn the language. As I have a good understanding of Ruby and OO principles, this was relatively straight forward.
The real difficulty, when learning a new language, comes when using the test suites.

Unittest syntax is completely different to rspec. Stubbing took a little bit of time to understand in unittest and dealing with random number generators is still a little bit of puzzle for me.

How to use the Program
-----
Once the repo has been cloned you can run the program in the python shell.

```
$ from plane import Plane
$ from airport import Airport
$ from weather import Weather
```

This will import all the classes from the relevant files.

```
$ heathrow = Airport()
$ jet = Plane()
```

This will create instances of their respective classes.

Planes are initialised flying (in the air), the following functions can now be used:

```
2.2.1 :004 > heathrow.land_plane(jet)  #lands a plane at the airport.
2.2.1 :005 > heathrow.planes  #returns all planes currently stored at the airport.
2.2.1 :006 > heathrow.capacity  #returns the capacity of the airport.(20)
2.2.1 :007 > heathrow.release_plane(jet)  #releases the plane which has been passed as an argument.
```
On occasion a storm may take hold making in impossible for an airport to take in any more planes

```
2.2.1 :008 > heathrow.land_plane jet
      => "The storm has made it impossible to land"  
```
If a storm is in town, planes cannot take off.

To run the tests, choose the test file and run using python, for example:

```
$ python airport_unittest.py
```
