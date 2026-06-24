# Eurovision-voting-simulator

A Python-based simulation of the Eurovision Song Contest featuring semi-finals, jury voting, televoting, country voting biases, and a grand final.

Overview

This project recreates the Eurovision voting process using a custom scoring system and randomly generated song attributes. Each participating country receives a unique song profile, and votes are awarded through both professional jury evaluations and public televoting.

The simulator models key aspects of the contest, including qualification rounds, weighted scoring systems, and voting patterns between countries.

Features

* Semi-Final 1 and Semi-Final 2
* Grand Final qualification system
* Eurovision-style scoring (12, 10, 8–1 points)
* Jury voting simulation
* Public televoting simulation
* Country voting biases
* Randomly generated song characteristics
* Automatic winner determination
* Detailed scoreboards and contest statistics

Song Attributes

Each country receives a randomly generated song with the following characteristics:

* Vocals
* Staging
* Originality
* Catchiness

These attributes influence both jury and televote results through different weighted scoring systems.

Scoring System

Jury Voting

The jury score is calculated using:

* 40% Vocals
* 35% Originality
* 25% Staging

Televoting

The televote score is calculated using:

* 45% Staging
* 35% Catchiness
* 20% Originality

This creates realistic differences between professional jury preferences and public opinion.

Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Algorithms and Sorting
* Weighted Scoring Systems
* Simulation Design

Running the Project

Clone the repository:

git clone https://github.com/YOUR_USERNAME/eurovision-simulator.git

Navigate to the project directory:

cd eurovision-simulator

Run the simulator:

python eurovision_simulator.py

Example Output

EUROVISION SONG CONTEST SIMULATOR
Running Semi Final 1...
Running Semi Final 2...
GRAND FINAL RESULTS
1. Sweden      Total: 154
2. Finland     Total: 147
3. Italy       Total: 141
WINNER: Sweden

Educational Goals

This project was developed to practice:

* Python programming
* Object-oriented design
* Data modeling
* Simulation systems
* Ranking algorithms
* Git and GitHub workflows

Future Improvements

* Additional participating countries
* Song genres and performance styles
* Monte Carlo tournament simulations
* Qualification probability analysis
* Data visualization with Matplotlib
* CSV export of contest results
* Interactive user interface

License

This project is licensed under the MIT License.

Author
Ayşe İrem Zeybek
