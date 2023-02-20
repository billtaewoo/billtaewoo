Thank you for reading this file.
Author of this program is TAEWOO LEE (s1711673) and I note a few important information
before you running my code.
--------------------------------------------------------------------------------------------------
1. The simulation must run with specific order.
	This is very important, becasue it would break the simulation if you didn't follow it.
	First, check if any txt files except 'bodies.csv' and 'README.txt' exists. If you found them
	please delete them before running simulation. This is because this codes are not
	designed to overwrite the already existing data stored. This is all becasue my inexpertness.

2. The simulation file is called 'Simulation_final.py'. Please run it FIRST. the other files won't 
work unless you run the simulation first, becasue there are no stored data to use.

3. If animation stuttered/lagged/stopped/not played delete the current kernel. Because of my
in expertness, the code is quite heavy than it looks. If there are so many caches exists in your
kernel, my animation may not work properly.

4. This code is made and expected to run on the Spyder. Please update the Spyder if you run
this code on the Spyder; since I wrote this code on very new version of the Spyder.

5. Energy_simulation.py is the stand-alone program for ploting total energy against time. 
Make sure that 'energy.txt' is formed before run this file.

6. Journey_time_and_the_closest_distance.py is the stand-alone program to calculate the
minimum distance between Mars and satellite. Please make sure you check that 
distance_diff.txt is generated before run this code.

7. Planets.py is object class code, which is crucial for storing values for simulation. please 
do not modify or delete it.

8. Orbital period will stored in form of txt file named 'period.txt'. the period is written in 
order of Mercury, Venus, Earth, Mars and units are in Earth Year.

9. 'Simulation_expected_values.zip' is an example file that has been produced my test.
If you like to compare the simulation ran in your computer to my simulation. Feel free to 
use it.

Thanks for reading.

Sincerely, 
TAEWOO LEE