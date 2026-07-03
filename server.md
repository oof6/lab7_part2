### What the Server Does? 

The server has two functions/tools it can call: 
- `list_notes` which lists the note files that are available to be read 
- `read_notes` reads a note from the notes directory

# What Vulnerability Class We Planted? 

We made the server vulnerable to path traversal. This is something that could be a realistic developer mistake because it can be easy to forget that pathlib naturally allows and evaluates `../` sequences in paths. This is caused by not checking to make sure the path stays within the sandbox/is allowed after resolving the path. The fix is to resolve the path and then check if it is a permitted path to take.
