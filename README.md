# Day-6-Project
# Reeborg's World - Maze Solver

A Python solution for navigating mazes in Reeborg's World using the right-hand wall-following algorithm.

## About

Built this to practice functions, conditionals, and algorithmic thinking in Python. The program uses a right-hand wall-following strategy to navigate Reeborg through maze challenges and reach the goal.

## How It Works

The solution follows a simple principle: **keep your right hand on the wall and follow it to the exit.**

### Helper Functions

- `turn_around()` - Turn 180 degrees
- `turn_right()` - Turn right (Reeborg only has turn_left() built-in)
- `jump()` - Jump over a single hurdle

### Main Algorithm

1. Find the wall: Move forward until encountering a wall on the right
2. Follow the wall: Keep the wall on the right while moving toward the goal
3. Navigate turns: Turn left at dead ends, turn right when the wall opens up

### Decision Logic
```
If front is clear AND wall on right → Move forward
If front is blocked AND wall on right → Turn left
If right is clear (wall disappeared) → Turn right and move
```

## Reeborg's World Commands Used

**Movement:**
- `move()` - Move forward one space
- `turn_left()` - Turn 90° left

**Sensors:**
- `front_is_clear()` - Check if front is open
- `right_is_clear()` - Check if right is open
- `wall_on_right()` - Check if wall exists on right
- `wall_in_front()` - Check if wall exists in front
- `at_goal()` - Check if goal reached

## Wall-Following Algorithm

This is a classic maze-solving technique that works for any maze where the goal is connected to the outer wall. It's guaranteed to find the exit (though not necessarily the shortest path).

The algorithm: Keep the wall on your right and follow it. When you hit a dead end, turn left. When the wall disappears on your right, turn right to follow it.

## What I Learned

- Algorithmic thinking - Breaking down maze navigation into simple rules
- Function abstraction - Creating reusable helper functions
- While loops - Repeating actions until a condition is met
- Conditional logic - Making decisions based on environment
- Problem decomposition - Splitting complex behavior into smaller functions

## Code Notes

**Unused Functions:**
- `vertical()` and `jump()` were created for different Reeborg challenges but aren't used in this maze solver
- Left in code as examples of movement patterns for other worlds

## Limitations

- Only works for mazes where following the right wall leads to the goal
- Doesn't find the optimal (shortest) path, just *a* path
- Won't work in mazes with "islands" or disconnected walls

## Potential Improvements

- Add left-hand wall following for different maze types
- Implement breadth-first search for optimal pathfinding
- Add memory to avoid revisiting spaces
- Handle more complex Reeborg worlds (multiple goals, obstacles)

---

*Learning project - practicing algorithmic problem-solving with Python*

**About Reeborg's World:** An interactive learning environment for Python programming where you control a robot through various challenges. Visit [reeborg.ca](https://reeborg.ca)
