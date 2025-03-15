import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QLineEdit
import gate_training

class LogicGateSimulator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        self.label1 = QLabel("Input A (0 or 1):")
        self.inputA = QLineEdit()
        
        self.label2 = QLabel("Input B (0 or 1):")
        self.inputB = QLineEdit()
        
        self.gateLabel = QLabel("Select Logic Gate:")
        self.gateSelector = QComboBox()
        self.gateSelector.addItems(["AND", "OR"])
        
        self.computeButton = QPushButton("Compute")
        self.computeButton.clicked.connect(self.compute_logic)
        
        self.resultLabel = QLabel("Output: ")
        
        layout.addWidget(self.label1)
        layout.addWidget(self.inputA)
        layout.addWidget(self.label2)
        layout.addWidget(self.inputB)
        layout.addWidget(self.gateLabel)
        layout.addWidget(self.gateSelector)
        layout.addWidget(self.computeButton)
        layout.addWidget(self.resultLabel)
        
        self.setLayout(layout)
        self.setWindowTitle("Logic Gate Simulator")
    
    def compute_logic(self):
        """
        try:
            a = int(self.inputA.text())
            b = int(self.inputB.text())
            if a not in [0, 1] or b not in [0, 1]:
                raise ValueError("Inputs must be 0 or 1")
            
            gate = self.gateSelector.currentText()
            
            if gate == "AND":
                result = a and b
            else:
                result = a or b
            
            self.resultLabel.setText(f"Output: {result}")
        except ValueError:
            self.resultLabel.setText("Invalid input! Enter 0 or 1.")
        """
        gate_t= None
        gate_type = self.gateSelector.currentText()
        if gate_type.lower() == "and":
            gate_t=0
        elif gate_type.lower() == "or":
            gate_t = 1
        try:
            num1 = int(self.inputB.text())
            num2 = int(self.inputA.text())
            test_input = gate_training.np.array([[num1, num2]], dtype=gate_training.np.float32)  # Example input
            prediction = gate_training.model.predict(test_input)
            #print(f"Input: {test_input.tolist()} => Predicted Output: {prediction[0][0]:.4f}")
            #print(f"Result : {round(res)}")
            res = float(prediction[0][gate_t])
            print(f"Input: {test_input.tolist()} => Predicted Output: {prediction[0][gate_t]:.4f}")
            print(f"Input: {test_input.tolist()} => Predicted Output: {round(res)}")
            self.resultLabel.setText(f"Output: {round(res)}")
        except ValueError:
            self.resultLabel.setText("Invalid input! Enter 0 or 1.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogicGateSimulator()
    window.show()
    sys.exit(app.exec_())