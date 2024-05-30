import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("262x350")
        self.root.resizable(False, False) 
        self.entry = tk.Entry(self.root, width=20, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        window_width = 262
        window_height = 350
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")


        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C' 
        ]
        
        row = 1
        col = 0
        for button in buttons:
            if button == 'C':
                tk.Button(self.root, text=button, width=5, height=2, font=("Arial", 12),
                          command=self.clear_entry, bg="red", fg="white").grid(row=row, column=col, padx=5, pady=5)
            elif button == '=':
                tk.Button(self.root, text=button, width=5, height=2, font=("Arial", 12),
                          command=lambda button=button: self.button_click(button), bg="green", fg="white").grid(row=row, column=col, padx=5, pady=5)
            elif button in ['+', '-', '*', '/']:
                tk.Button(self.root, text=button, width=5, height=2, font=("Arial", 12),
                          command=lambda button=button: self.button_click(button), bg="orange", fg="white").grid(row=row, column=col, padx=5, pady=5)
            else:
                tk.Button(self.root, text=button, width=5, height=2, font=("Arial", 12),
                          command=lambda button=button: self.button_click(button), bg="light blue", fg="black").grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def button_click(self, button):
        current = self.entry.get()
        if button == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)
    
    def clear_entry(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
