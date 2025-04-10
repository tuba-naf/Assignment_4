import tkinter as tk

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("Canvas")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack()
        self.last_click_x = 0
        self.last_click_y = 0
        self.clicked = False
        self.canvas.bind('<Button-1>', self._on_click)
        
    def _on_click(self, event):
        self.last_click_x = event.x
        self.last_click_y = event.y
        self.clicked = True
        
    def get_mouse_x(self):
        return self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        
    def get_mouse_y(self):
        return self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        
    def get_last_click(self):
        return self.last_click_x, self.last_click_y
        
    def wait_for_click(self):
        self.clicked = False
        while not self.clicked:
            self.root.update()
        
    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        
    def moveto(self, item, x, y):
        self.canvas.coords(item, x, y, x + 20, y + 20)
        
    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)
        
    def set_color(self, item, color):
        self.canvas.itemconfig(item, fill=color)
        
    def update(self):
        self.root.update()
        
    def mainloop(self):
        self.root.mainloop() 