# A-CPPCompiler
What the heck is A-C++? It stands for Abstracted C++, and it compiles to raw C++. It offers the raw power and low-level features of C++, but also offers the easy-to-read syntax and layout of a high level language. For example this c++ code:

std::vector\<int\> reallybigfunction(const std::vector\<int\> vector1, const std::vector\<int\> vector2){
std::vector\<int\> vectorcopy = vector1
return vectorcopy

Can be written like this in A-C++:

reallybigfunction({vector1,vector2}:(const)std::vector\<int\>)
  vectorcopy = vector1
  return vectorcopy
This language is very early in its development. The current python file will turn a line of A-C++ to C++, and it currently only translates variable and function declarations. If my source code is readible to you, feel free to contribute... that's always appreciated!
