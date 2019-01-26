Coding-Challenge README.txt
Hayden Lalljie
January 25, 2019

Coding-Challenge consists of two problems separated in to two separate Eclipse Pydev projects.

If you already have Eclipse with Pydev and have python-Selenium installed you can import the project directly into that enviroment to run.
If not here are the steps to take to run the programs:

  The most simple way to run these programs requires only python, Selenium for python, firefox and geckodriver(for firefox).
  1. First Download python from https://www.python.org/downloads/
  2. Then dowload Selenium for python tutorial here: https://selenium-python.readthedocs.io/installation.html and below
    2a. Run "pip install selenium" from the command line
    2b. Install geckodriver from https://github.com/mozilla/geckodriver/releases
  3. Run the main files of each project seperately.
  
Outward_Coding_Challenge
1. Testing Search functionality works as intended
Runtime ≈ 26 seconds.
Output:
2613243 is an invalid sku.
123456 is an invalid sku.
Notes: 
-First run might produce two invalid results due to lag in importing. 
-Screenshot of failed test will be in project directory unless otherwise specified.

Outward_Coding_Challenge
1. Testing Search functionality works as intended
Runtime ≈ 30 seconds.
Output:
Selecting Arizona in the Store locator gave 2 results.
Selecting Texas in the Store locator gave 8 results.
Notes:
-If you already have a default location profile for Selenium in Firefox you may need to turn it off for the program to work correctly.
