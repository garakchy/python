from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton    # QMainWindow is a subclass of QWidget  
import sys                                                       # QPushButton is a subclass of QAbstractButton     
app = QApplication(sys.argv)                                            
window = QMainWindow()                          
window.setWindowTitle("My first MainWindow app")        
button = QPushButton()              
button.setText("Click me")                  
window.setCentralWidget(button)             
window.show()                   
sys.exit(app.exec_())   # This is the event loop