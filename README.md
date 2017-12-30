# Hashcrack
Cracks hashes using a wordlist/bruteforce. Lots of parameters and options to choose from. Currently supports 14 hash algorithms (including half-hashes) 

# Parameters
Options
+---------+---------------+---------+----------------------------------------+-------------------------------------+---------+-------------------+
| Options |   Alias For   |  Type   |              Description               |               Example               | Default |     Required      |
+---------+---------------+---------+----------------------------------------+-------------------------------------+---------+-------------------+
| -h      | hash          | String  | The hash to break (Do not use with -f) | -h 1d478c2b5b2560c9415b8ca9da92bd6e | None    | Yes unless -f     |
| -f      | hash-file     | File    | File containing hashes to break        | -f hashes.txt                       | None    | Yes unless -h     |
| -t      | type          | Integer | Hash ID (See table below)              | -t 0 (md5)                          | None    | Yes               |
| -w      | wordlist      | File    | Wordlist file (Use if -a is 1)         | -w words.txt                        | None    | Yes if using -a 0 |
| -a      | attack method | Integer | Attack method ID                       | -a 1 (bruteforce)                   | None    | Yes               |
| -b      | bounds        | Range   | Min/Max hash length (before hashing)   | -b 0,10                             | 0,10    | No                |
| -o      | output        | File    | Outputs the cracked hash/hashes        | -o cracked.txt                      | None    | No                |
| -g      | show          | Boolean | Show hash attempts live                | -g True                             | False   | No                |
| --h     | help          | None    | Returns help page                      | --h                                 | N/A     | N/A               |
+---------+---------------+---------+----------------------------------------+-------------------------------------+---------+-------------------+

Required parameters: These parameters are required in order for this program to work

-h | -f : A hash is required otherwise it's cracking nothing.
-a : An attack method is required otherwise it won't know what to do.
-t : The algorithm used is required otherwise a lot of guessing is involved.
-w : A wordlist is needed otherwise you're not declaring anything to try. ONLY APPLIES IF -a 1
-b : Bounds are required otherwise you'll end up cracking an 8-bit password using range 1-256. ONLY APPLIES IF -a 0


Recommended: These parameters are recommended for the program to fulfil its function better.
-o if using a hash file : Gonna be hard to scroll up and see all those cracked hashes, easier to output it to a file.

Banned: These parameters can not work together.
-w & -a 0
-b & -a 1

Hash IDs
+----+---------------------+-----------+
| ID |       Name          | Category  |
+----+---------------------+-----------+
|  0 | MD5                 | Raw Hash  |
|  1 | SHA1                | Raw Hash  |
|  2 | SHA224              | Raw Hash  |
|  3 | SHA256              | Raw Hash  |
|  4 | SHA512              | Raw Hash  |
|  5 | Half-MD5 (left)     | Half Hash |
|  6 | Half-SHA1 (left)    | Half Hash |
|  7 | Half-SHA224 (left)  | Half Hash |
|  8 | Half-SHA256 (left)  | Half Hash |
|  9 | Half-SHA512 (left)  | Half Hash |
| 10 | Half-MD5 (right)    | Half Hash |
| 11 | Half-SHA1 (right)   | Half Hash |
| 12 | Half-SHA224 (right) | Half Hash |
| 13 | Half-SHA256 (right) | Half Hash |
| 14 | Half-SHA512 (right) | Half Hash |
+----+---------------------+-----------+

Attack Modes
+----+--------------------+-----------------------------------------------------------+---------------------+----------------+-------------+
| ID |       Method       |                        Description                        |    Requirements     | Example Output |   Status    |
+----+--------------------+-----------------------------------------------------------+---------------------+----------------+-------------+
|  0 | Bruteforce         | Tries various psuedo-random combinations                  | Min/Max hash length | ifnstbasf      | Available   |
|  1 | Straight           | Dictionary attack.                                        | Wordlist file       | apple          | Available   |
|  2 | Reverse-Bruteforce | Tries first instance in wordlistagainst each hash in file | Min/Max hash length | ifnstbasf      | Coming Soon |
+----+--------------------+-----------------------------------------------------------+---------------------+----------------+-------------+
