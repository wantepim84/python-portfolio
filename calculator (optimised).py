from tkinter import Tk, StringVar, Label, Button, Frame

class Calculator:
    def __init__(self, window):
        self.equation_txt = ""
        self.equation_label = StringVar()
        self.create_widgets(window)

    def button_press(self, num):
        self.equation_txt += str(num)
        self.equation_label.set(self.equation_txt)

    def equals(self):
        try:
            total = str(eval(self.equation_txt))
            self.equation_label.set(total)
            self.equation_txt = total
        except (ZeroDivisionError, SyntaxError):
            self.equation_label.set("Error")
            self.equation_txt = ""

    def clear(self):
        self.equation_label.set("")
        self.equation_txt = ""

    def create_widgets(self, window):
        label = Label(window, textvariable=self.equation_label, font=(
            "Comic Sans", 20), bg="white", width=30, height=2)
        label.pack()

        frame = Frame(window)
        frame.pack()

        buttons = [
            '1', '2', '3', '/',
            '4', '5', '6', '*',
            '7', '7', '9', '-',
            '0', '.', '=', '+'
        ]

        row, col = 0, 0
        for btn_text in buttons:
            btn = Button(frame, text=btn_text, height=4, width=10, font=30,
                         command=lambda text=btn_text: self.button_press(text) if text != '=' else self.equals())
            btn.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_button = Button(window, text="Clear", height=4,
                              width=10, font=30, command=self.clear)
        clear_button.pack()


if __name__ == "__main__":
    window = Tk()
    window.title("Calculator Program")
    window.geometry("650x650")

    calculator = Calculator(window)

    window.mainloop()
