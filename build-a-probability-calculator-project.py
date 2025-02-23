import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)  # Add each color the specified number of times

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]  # Copy all balls
            self.contents = []  # Clear the contents
            return drawn_balls
        drawn_balls = random.sample(self.contents, num_balls)  # Draw without replacement
        for ball in drawn_balls:
            self.contents.remove(ball)  # Remove drawn balls from the hat
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)  # Create a copy of the hat for each experiment
        drawn_balls = hat_copy.draw(num_balls_drawn)  # Draw the specified number of balls

        # Check if the drawn balls meet the expected criteria
        if all(drawn_balls.count(color) >= count for color, count in expected_balls.items()):
            success_count += 1  # Increment success count if criteria are met

    # Calculate the probability
    probability = success_count / num_experiments
    return probability

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(probability)