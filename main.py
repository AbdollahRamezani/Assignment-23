import sys
from sudoku import Sudoku
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)
        puzzle = Sudoku(3).difficulty(0.5)
        
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                if puzzle.board[i][j] != None:
                    new_cell.setText(str(puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.grid_Layout.addWidget(new_cell, i, j)

                

if __name__ == "__main__":        
    app = QApplication(sys.argv)    
    
    main_window = MainWindow()
    main_window.show()



    app.exec()