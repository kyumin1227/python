import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("계산기")

        self.current_input = ""
        self.result_var = tk.StringVar()

        # 입력창
        self.display = tk.Entry(master, textvariable=self.result_var, justify='right', bd=20, bg='light grey')
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

    def click_event(self, button):
        if button == 'C':
            self.current_input = ""
            self.result_var.set(self.current_input)
        elif button == '=':
            try:
                self.current_input = str(eval(self.current_input))
                self.result_var.set(self.current_input)
            except Exception as e:
                self.result_var.set("Error")
                self.current_input = ""
        else:
            self.current_input += str(button)
            self.result_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
