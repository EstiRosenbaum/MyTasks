### cut
The cut command is a gadget that splits the text into columns, and it can specify the delimiter that separates the columns in its output.

Command Format
`'cut [option] file-name'`
For example:
To extract the first and the third columns in the student.txt file, 
the command is:
`'cut -f 1,3 -d ' ' student.txt'`


### paste
The function of the paste command is exactly the opposite of cut.
It adds one or moretext columns to afile. It readsmultiple files andthen combines thefields in the filesinto a single textstream that is inputto the standard output.
Command Format
` 'paste [option] file-name' `


For example:
To splice the contents of student.txt and telphone.txt files by column, the command is:
`'paste student.txt telphone.txt'`

### tr

The tr command is often used to change characters. 
is is the same "search and replace" operation.

tr can read only from stdin (standard input) and cannot accept input via command-line arguments.
"tr" is the abbreviation for translate.

Command Format
`tr [options] SET1 SET2`


For example:
To convert the input characters to lowercase, the command is:
`'echo 'THIS IS LABEX!' | tr 'A-Z' 'a-z' '`