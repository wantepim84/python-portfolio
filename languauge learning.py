import tkinter as tk
from tkinter import messagebox
import random

class LanguageLearningApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Language Learning App")

        # Vocabulary data (replace with your own data)
        self.vocab_data = {
            "English": {
                "hello": "Hello",
                "goodbye": "Goodbye",
                "thank you": "Thank you",
                "house": "House",
                "dog": "Dog",
                "cat": "Cat",
                "friend": "Friend",
                "food": "Food",
                "sun": "Sun",
            },
            "Spanish": {
                "hello": "Hola",
                "goodbye": "Adiós",
                "thank you": "Gracias",
                "house": "Casa",
                "dog": "Perro",
                "cat": "Gato",
                "friend": "Amigo",
                "food": "Comida",
                "sun": "Sol",
            },
            "French": {
                "hello": "Bonjour",
                "goodbye": "Au revoir",
                "thank you": "Merci",
                "house": "Maison",
                "dog": "Chien",
                "cat": "Chat",
                "friend": "Ami",
                "food": "Nourriture",
                "sun": "Soleil",
            },
            "Italian": {
                "hello": "Ciao",
                "goodbye": "Arrivederci",
                "thank you": "Grazie",
                "house": "Casa",
                "dog": "Cane",
                "cat": "Gatto",
                "friend": "Amico",
                "food": "Cibo",
                "sun": "Sole",
            },
            "German": {
                "hello": "Hallo",
                "goodbye": "Auf Wiedersehen",
                "thank you": "Danke",
                "house": "Haus",
                "dog": "Hund",
                "cat": "Katze",
                "friend": "Freund",
                "food": "Essen",
                "sun": "Sonne",
            },
            "Japanese": {
                "hello": "こんにちは",
                "goodbye": "さようなら",
                "thank you": "ありがとう",
                "house": "家",
                "dog": "犬",
                "cat": "猫",
                "friend": "友達",
                "food": "食べ物",
                "sun": "太陽",
            },
            "Chinese": {
                "hello": "你好",
                "goodbye": "再见",
                "thank you": "谢谢",
                "house": "房子",
                "dog": "狗",
                "cat": "猫",
                "friend": "朋友",
                "food": "食物",
                "sun": "太阳",
            },
            "Russian": {
                "hello": "Привет",
                "goodbye": "До свидания",
                "thank you": "Спасибо",
                "house": "Дом",
                "dog": "Собака",
                "cat": "Кот",
                "friend": "Друг",
                "food": "Еда",
                "sun": "Солнце",
            },
            # Add more languages and words as needed
        }

        self.current_language = tk.StringVar()
        self.current_language.set("English")

        self.word_label = tk.Label(master, text="", font=("Helvetica", 20))
        self.word_label.pack(pady=20)

        self.language_menu = tk.OptionMenu(
            master, self.current_language, *self.vocab_data.keys())
        self.language_menu.pack()

        self.next_button = tk.Button(
            master, text="Next Word", command=self.show_next_word)
        self.next_button.pack(pady=10)

        self.show_next_word()  # Display the first word when the app starts

    def show_next_word(self):
        language = self.current_language.get()

        if language in self.vocab_data:
            words = list(self.vocab_data[language].keys())
            random_word = random.choice(words)
            translation = self.vocab_data[language][random_word]

            word_text = f"{language}: {random_word}\nTranslation: {translation}"
            self.word_label.config(text=word_text)
        else:
            messagebox.showwarning("Error", "Invalid language selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()
