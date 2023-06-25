### comm
The comm command will compare two files already sorted line by line. 
The display consists of three columns: Column 1 depicts the lines found only in the first file,
Column 2 depicts the lines found only in the second file and Column 3 depicts the lines common to both files.

the "comm" command can only be used for data that has already been sorted.

Command Format
`'comm [option] file1 file2'`

For example:
Compare the contents of file1.txt and file2.txt the command is:
`'comm file1.txt file2.txt'`

### diff
the diff command is used to monitor the differences between files.
the diff command is used to monitor the differences between files. 


"diff" is an abbreviation for differential.


Command Format
`'diff [option] file'`

For example:
Display the differences between file1.txt and file2.txt.
the command is:
`'diff file1.txt file2.txt'`

### patch
The patch command is used to apply the changes to a text file. It accepts output from 
the diff program and is usually used to convert older file versions to newer file versions.

Command Format
`'patch [options] patch-file'`

