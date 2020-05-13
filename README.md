# BooleanEsolang
My own Esolang Interpreter, Write the code in the provided file Test.bb

I've started to work with Esolangs and made my own sort of glued-together one, The premise is simple, Go into the
'Test.bb' you can rename this as long as you update it in main.py.
The python file executes your Bool-Brain code as follows:
[ Start of a loop
] End of a loop
+ inverts the state of a current bit, bits can only be 1 or 0
> moves the pointer to the right
< moves the pointer to the left
, gets user input 1 or 0 and stores it in current bit
. outputs selected bit's value 1 or 0

Loops will continue until they hit a ] and the selected bit is a 0
I have the RAM/Memory print out in 8-bit segments at the end, this can be commented out, it's the last line of python code

You can make imbedded loops ie,

[>[<]]
I am curious if you could write a program that fills the RAM with 1s, too easy? Alternate 1s and 0s! Submit your solutions in the comments!
Feel free to add debugging!
