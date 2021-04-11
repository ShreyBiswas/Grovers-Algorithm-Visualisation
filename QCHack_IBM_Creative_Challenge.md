## QCHack: IBM Creative Challenge

The project was created to assist with visualisations of Grover's Algorithm.

Grover's Algorithm uses destructive interference to decrease the probability of measuring incorrect qubit states, and constructive interference to increase the probability of measuring correctly. It uses Amplitude Amplification to do this, but the process can be difficult to visually imagine, and gain an intuition for. 

When writing [a guide to Grover's Algorithm](https://medium.com/quantum-untangled/grovers-algorithm-mathematics-circuits-and-code-quantum-algorithms-untangled-c4aa47d506e5), I previously used Manim to illustrate Amplitude Amplification. However, this project for QCHack is less abstract, though more visually appealing. This makes it much more intuitive, and easier to understand, as well as fairly interesting to observe.

The project can assist in illustrating Amplitude Amplification - the Rose Chart is especially strong at showing how one state is amplified, while all others are suppressed. Additionally, as it links each step of the process to an Oracle + Diffuser pass, it can clearly show the relationship between the number of passes and the probabilities of the states. The project - after more development if needed - can assist in giving newcomers to Quantum Computing a strong intution for Grover's Algorithm, and the use of interference in Amplitude Amplification.

# Algorithm Simulation
The circuit simulating Grover's Algorithm is created using Qiskit, in `src/grover_algorithm.py`. The program randomly generates a bit-string which will be the 'correct' qubit state. It creates an Oracle and Diffusion Operator for that bit-string, roughly calculates how many steps of Amplitude Amplification are needed to obtain a satisfying result, and constructs a circuit to carry out the process.

The program constructs several circuits for each pass of the Oracle and Diffuser, and runs them through Qiskit Aer's Statevector-Simulator. The resulting statevector is retrieved, and the latter half is saved; since the Output bit is considered part of the statevector, the only difference between the first and second halves of the statevector are the Output bit. As it would usually be discarded, we can take either half for our purposes.

Feel free to change certain parameters in the algorithm's code itself - for example, `n=7` on Line 71 represents the number of qubits used to Query the Oracle. This can be changed freely - though since the simulation is classical, high values of `n` may take longer to calculate.


# Issues Faced
Mapping the statevector onto the Rose Chart and Bar Graph was difficult to perform, due to multiple reasons. 
 - For one, the statevector included complex numbers, which could not be easily mapped to the diagrams. Initially, I solved this by taking the modulus of the complex number. 
 - The next issue was that the statevector described probability amplitudes, which can be positive or negative - to find the probability, I would need to square the probability amplitudes. On doing so, I discovered an issue with scale; squaring small probability amplitudes resulted in incredibly small probabilities, which were indistinguishable on the graph. So, instead of squaring the numbers, I took their absolute value instead with `abs()`. Though technically inaccurate, it results in a much clearer visualisation, along with automatically finding the modulus of any complex numbers.
 
Dealing with the Output Qubit in the statevector was in response to noticing the bug as it was shown. 
 - Firstly, the number of points on both the Rose Chart and Bar Graph was twice as much as I had calculated, and in both cases I had two correct results emerge, rather than one. However, the Rose Chart always displayed them to be 180 degrees away, and they were also a constant distance apart on the Bar Graph. 
 - This led me to realise that a single qubit (the most significant) was all that differed between the two. Realising that this was the Output bit randomly collapsing to '0' or '1' from superposition, I found that it caused the entire statevector to be duplicated. To combat this, I only took the latter half ot the statevector, where the Output bit is constant - and so can be ignored.

I originally had planned to include the Oracle's effect on the statevector - flipping the correct state to a negative value. However, in practice, this ended up being worse for the visualisation - in the Rose Chart, it would flip from one side of the circle to another, and become obscured by the qubit states already there. 
 - To stop this, the only solution was to remove the feature entirely. Displaying the function of the Oracle on the Rose Chart would take away from the visualisation, rather than contributing any understanding.
 - If possible, I would like to implement this in the future, as it could aid in understanding Amplitude Amplification.

# Benefits
Amplitude Amplification is a rather complicated topic, especially for newcomers to the field. I personally found it to be the first real spike in difficulty while learning Quantum Algorithms, as the topic is usually described in extremely abstract ways. I hope visualising the tangible effects of each step of Amplitude Amplification can assist learners in understanding the process, as it illustrates exactly what occurs, rather than somewhat abstract notions of reflections and qubit states.

Additionally, in the future, I plan to improve on the project, cleaning up the display, making it easier to use, and adding features like the effect of the Oracle, and other forms of visualisation.
