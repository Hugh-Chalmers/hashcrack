# Hashcrack
Cracks hashes using a wordlist/bruteforce. Lots of parameters and options to choose from. Currently supports 14 hash algorithms (including half-hashes) 

# Parameters
Options
Presented in a nice table over at (https://pastebin.com/raw/sBTHEaVg) this table will break if your monitor is too small. Simple version of the table below:

-h : Takes the hash from the user. : -h 1d478c2b5b2560c9415b8ca9da92bd6e  
-f : Takes a file containing hashes. Alternative to -h : -f hashes.txt  
-t : Lists the ID of the hash (0 for MD5) : -t 0  
-w : Takes a wordlist file to be used for -a 1 : -w words.txt  
-a : Takes the attack method ID (0 for bruteforce) : -a 0  
-b : Takes bounds to be used in bruteforce attack : -b 2,50  
-o : Takes file to output cracked hashes to : -o cracked.txt  
-g : Decide whether or not to output attempted hashes : -g true  

# Usage
The parameters can be written in any order, rather than passing them with the filename, you can run the file then enter them from there.
