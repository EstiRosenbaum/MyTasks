### sort
The sort command helps us sort text files and stdin.
Usually, it combines other commands to generate the desired output.
Command Format
`'sort [option] file-name'`

For example:
List the top 10 files by size in the /usr/share/ directory, use it:
`du -s /usr/share/* | sort -nr | head -10`

### uniq
The uniq command is often used in conjunction with the sort command. 
uniq accepts an ordered list of data from standard input or a single file name parameter, 
and by default removes any duplicate rows from the data list.

uniq can only be used for sorted data input, 
so uniq uses either piped or sorted files as input and is always used in conjunction with the sort command in this way.

"uniq" is an abbreviation for unique.

Command Format
`'uniq [option] [file-name]'`

To find out all the common commands in the /bin directory and the /usr/bin directory,
the command is:
`'ls /bin /usr/bin | sort | uniq -d'`


### join
The join command is similar to paste which adds columns to the file, but it uses a unique approach. 
A join operation is usually associated with a relational database in which data from multiple tables sharing common key fields is combined to obtain the desired result. 
This join command does the same thing and it combines data from multiple shared key domain-based files.

Command Format
`'join [option] file1 file2'`

for example:
Using the first field in two files as a match field, connect the two files. 
`'join a.txt b.txt'`