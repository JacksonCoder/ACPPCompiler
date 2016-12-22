#Introduction
What is A-C++? It stands for Abstracted C++, and it compiles to raw C++. It offers the raw power and low-level features of C++, but also offers the easy-to-read syntax and layout of a high level language. For example this c++ code:

```cpp
std::vector<int> reallybigfunction(const std::vector<int> vector1, const std::vector<int> vector2){
std::vector<int> vectorcopy = vector1;
return vectorcopy;
}
```
Can be written like this in A-C++:
```
reallybigfunction({vector1,vector2}:(const)std::vector<int>)
  vectorcopy = vector1
  return vectorcopy
```
#How to use
Use ```cd Downloads``` and then ```git clone https://github.com/JacksonCoder/ACPPCompiler``` in your OS file browser to clone this repository to your Downloads folder.
Running the program:
Beforehand, make sure to have Python 2.7 installed to run this. Then go into Terminal (or Command Prompt, for Windows users) and type:
```
python Downloads/ACPPCompiler/ACPPCompiler.py
```
or if you are a Windows user:
```
<Path to python interpreter> C:\Downloads\ACPPCompiler\ACPPCompiler.py
```
replacing ```<Path to python interpreter>``` with the path to your python interpreter executable.
#Upcoming changes
0.1 has just been implemented, and can do very basic function/variable declaration parsing.
0.2 is in development, and will probably take about a month.
