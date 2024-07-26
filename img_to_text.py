import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image, ImageTk, ImageGrab
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'E:\CN\FCoder\face_json\face_ana\tessseract\tesseract.exe'  # Adjust this path as needed

class ImageToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Converter")

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="lightgray")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.select_image)

        self.paste_button = tk.Button(self.root, text="Paste Image from Clipboard", command=self.paste_image)
        self.paste_button.pack(pady=10)

        self.text_area = Text(self.root, wrap="word")
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)

    def select_image(self, event):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            self.display_image(file_path)
            self.extract_text(file_path)

    def paste_image(self):
        try:
            image = ImageGrab.grabclipboard()
            if isinstance(image, Image.Image):
                self.display_image(image)
                self.extract_text(image)
            else:
                self.show_error("No image found in clipboard.")
        except Exception as e:
            self.show_error(f"Error pasting image: {e}")

    def display_image(self, image):
        if isinstance(image, str):
            image = Image.open(image)
        self.img_tk = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img_tk)

    def extract_text(self, image):
        if isinstance(image, str):
            image = Image.open(image)
        text = pytesseract.image_to_string(image)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, text)

    def show_error(self, message):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, message)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextApp(root)
    root.mainloop()
