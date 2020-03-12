# Quantum-Random-Number-Generator-Simulation
⚛ A random number generator and Visualizer that generates true random numbers (theoritically) by simulating a Qunatum Sysem and plots live graph of the numbers generated. The alogrithm is based on the core concept of superposition and its uncertainity.

## 👨‍🏫 Physics Alert!
This qunatum algorithm is based upon the core idea of **Werner Heisenberg Uncertainty Principle** and **Quantum Superposition**. The value of a qubit in a bloch sphere model is determined to be in the eigenstates of **|0>** or **|1>** based upon its position along the **z-axis** and **|+>** or **|->** based upon its positoin in **x-axis**. According to the uncertainity principle if we measure the qubit along the x-axis the state of the qubit along the z-axis goes in the superposition. In this algorithm the qubit was initially |0> i.e. its value along the z-axis was certain. I then applied the **Hadamard Gate** which performed matrix operation upon the qubit to perform a rotation of ⫪ radian along the z-axis and ⫪/2 radian along y-axis. This operation projects the qubit on the x plane which puts it in a superposition along the other two axises. The effect of Hadamard gate on a qubit can be formalized as:

![hadamard gate on |0>](https://latex.codecogs.com/gif.latex?H|0>=\frac{|0>&plus;|1>}{\sqrt{2}})

![hadamard gate on |1>](https://latex.codecogs.com/gif.latex?H|1>=\frac{|0>-|1>}{\sqrt{2}})

This gives you a qubit that will have the unbiased equal probability of getting |0> and |1> at a particular time. We then applied a **measurement gate** to the qubit that would perform a wave function collapse along the z-axis and result into either of the eigen states i.e. |0> or |1>.

___

# 🛠 Requirements
The script is written in **Q#** and **Python** and uses Microsoft **Quantum Development Kit** and thus to run the script you need to have few packages, softwares and frameworks installed. The steps to install all requirements are listed below:

+ ## Python 3
   In order to execute the script you need have python installed and configured in your system environment variables. You can download Python from [**here**](https://www.python.org/downloads/)

+ ## PIP
   It is a python package manager, you would need it to install and manage required packages. If you are using python 2 or latest it should come preinstalled else you can get it from [**here**](https://pip.pypa.io/en/stable/installing/)
   
+ ## .NET Core
   You need to have .NET Core installed and running on your system as it is required for building and executing apps and scripts written using the QDK. You can download .NET Core from [**here**](https://dotnet.microsoft.com/download)
   
+ ## QSharp
   QSharp a Python package that enables interop between Q# and Python. It need to be installed in the current environemt you are working upon. To install using pip open terminal and type the following command:
   #### `pip install qsharp`
   
+ ## IQSharp
   Install iqsharp, a kernel used by Jupyter and Python that provides the core functionality for compiling and executing Q# operations. To install IQSharp you need to have .NET Core installed and running on your system. Use the following commands in the terminal to install IDSharp:
   #### `dotnet tool install -g Microsoft.Quantum.IQSharp`
   #### `dotnet iqsharp install`
   
+ ## Matplotlib
   Matplotlib is a python package that enables us in plotting and rendering visual graphs with lots of customiziblity and flexibility. We would use it to plot realtime graph of the numbers generated. To install matplotlib run the following command:
   #### `pip install matplotlib`
   
> If you use Visual Studio Code for using Q# you can install the [QDK extension for VS Code](https://marketplace.visualstudio.com/items?itemName=quantum.quantum-devkit-vscode)

___
# 🏃‍♂️ Run
The repository has two files:
+ **generator.py**: This script generates the random numbers by simulating a quantum system and logs them in the **log.txt** file.
+ **liveplot.py**: This script monitors and plots the data in the **log.txt** file after every fixed interval of time.

To start generating and visualization, run the **generator.py** and then the **liveplot.py**. To change the rate of generation of numbers you can change the sleep time in the generator.py accordingly and to change the refesh rate in the graph you can change the interval time in the liveplot.py.

## **❤ Support**
If you like my work, a bit of contribution would motivate me a lot for more open source contributions.

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/amannirala13)

*Please support the work:*
 - [Follow on **Github**](https://github.com/amannirala13)
 - [Follow on **LinkedIn**](https://www.linkedin.com/in/amannirala13/)
 - [Follow on **Twitter**](https://twitter.com/AmanNirala13)
 - [Follow on **Instagram**](https://www.instagram.com/amannirala13/)
 - [Follow on **HackerRank**](https://www.hackerrank.com/amannirala13)
