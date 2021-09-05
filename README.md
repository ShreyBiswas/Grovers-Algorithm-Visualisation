## Grover's Algorithm Visualisation
![image](https://github.com/StreakSharn/Grovers-Algorithm-Visualisation/blob/main/animation.gif)

Submission by Streak#8889, to QCHack's IBM Challenge Part 1

This visualisation illustrates the process of Amplitude Amplification, specifically in Grover's Algorithm. On each pass through the Oracle and Diffusion Operator, incorrect states are interfered out, increasing the probability of a single 'correct' amplitude, and decreasing the probability of all others.

By regularly sampling the statevector throughout the circuit, the program obtains the qubit states after each Oracle + Diffuser pass. Due to the Auxiliary/Output qubit being included in the statevector, only half of the statevector is used for the display.

The statevector is then displayed in two forms: a Bar Graph and Rose Chart. Both assign a single colour to each potential output state, which is consistent between the visualisations. They show the growth of one particular state, along with the decrease in all others. The Bar Chart includes a 'zero' line in grey, where the probability of measuring a state is zero. For the Rose Chart, this is the centre of the circle.

# Usage Instructions
 - Install [Qiskit](https://github.com/Qiskit/qiskit) and [ManimCE](https://github.com/ManimCommunity/manim), along with dependencies they may have.
 - Clone this repository to your machine.
 - Open a Terminal to the folder where `grover_animation.py` is stored, currently named `src`.
 - Run the following command: `manim grover_animation.py Grover_Animation -p --leave_progress_bars -qm`

# Notes:

When creating the video files, Manim uses FFMPEG. Your antivirus may detect FFMPEG creating files, and prevent it from functioning correctly - you may need to create an exception within the antivirus. FFMPEG is reputable, open-source software which can be viewed [here](https://github.com/FFmpeg/FFmpeg).

The above Terminal command renders the illustration in medium quality. For faster rendering, lower the quality by replacing `-qm` with `-ql` (lowercase L, not the number 1). For higher quality, replace `-qm` with `-qh`.


