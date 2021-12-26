import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

pointsLea = 0
pointsCorentin = 0

# Fonction ajout de points
def corentinScores():
    global pointsCorentin
    pointsCorentin = pointsCorentin + 1
    affichageScores()

def leaScores():
    global pointsLea
    pointsLea = pointsLea + 1
    affichageScores()

# Fonction permettant l'actualisation des scores
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


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("BlindtestScore")
window.setFixedWidth(460)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

### Widgets

# Score buttons
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
