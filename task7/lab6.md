### wc
The wc command is a statistical tool that is used to display the number of lines, words, and bytes contained in a file.
"wc" is an abbreviation for word count.

Command Format
`wc [option] file`
For example:
Count the number of lines of a file. the command is:
`wc -l c.txt `

To count the number of command files in the /bin directory, the command is:
`ls /bin | wc -l`


### grep
grep is a very powerful command for finding matching text in a file, accepting regular expressions and wildcards,
and using multiple grep commandoptions to generate output in variousformats.

Command Format
`grep [options] pattern [file]`

For example:
Take out the line corresponding to the root user in the /etc/passwd file and add the color to the keyword. the command is:
`grep "root" /etc/passwd --color=auto
cat /etc/passwd | grep "root" --color=auto`


### Regular Expressions
A regular expression is a symbolic representation that is used to identify text patterns.

Regular expression metacharacters consist of the following characters:

^ $ . [ ] { } - ? * + ( ) | \

Used to:
Examplse:
`^`: Line start marker.
`$`: End-of-line marker.
`.`: Match any character.
`[ ]`: Match any character contained in [Character].

`[^ ]`: Match any character except the characters in [^character].

