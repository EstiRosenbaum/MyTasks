### which
the which command is used to search the executable files location in the path specified by the PATH variable.

Command Format
which[executable-file-name]

For Example:To confirm whether gcc is installed :
`which gcc` -return the path to the gcc program.


### whereis
The whereis command is mainly used to locate the executable file, source code file, and help file in the file system.

Command Format
whereis [options] file


For Example:
Search for the path to the gcc executable. You can use the following command:
return `whereis -b gcc`
