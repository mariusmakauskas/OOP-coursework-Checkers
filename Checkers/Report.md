# OOP Coursework Report

## Introduction

This application is a digital version of the classic board game Checkers, implemented using Python programming language. It allows two players to play against each other on an 8x8 board, following standard checkers rules, including piece movement, capturing, kinging, and alternating turns.

### To run the program, follow these steps:

* Ensure you have Python 3.x installed on your machine.
* Install pygame library.
* Navigate to the folder containing the source files.
* Run the main script.

### Once the program starts:

* A checkers board will be displayed
* Player 1 (or player with grey checker pieces) and Player 2 (or player with white checker pieces) take turns by clicking on a piece and then clicking on a valid square to move.
* Captures are made by jumping over opponent pieces.
* Pieces that reach the opposite side of the board are promoted to kings.
* The game ends when one player has captured all their opponents’ pieces.

# Analysis
**Polymorphism** is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as if they were objects of the same superclass. It enables a single interface to be used for different underlying data types or classes. The application functions correctly, providing a full checkers experience for two players. All core game rules are implemented and tested. The user interface updates in real-time based on player actions.
![alt text](<Assets for report/Report1.png>)
![alt text](<Assets for report/Report2.png>)
In this instance of polymorphism I have “Piece” class and it’s daughter class “King”, which allows me to overwrite the draw method that draws a checker piece on the board whenever a piece is promoted to king and make it look different from the rest.

An **abstract class** is a class that cannot be instantiated on its own and is meant to be subclassed. It often contains one or more abstract methods - methods that are declared but have no implementation in the abstract class. Subclasses are expected to implement these methods.
![alt text](<Assets for report/Report3.png>)
In this instance of abstract class I create AbstractPiece class that makes sure draw and calculate_position methods are implemented in the Piece class.

**Inheritance** is a fundamental concept in object-oriented programming (OOP) where a class (child/subclass) derives properties and behaviors (methods and attributes) from another class (parent/superclass). This allows for code reuse, extensibility, and a hierarchical class structure.
![alt text](<Assets for report/Report4.png>)
In this instance of inheritance King class inherits Piece class which lets me create fewer methods since most behavior is already covered in the Piece class.

**Encapsulation** is an object-oriented programming (OOP) principle that involves bundling data (attributes) and the methods that operate on that data into a single unit (a class), while restricting direct access to some of the object’s components. This helps protect the internal state of an object and enforce a clean interface for interacting with it.
![alt text](<Assets for report/Report5.png>)
The Board class encapsulates its internal state using private attributes and provides controlled access through getter and setter methods.

A **Singleton** is a design pattern that ensures a class has only one instance throughout the lifetime of a program and provides a global point of access to that instance.
![alt text](<Assets for report/Report6.png>)
In a checkers game, there should only ever be one game board active at a time. Allowing multiple Board instances could lead to conflicting game states, confusion in turn logic or difficulty synchronizing. By using the Singleton pattern, the program guarantees that only one Board instance exists throughout the game.

**Composition** is an object-oriented programming principle where one class is made up of one or more objects of other classes, meaning it "has-a" relationship. It represents a strong ownership—when the container (parent) object is destroyed, its composed (child) objects are also destroyed.
 ![alt text](<Assets for report/Report7.png>)
Game class creates the board based on Board class which means there’s no way for game to exist without board.

# Results:
* Board Setup: The checkers board is initialized correctly with pieces placed in starting positions.
* Turn-Based Gameplay: The application manages turn-taking between the two players.
* Piece Movement: Players can move pieces diagonally forward and perform valid jumps over opponents.
* Capturing Mechanism: Jumping over and removing opponent pieces works according to the official rules.
* King Promotion: When a piece reaches the opposite side of the board, it is promoted to a king, gaining the ability to move backward as well.
* Win Condition Detection: The game checks if a player has won by eliminating all opponent pieces.
* Graphical Interface: The board and pieces are drawn using the pygame library, with user interaction handled via mouse events.
* Input Validation: Illegal moves are rejected and not processed.

# Possible Extensions:
* Single-player mode with AI opponent using minimax algorithm or other game tree strategies.
* Online multiplayer using network sockets or integration with web technologies.
* Customizable settings, such as board size, themes, or rule variants.
* Improved animations and sound effects for better user experience.
* Saving and loading games to allow players to resume previous sessions.