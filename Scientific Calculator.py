import tkinter as tk
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("360x520")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.expression = ""

        # Display box
        self.display_frame = tk.Frame(
            root, bg="black", highlightbackground="white", highlightthickness=2
        )
        self.display_frame.pack(fill="x", padx=15, pady=15)

        self.display = tk.Entry(
            self.display_frame,
            font=("Arial", 22),
            bg="black",
            fg="white",
            borderwidth=0,
            justify="right",
            insertbackground="white"
        )
        self.display.pack(fill="x", padx=10, pady=10, ipady=10)

        self.create_buttons()
        self.bind_keyboard()   # 👈 keyboard support

    def create_buttons(self):
        buttons = [
            ["7", "8", "9", "/", "√"],
            ["4", "5", "6", "*", "x²"],
            ["1", "2", "3", "-", "log"],
            ["0", ".", "=", "+", "AC"],
            ["sin", "cos", "tan", "(", ")"]
        ]

        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        for row in buttons:
            row_frame = tk.Frame(main_frame, bg="black")
            row_frame.pack(expand=True, fill="both")

            for btn in row:
                box = tk.Frame(
                    row_frame,
                    bg="black",
                    highlightbackground="white",
                    highlightthickness=1
                )
                box.pack(side="left", expand=True, fill="both", padx=4, pady=4)

                button = tk.Button(
                    box,
                    text=btn,
                    font=("Arial", 14),
                    bg="black",
                    fg="white",
                    activebackground="#222222",
                    activeforeground="white",
                    borderwidth=0,
                    command=lambda b=btn: self.on_click(b)
                )
                button.pack(expand=True, fill="both")

    def bind_keyboard(self):
        self.root.bind("<Key>", self.key_press)
        self.root.bind("<Return>", lambda e: self.on_click("="))
        self.root.bind("<BackSpace>", self.backspace)
        self.root.bind("<Escape>", lambda e: self.on_click("AC"))

    def key_press(self, event):
        key = event.char

        if key in "0123456789+-*/().":
            self.on_click(key)

        elif key == "s":
            self.on_click("sin")
        elif key == "c":
            self.on_click("cos")
        elif key == "t":
            self.on_click("tan")
        elif key == "l":
            self.on_click("log")
        elif key == "r":
            self.on_click("√")
        elif key == "q":
            self.on_click("x²")

    def backspace(self, event):
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def on_click(self, value):
        if value == "AC":
            self.expression = ""
            self.display.delete(0, tk.END)

        elif value == "=":
            self.calculate()

        elif value == "√":
            self.expression = f"math.sqrt({self.expression})"
            self.calculate()

        elif value == "x²":
            self.expression = f"({self.expression})**2"
            self.calculate()

        elif value in ["sin", "cos", "tan"]:
            self.expression = f"math.{value}(math.radians({self.expression}))"
            self.calculate()

        elif value == "log":
            self.expression = f"math.log10({self.expression})"
            self.calculate()

        else:
            self.expression += value
            self.display.insert(tk.END, value)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = str(result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""


# Run app
root = tk.Tk()
app = ScientificCalculator(root)
root.mainloop()
