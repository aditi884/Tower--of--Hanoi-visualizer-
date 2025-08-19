🗼 Tower of Hanoi Visualizer
This is a console-based application that visually solves the classic Tower of Hanoi puzzle. It uses recursion to find the optimal solution and provides a step-by-step ASCII-based animation of each disk movement, so you can see the algorithm in action.

⚙️ Core Concepts & Features
Recursive Solution: The program uses a recursive algorithm, which is the most elegant way to solve the Tower of Hanoi puzzle.

ASCII-Based Visualization: The state of the three towers and the disks is drawn directly in the console using a custom draw_towers function. This provides a real-time, animated view of the solution.

Interactive Input: You can specify the number of disks to solve for (from 1 to 8).

Controlled Speed: The animation speed can be easily adjusted by changing the DELAY variable in the code.

🚀 How to Run
Prerequisites: Ensure you have Python 3.x installed on your system.

Execution:

Save the code as a Python file (e.g., hanoi_visualizer.py).

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the script using the Python interpreter:

Bash

python hanoi_visualizer.py
The program will prompt you to enter the number of disks you want to solve.

📋 Sample Output
Here is a sample of what the output looks like for a 3-disk puzzle. Each step shows the configuration of the towers after a disk has been moved.

Enter the number of disks (1-8): 3

--- Initial State ---
   █     |      |
  ███    |      |
 █████   |      |
------- ------- -------
   A       B       C

Step: Move disk 1 from A to C
   █     |      |
  ███    |      |
------- ------- -------
   A       B       C

Step: Move disk 2 from A to B
   █     |      |
  ███    |      |
------- ------- -------
   A       B       C

Step: Move disk 1 from C to B
   █     |      |
  ███    |      |
------- ------- -------
   A       B       C

Step: Move disk 3 from A to C
   █     |      |
  ███    |      |
------- ------- -------
   A       B       C

Step: Move disk 1 from B to A
   █     |      |
  ███    |      |
------- ------- -------
   A       B       C

Step: Move disk 2 from B to C
   █     |      |
  ███    |      |
------- ------- -------
   A       B       C

Step: Move disk 1 from A to C
   █     |      |
  ███    |      |
------- ------- -------
   A       B       C


--- Puzzle Solved! ---
