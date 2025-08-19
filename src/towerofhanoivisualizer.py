import os
import time

# --- Global Configuration ---
# Set the delay in seconds to control the speed of the animation.
DELAY = 0.5
# Define the characters for the disks.
DISK_CHAR = '█'
# The base character for the tower pegs.
PEG_CHAR = '|'

def draw_towers(towers, disk_width):
    """
    Draws the current state of the three towers using ASCII art.
    Each tower is represented as a list of disks (integers).
    
    Args:
        towers (dict): A dictionary where keys are tower names ('A', 'B', 'C')
                       and values are lists of disk sizes (integers).
        disk_width (int): The maximum width of the largest disk for formatting.
    """
    # Clear the console for a clean visualization on each step.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Find the maximum height (number of disks) to ensure all towers
    # are drawn to the same height for a stable visual.
    max_height = max(len(towers['A']), len(towers['B']), len(towers['C']))
    
    # Iterate from top to bottom of the tallest tower.
    for i in range(max_height - 1, -1, -1):
        line = ""
        for name in ['A', 'B', 'C']:
            # Get the disk at the current level, if it exists.
            disks = towers[name]
            if i < len(disks):
                disk_size = disks[i]
                # Create the visual representation of the disk.
                disk_str = DISK_CHAR * (2 * disk_size - 1)
                # Pad the disk string with spaces to center it.
                padding = " " * (disk_width - disk_size)
                line += f"{padding}{disk_str}{padding}   "
            else:
                # If no disk, draw an empty peg space.
                empty_space = " " * (2 * disk_width - 1)
                line += f"{empty_space}   "
        print(line)

    # Draw the base of the towers.
    base_line = ""
    for _ in range(3):
        base_line += "-" * (2 * disk_width - 1) + "---"
    print(base_line)
    
    # Label the towers.
    labels = f" {'A':^{2*disk_width-1}}   {'B':^{2*disk_width-1}}   {'C':^{2*disk_width-1}}"
    print(labels)


def hanoi(n, source, destination, auxiliary, towers, disk_width):
    """
    The recursive function to solve the Tower of Hanoi puzzle.
    
    Args:
        n (int): The number of disks to move.
        source (str): The name of the source tower.
        destination (str): The name of the destination tower.
        auxiliary (str): The name of the auxiliary tower.
        towers (dict): A reference to the current state of the towers.
        disk_width (int): The maximum width of the largest disk for formatting.
    """
    # Base case: if there's only one disk, move it directly.
    if n == 1:
        # Move the disk from the source to the destination.
        disk = towers[source].pop()
        towers[destination].append(disk)
        
        # Print the step and visualize the new state.
        print(f"\nStep: Move disk {disk} from {source} to {destination}")
        draw_towers(towers, disk_width)
        time.sleep(DELAY)
        return

    # Recursive step 1: Move n-1 disks from the source to the auxiliary peg.
    hanoi(n - 1, source, auxiliary, destination, towers, disk_width)

    # Recursive step 2: Move the nth disk (the largest one) from the source to the destination.
    disk = towers[source].pop()
    towers[destination].append(disk)
    print(f"\nStep: Move disk {disk} from {source} to {destination}")
    draw_towers(towers, disk_width)
    time.sleep(DELAY)

    # Recursive step 3: Move the n-1 disks from the auxiliary to the destination peg.
    hanoi(n - 1, auxiliary, destination, source, towers, disk_width)


def main():
    """
    Main function to initialize the puzzle and start the visualization.
    """
    while True:
        try:
            num_disks_input = input("Enter the number of disks (1-8): ")
            num_disks = int(num_disks_input)
            if 1 <= num_disks <= 8:
                break
            else:
                print("Please enter a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Initialize the towers. Tower 'A' gets all the disks.
    towers = {
        'A': list(range(num_disks, 0, -1)),
        'B': [],
        'C': []
    }
    
    # Calculate the width needed for formatting the ASCII art.
    disk_width = num_disks + 1

    print("\n--- Initial State ---")
    draw_towers(towers, disk_width)
    time.sleep(DELAY * 3) # Pause to see the initial state

    # Start the recursive solution.
    hanoi(num_disks, 'A', 'C', 'B', towers, disk_width)
    
    print("\n\n--- Puzzle Solved! ---")

if __name__ == "__main__":
    main()
