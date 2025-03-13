Fact or Fake - A Pygame Fact-Checking Game

  Overview

    Fact or Fake is a simple yet engaging game built using Python and Pygame. 
    The game tests players' ability to distinguish between real and fake facts within a time limit.
    The objective is to score as many points as possible by correctly identifying statements as either true or false.

  Features

    Randomized fact presentation with both real and fake statements.
    
    Timed gameplay with a countdown for each question.
    
    Score tracking with penalties for incorrect answers.
    
    Verification option for players who are unsure about a fact (with a score penalty).
    
    Win/Loss conditions based on score thresholds.
    
    Simple yet visually appealing UI built with Pygame.

How to Play

    Start the game by clicking the "Start Game" button.
    
    A statement will appear on the screen.
    
    Press the following keys to respond:
    
    T - If you think the statement is true.
    
    F - If you think the statement is false.
    
    V - Verify the fact (results in a score penalty).
    
    Answer quickly! You have limited time for each statement.
    
    The game ends when you either reach 200 points (Win) or -200 points (Game Over).

Installation & Setup

Ensure you have Python installed (version 3.6 or higher recommended).

Install the required dependency:

  pip install pygame
  
Clone the repository:

  git clone https://github.com/yourusername/fact-or-fake.git

Navigate to the project directory:

  cd fact-or-fake

Run the game:
  python fact_or_fake.py
