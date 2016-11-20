# A-CPPCompiler
What the heck is A-C++? It stands for Abstracted C++, and it compiles to raw C++. It offers the raw power and low-level features of C++, but also offers the easy-to-read syntax and layout of a high level language. For example this c++ code:

std::vector\<int\> some_array;

Can be written like this in A-C++:

array-\>int some_array

This language is very early in its development. The current python file will turn a line of A-C++ to C++, and it currently only translates variable declarations. If my source code is readible to you, feel free to contribute... that's always appreciated!
And make sure you download the "parse" library before you run this, or you will not be able to execute the script properly.
(Eventually, I will bundle the parse library files with this repository)
