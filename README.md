# Air Quality Office Explore

This is a total pleasure project to play with a few environmental sensors in my office to just collect data, learn about robotics/sensors, and be nerdy about stats.

What I have so far.
- python file on a raspberry pi that
  - reads the sensors
  - appends data to a data log csv
- a .sh file that
  - searches the wifi network for a raspberry pi
  - copies the data log to the laptop
  - runs the "analysis" python script on the local machine
  - displays a CLI graph of the past weeks CO2 measurements
- an analysis python script
  - reads in datalog from the raspberry pi through the .sh file
  - generates some stats from the file
  - creates a CLI graph

Things I want to implement.
- store the data in a database on AWS
- work on field naming conventions in the csv
- add in temperature


References:
For wiring up the devices these websites were useful:

https://pinout.xyz/

https://www.circuits.dk/testing-mh-z19-ndir-co2-sensor-module/

https://learn.adafruit.com/adafruit-tsl2591/python-circuitpython