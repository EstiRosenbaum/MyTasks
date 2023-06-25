### df

The function of the df command in Linux is to check the disk space usage of the file system.

"df" is an acronym for disk free.

Command Format
`'df [option] file'`

For example :
To display the disk usage in incode mode, use this command:
`df -i`


### du
The du command is used to view the space used by files and directories on a disk.

"du" is an acronym for disk usage.


Command Format
``'du [option] file'`

For example:
1.Display the space occupied by the specified file and display it in a format that is easy to read. 
use this command:
`'du -h file1.txt'`

2.To sort the display in reverse order according to the space size,
use this command:

`'du -h | sort -nr | head -10'`



### time
The time command is often used to measure the running time of a command, including the actual time, the processing time spent in user mode, and the processing time spent in kernel mode.

Command Format
`'time command'`

For example:
To measure the running time of the date command,
use it:
`'time date'`
