# **ForceZip**
ForceZip is a brute force password cracker for password protected files in a zip folder, with the capabilities of a simple zip file manager as well. Written in python3, the algorithm is a sequential search with no optimizations, meant as an educational tool to learn how to use the itertools and zipfile standard libraries.

### Getting Started
To use ForceZip, simply place the ForceZip.exe file in the same directory as your target zip file, and run the program. The program will ask you to enter the name of the zip file, select the file you want to crack, and then extract the file to the Desktop after the matching password has been found.

You can also use ForceZip as a simple zip file manager to open and extract specified unprotected files from the zip folder.

### *Caution*
ForceZip exhibits increasingly longer run-times with additional characters in the password it is cracking. ForceZip is recommended to be used for passwords up to 5 characters in length for it to finish executing in a reasonable amount of time.