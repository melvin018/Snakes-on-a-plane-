# Snakes-on-a-plane-
This project is a simple yet polished implementation of the classic Snake game built using Python and the Pygame library.
Snake Game – Documentation
Overview

This project is a simple yet polished implementation of the classic Snake game built using Python and the Pygame library.
The objective is to control a growing snake, eat food items, avoid collisions, and achieve the highest possible score.
The game features smooth movement, dynamic speed increase, grid-based rendering, and a clean user interface.

Features

Classic Snake Gameplay – Move the snake around a grid and eat food to grow.

Smooth Controls – Supports arrow keys or WASD.

Dynamic Difficulty – Game speed increases each time food is eaten.

Collision Detection

Wall collision ends the game

Self-collision ends the game

Restart Mechanism – Press R after game over to restart.

HUD Display – Shows real-time score during gameplay.

Clean Visual Style – Dark background, color-coded snake segments, and minimalistic grid lines.

Requirements

Python 3.x

pygame library

Install pygame using:

pip install pygame

How to Run

Save the script as snake.py

Run the game using:

python3 snake.py


The game window will open automatically.

Controls
Key	Action
← / A	Move Left
→ / D	Move Right
↑ / W	Move Up
↓ / S	Move Down
R	Restart after Game Over
Q / ESC	Quit Game
Gameplay Mechanics
Movement

The snake moves continuously in the last chosen direction.

The player cannot instantly reverse direction (e.g., from left to right). This prevents immediate self-collision.

Food

Food appears randomly on any free cell.

Eating food:

Increases score by 1

Grows the snake by one segment

Increases game speed up to a defined maximum

Speed

Starting speed: 8 FPS

Maximum speed: 25 FPS

Each food eaten increases speed by 0.5 FPS

Game Over Conditions

The game ends when:

The snake hits a wall

The snake collides with its own body

A “Game Over” message will be displayed, along with instructions to restart or quit.

Code Structure
Main Components

Configuration Section
Sets constants such as grid size, cell size, colors, and speed values.

Utility Functions

rnd_cell(exclude) – Chooses a random grid coordinate not occupied by the snake.

draw_grid() – Draws the background grid.

draw_rect() – Renders snake segments and food.

main() Function

Initializes pygame, screen, clock, and fonts

Runs the game loop

Handles:

Input events

Snake movement

Collision logic

Rendering

Game over & restart behavior

new_game()

Resets all game variables:

Snake starting position

Direction

Food location

Score

Speed

Visual Design

Background: Dark gray to reduce eye strain

Grid Lines: Subtle lines for orientation

Snake Head: Bright green

Snake Body: Darker green

Food: Red for visibility

Text Color: Light gray

Possible Enhancements

You can extend the game with:

Sound effects (eating, game over)

Adjustable difficulty levels

High score saving

Animations

Skins or themes

Obstacles mode

Menu screen

License

This project is free to use, modify, and distribute for learning or personal use.