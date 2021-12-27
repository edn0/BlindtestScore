import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


# // # TODO:
# Ability to add new players, and more players simulaneously
# Hide the total number of victories while game is ongoing (only show once "End game" is clicked, and disappears once "Reset" is hit. Might require a widget list, and therefore restructuring the app functionnality)

pointsLea = 0
pointsCorentin = 0

# Check for the existence of database, else creates it
con = sqlite3.connect("points.db")
cur = con.cursor()
cur.execute("create table if not exists points(joueur text, victoires integer)")
con.close()

# Checks the content of the db on startup and prints in console
def checkDb():
    con = sqlite3.connect("points.db")
    cur = con.cursor()
    cur.execute("select * from points")
    search_results  = cur.fetchall()
    print(search_results)
    con.close()
checkDb()

# Fuctions to connect to db to update victory total
def corentinWins():
    con = sqlite3.connect("points.db")
    cur = con.cursor()
    cur.execute("update points set victoires=victoires+1 where joueur='Corentin'")
    con.commit()
    checkDb()
    con.close()

def leaWins():
    con = sqlite3.connect("points.db")
    cur = con.cursor()
    cur.execute("update points set victoires=victoires+1 where joueur='Lea'")
    con.commit()
    checkDb()
    con.close()

# Finish game function, increasing by 1 the number of victories of the player with the most points and starts the function that'll edit the database
def gameFinished():
    if pointsCorentin > pointsLea:
        corentinWins()
    else:
        leaWins()
    displayVictories()

# Functions to reset and add points
def corentinScores():
    global pointsCorentin
    pointsCorentin = pointsCorentin + 1
    affichageScores()

def leaScores():
    global pointsLea
    pointsLea = pointsLea + 1
    affichageScores()

def resetScore():
    global pointsLea
    global pointsCorentin
    pointsCorentin = 0
    pointsLea = 0
    affichageScores()

# Function to update the score displayed
def affichageScores():
    scoreLea = QLabel(str(pointsLea))
    scoreLea.setAlignment(QtCore.Qt.AlignCenter)
    # stylesheet à revoir
    scoreLea.setStyleSheet(
    "font-size: 32px;"+
    "color: 'white';"+
    "margin: 5px 25px;"
    )
    grid.addWidget(scoreLea, 3, 0)
    scoreCorentin = QLabel(str(pointsCorentin))
    scoreCorentin.setAlignment(QtCore.Qt.AlignCenter)
    # stylesheet à revoir
    scoreCorentin.setStyleSheet(
    "font-size: 32px;"+
    "color: 'white';"+
    "margin: 5px 25px;"
    )
    grid.addWidget(scoreCorentin, 3, 2)

# Display total number of victories
def displayVictories():
    con = sqlite3.connect("points.db")
    cur = con.cursor()
    cur.execute("select * from points")
    victories = cur.fetchall()
    print("Léa :", victories[1][1])
    print("Corentin:", victories [0][1])
    print("////////////////////////////////////////:")
    checkDb()
    corentinVictories = victories[0][1]
    leaVictories = victories [1][1]
    con.close()

    labelLeaVictories = QLabel(str(leaVictories))
    labelLeaVictories.setAlignment(QtCore.Qt.AlignLeft)
    labelLeaVictories.setStyleSheet(
    "font-size: 24px;"+
    "color: 'white';"+
    "margin: 5px 25px;"
    )
    grid.addWidget(labelLeaVictories, 6, 0)

    labelCorentinVictories = QLabel(str(corentinVictories))
    labelCorentinVictories.setAlignment(QtCore.Qt.AlignRight)
    labelCorentinVictories.setStyleSheet(
    "font-size: 24px;"+
    "color: 'white';"+
    "margin: 5px 25px;"
    )
    grid.addWidget(labelCorentinVictories, 6, 2)

    labelTotalWins = QLabel("Total wins")
    labelTotalWins.setAlignment(QtCore.Qt.AlignCenter)
    labelTotalWins.setStyleSheet(
    "font-size: 24px;"+
    "color: 'white';"+
    "margin: 5px 20px;"
    )
    grid.addWidget(labelTotalWins, 6, 1)


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("BlindtestScore")
window.setFixedWidth(460)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()


### Widgets

# Score buttons
# Increase score buttons
buttonCorentin = QPushButton("+1")
buttonCorentin.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
buttonCorentin.clicked.connect(corentinScores)
buttonCorentin.setStyleSheet(
"*{border: 4px solid '#FFFFFF';"+
"border-radius:15px;"+
"font-size: 27px;"+
"margin: 20px 25px;"+
"background-color: '#9b37e6';"+
"color: 'white'}"+
"*:hover{background: '#3c2c48';"+
"font-size: 30px;}"
)
grid.addWidget(buttonCorentin, 4, 2)

buttonLea = QPushButton("+1")
buttonLea.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
buttonLea.clicked.connect(leaScores)
buttonLea.setStyleSheet(
"*{border: 4px solid '#FFFFFF';"+
"border-radius:15px;"+
"font-size: 27px;"+
"margin: 20px 25px;"+
"background-color: '#9b37e6';"+
"color: 'white'}"+
"*:hover{background: '#3c2c48';"+
"font-size: 30px;}"
)
grid.addWidget(buttonLea, 4, 0)

# Game finished button
endGameButton = QPushButton("End game")
endGameButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
endGameButton.clicked.connect(gameFinished)
endGameButton.setStyleSheet(
"*{border: 2px solid '#FFFFFF';"+
"border-radius:5px;"+
"font-size: 16px;"+
"margin: 20px 25px;"+
"background-color: '#161219';"+
"color: 'white'}"+
"*:hover{background: '#752617';"+
"font-size: 16px;}"
)
grid.addWidget(endGameButton, 5, 1)

# Reset score button
buttonReset = QPushButton("Reset")
buttonReset.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
buttonReset.clicked.connect(resetScore)
buttonReset.setStyleSheet(
"*{border: 2px solid '#FFFFFF';"+
"border-radius:5px;"+
"font-size: 16px;"+
"margin: 20px 25px;"+
"background-color: '#161219';"+
"color: 'white'}"+
"*:hover{background: '#3c2c48';"+
"font-size: 16px;}"
)
grid.addWidget(buttonReset, 0, 2)

# Display our pictures and add names
avatarCorentin = QPixmap("co.png")
co = QLabel()
co.setPixmap(avatarCorentin)
co.setAlignment(QtCore.Qt.AlignLeft)
co.setStyleSheet("margin-bottom: 12")

player1name = QLabel("Corentin")
player1name.setAlignment(QtCore.Qt.AlignLeft)
player1name.setStyleSheet(
"font-size: 24px;"+
"color: 'white';"+
"margin: 5px 0px;"
)

avatarLea = QPixmap("lea.png")
lea = QLabel()
lea.setPixmap(avatarLea)
lea.setAlignment(QtCore.Qt.AlignRight)
lea.setStyleSheet("margin-bottom: 12")

player2name = QLabel("Léa")
player2name.setAlignment(QtCore.Qt.AlignRight)
player2name.setStyleSheet(
"font-size: 24px;"+
"color: 'white';"+
"margin: 5px 25px;"
)

grid.addWidget(co, 1, 2)
grid.addWidget(player1name, 2, 2)
grid.addWidget(lea, 1, 0)
grid.addWidget(player2name, 2, 0)

# Title at the top of the startFrame
frameTitle = QLabel("Blindtest")
frameTitle.setAlignment(QtCore.Qt.AlignCenter)
frameTitle.setStyleSheet(
"font-size: 32px;"+
"color: 'white';"+
"margin: 5px 10px;"
)
grid.addWidget(frameTitle, 0, 1)

affichageScores()

window.setLayout(grid)

window.show()
sys.exit(app.exec())
