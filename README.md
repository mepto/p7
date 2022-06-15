AlgoInvest&Trade - Find the best wallet
=======================================

How to install
--------------

1. Clone this repo on your local machine

`git clone https://github.com/mepto/p4.git`

2. Make sure you use python 3.9. Check your python version:

`python --version`

3. Create and activate your virtual environment. The methodology below uses 
   the venv module but you may use your favorite virtual environment instead.
* Creation from project root:

`python -m venv <your-virtual-env-name>` 
 
* Activation in Windows:

`<your-virtual-env-name>\Scripts\activate.bat`

* Activation in Linux:

`source <your-virtual-env-name>/bin/activate`

4. Requirements

You only need to install the requirements if you wish to update the project. 
Requirements do not need to be installed if you wish to use the project as is.

5Launch either the Bruteforce of the Optimised wallet search script. 

From the directory root, in your terminal launch the following command from 
the project root, where <algo_choice> is either 'optimized' or 'bruteforce' 
and <full_path_to_csv_file> is, well, the full path to the csv file you wish 
to use:

`python -m <algo_choice> <full_path_to_csv_file>`
