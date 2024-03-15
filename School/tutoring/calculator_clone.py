import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("계산기")

        self.current_input = ""
        self.result_var = tk.StringVar()    # 결과창

        self.num1 = ""  # 첫번째 숫자
        self.num2 = ""  # 두번째 숫자
        self.operator = ""  # 연산자
        self.operator_check = False     # 연산자 값이 들어왔는지 체크

        # 입력창
        self.display = tk.Entry(master, textvariable=self.result_var, justify='right', bd=20, bg='light grey', fg="black")
        self.display.grid(row=0, column=0, columnspan=4)

        # 버튼 배치
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        row, col = 1, 0
        for button in buttons:
            tk.Button(master, text=button, width=5, height=2, command=lambda b=button: self.click_event(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    operators = ["+", "-", "*", "/"]

    def click_event(self, button):
        if button == "C":
            self.current_input = ""
            self.result_var.set("")
            self.num1 = ""
            self.num2 = ""
            self.operator = ""
            self.operator_check = False
        elif button == "=":
            if self.operator == "+":
                self.result_var.set(int(self.num1) + int(self.num2))
            elif self.operator == "-":
                self.result_var.set(int(self.num1) - int(self.num2))
            elif self.operator == "*":
                self.result_var.set(int(self.num1) * int(self.num2))
            elif self.operator == "/":
                self.result_var.set(int(self.num1) / int(self.num2))
        elif button in self.operators:
            self.operator_check = True
            self.operator = button
            self.result_var.set(self.operator)
        else:
            if self.operator_check:
                self.num2 += button
                self.result_var.set(self.num2)
            else:
                self.num1 += button
                self.result_var.set(self.num1)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
