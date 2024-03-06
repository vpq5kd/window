import tkinter as tk
import time

class Window:
    def __init__(self, root, text, wpm):
        self.root = root
        self.text = text
        self.wpm = wpm
        self.index = 0

        #text portion
        self.text_label = tk.Label(root, text="", font=("Arial", 12),anchor="n", fg="black", bg="grey")
        self.text_label.pack(fill="both",expand=True)


        self.start_typing()

    def start_typing(self):
       self.typing_speed = 60000 / self.wpm
       self.write_word()

    def write_word(self):
        word = self.text[self.index]
        self.text_label.config(text=self.text_label["text"] + word)
        self.index += 1
        if self.index < len(self.text):
            self.root.after(int(self.typing_speed), self.write_word)
        # else:
        #     self.fade_in_image()

    # def fade_in_image(self, opacity=0):
    #     if opacity < 1:
    #         self.image_label.config(bg="white", bd=0, highlightthickness=0)
    #         self.image_label.tkraise()
    #         self.root.attributes("-alpha", opacity)
    #         opacity += 0.05
    #         self.root.after(50, lambda: self.fade_in_image(opacity))
    #     else:
    #         self.root.attributes("-alpha", 1)
def main():
    root = tk.Tk()
    root.geometry("500x300")
    root.title("today is not your birthday!")
    text = "Dear Chloe,\n Today is not your birthday, so this isn't a birthday card. \n And, therefore, I am NOT celebrating your birthday ;). But, if it was,\n it would be the perfect oppurtunity to tell you that you are an amazing,\n kind, funny, smart, beautiful person and I am so so so grateful to have\n you in my life :) . Wishing you the absolute best for this year \n and all the years to come!!!"
    wpm = 800
    window = Window(root, text, wpm)
    root.mainloop()
if __name__ == "__main__":
    main()
