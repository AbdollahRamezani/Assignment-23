import sys
import random
from functools import partial
from sudoku import Sudoku
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow  


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)
        self.ui.menu_newgame.triggered.connect(self.new_game)
        self.ui.menu_openfile.triggered.connect(self.open_file)
        self.line_edit = [[None for i in range(9)] for j in range(9)]   
        self.new_game()

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Open File...")[0] 
        f = open(file_path, "r")
        big_text = f.read()
        rows = big_text.split("\n")
        puzzle_board = [[None for i in range(9)] for j in range(9)]
        for i in range(len(rows)):
            cells = rows[i].split(" ")
            for j in range(len(cells)):
                puzzle_board[i][j] = int(cells[j])       
               

        puzzle = Sudoku(3, seed= random.randint(1, 1000)).difficulty(0.5)       
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setReadOnly(False)
                if puzzle.board[i][j] != 0:
                    new_cell.setText(str(puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.grid_Layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j)) 
                self.line_edit[i][j] = new_cell         


    def new_game(self):
        puzzle = Sudoku(3, seed= random.randint(1, 1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setReadOnly(False)
                if puzzle.board[i][j] != None:
                    new_cell.setText(str(puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.grid_Layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j)) 
                self.line_edit[i][j] = new_cell 


    def check(self):
        for i in range(0, 9):
            for j in range(0, 9):
                number1 = self.line_edit[i][0].text()
                number2 = self.line_edit[i][j].text()
                if number1 == number2:
                    return False
                else:
                    return True
            

    def validation(self, i, j, text):  
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
             self.line_edit[i][j].setText("")
        self.check()     


if __name__ == "__main__":        
    app = QApplication(sys.argv)    
    
    main_window = MainWindow()
    main_window.show()



    app.exec()
