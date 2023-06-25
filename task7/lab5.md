### find
The main function of the find command is to traverse down the file hierarchy, 
match the files that meet the conditions, and perform the corresponding operations.

Command Format
find option [expression]

For example:
To print a list of files/directories in the current directory, use the following command: (Only the first 10 rows are displayed.)
`find . -print | head -10`

  Print all the file names ending in .txt in the current directory. You can use the following command:
  `find . -name "*.txt" -print | head -10`


### xargs
The "xargs" command can receiveinput from standard input andconvert that to a specific parameterlist.
Command Format
`command | xargs [Options] command`


For example:
To convert multi-line input to single-line output can use the following command:
`cat a.txt | xargs`
