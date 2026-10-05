# File integrity checker
A simple python-based cybersecurity tool that detects file modification using SHA-256 hashing.
## Features
-calculates SHA-256 hash of a file
-saves the original hash as abaseline
-checks the file for unauthorized changes
-detects when file content has been modified
-displays a warning when file integrity changes
## How it works
1. The users enters a file name.
2. The program calculates its SHA-256 has hash.
3. The first hash is saved as a baseline.
4. When the program runs again, if calculates the current hash.
5. If both hashes match, the file is unchanged.
6. If the hashes are different , the program displays:
  "WARNING: FILE MODIFIED!"
## Runs the project
Run: 
. . . bash
python integrity_checker.py
## Example 
Enter file name: test.txt
saved hash:ee8a4575. . .
current hash:f7ae214d. . .
WARNING: FILE MODIFIED!
##cybersecurity concepts
-File integrity monitoring 
-SHA-256 Hashing
-Change detection
-Integrity verification 
-Python file Handling
## Technology Used
.python
.hashlib
.SHA-256
.powershell
.Github
## Purpose
This project was created as a hands-on cybersecurity exercise to demonstrate how cryptographic hashes can be used to detected change to files.




