import tkinter as tk

# Custom button style
def create_button(master, text, command, bg_color, fg_color, font=("Helvetica", 20, "bold")):
    return tk.Button(master, text=text, command=command, bg=bg_color, fg=fg_color, font=font, bd=0, relief="ridge", padx=10, pady=10)

# Calculator class
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("350x500")
        self.root.title("Calculator")
        self.root.configure(bg="black")
        
        # Remove default title bar
        self.root.overrideredirect(True)
        
        # Add custom title bar
        self.create_title_bar()
        
        # Display screen
        self.screen = tk.Entry(root, font=("Helvetica", 30), bg="black", fg="white", bd=0, justify="right")
        self.screen.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        
        # Add buttons
        self.create_buttons()
        
        # Keyboard bindings
        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<BackSpace>", lambda event: self.delete_last())
        self.root.bind("<Escape>", lambda event: self.clear())
        
    def create_title_bar(self):
        # Create a frame for the custom title bar
        title_bar = tk.Frame(self.root, bg="black", height=20)
        title_bar.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Add a close button
        close_button = tk.Button(title_bar, text="X", command=self.root.destroy, fg="white", bg="black", bd=0, font=("Helvetica", 12))
        close_button.pack(side="right", padx=5)

        # Add a title label
        title_label = tk.Label(title_bar, text="Calculator", fg="white", bg="black", font=("Helvetica", 12))
        title_label.pack(side="left", padx=10)
        
    def create_buttons(self):
        buttons = [
            ("C", lambda: self.clear(), "#ff9f0a", "white"),
            ("+/-", lambda: self.negate(), "#ff9f0a", "white"),
            ("%", lambda: self.add_to_screen("%"), "#ff9f0a", "white"),
            ("/", lambda: self.add_to_screen("/"), "#ff9f0a", "white"),
            ("7", lambda: self.add_to_screen("7"), "#4d4d4d", "white"),
            ("8", lambda: self.add_to_screen("8"), "#4d4d4d", "white"),
            ("9", lambda: self.add_to_screen("9"), "#4d4d4d", "white"),
            ("*", lambda: self.add_to_screen("*"), "#ff9f0a", "white"),
            ("4", lambda: self.add_to_screen("4"), "#4d4d4d", "white"),
            ("5", lambda: self.add_to_screen("5"), "#4d4d4d", "white"),
            ("6", lambda: self.add_to_screen("6"), "#4d4d4d", "white"),
            ("-", lambda: self.add_to_screen("-"), "#ff9f0a", "white"),
            ("1", lambda: self.add_to_screen("1"), "#4d4d4d", "white"),
            ("2", lambda: self.add_to_screen("2"), "#4d4d4d", "white"),
            ("3", lambda: self.add_to_screen("3"), "#4d4d4d", "white"),
            ("+", lambda: self.add_to_screen("+"), "#ff9f0a", "white"),
            ("0", lambda: self.add_to_screen("0"), "#4d4d4d", "white"),
            (".", lambda: self.add_to_screen("."), "#4d4d4d", "white"),
            ("=", lambda: self.calculate(), "#ff9f0a", "white"),
        ]
        
        for i, (text, command, bg, fg) in enumerate(buttons):
            row, col = divmod(i, 4)
            create_button(self.root, text, command, bg, fg).grid(row=row + 2, column=col, sticky="nsew", padx=5, pady=5)
            
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            
    def add_to_screen(self, value):
        self.screen.insert(tk.END, value)
        
    def clear(self):
        self.screen.delete(0, tk.END)
        
    def delete_last(self):
        self.screen.delete(len(self.screen.get()) - 1)
        
    def negate(self):
        value = self.screen.get()
        if value:
            if value[0] == "-":
                self.screen.delete(0)
            else:
                self.screen.insert(0, "-")
        
    def calculate(self):
        try:
            result = eval(self.screen.get())
            self.clear()
            self.screen.insert(0, result)
        except:
            self.clear()
            self.screen.insert(0, "Error")
        
# Create the app instance
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()