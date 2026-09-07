import tkinter as tk                                                                                                # importiere tkinter und random für GUI und random Fragen
import random

class QuizApp:                                                                                                      # Klasse QuizApp wird erstellt

    fragen_liste = {                                                                                                # Listen für die Fragen und dazugehörigen Antworten werden erstellt
              "LVL1": [
            {"frage": "Welche Farbe hat der Himmel?", "antwort": "Blau"},
            {"frage": "Was machen Hunde?", "antwort": "Bellen"},
            {"frage": "Wie viele Tage hat eine Woche?", "antwort": "7"},
            {"frage": "Welche Farbe hat Gras?", "antwort": "Grün"},
            {"frage": "Wie viele Beine hat eine Spinne?", "antwort": "8"},
            {"frage": "Was ist die Hauptstadt von Deutschland?", "antwort": "Berlin"},
            {"frage": "Wie viele Monate hat ein Jahr?", "antwort": "12"},
            {"frage": "Welches Tier sagt Muh?", "antwort": "Kuh"},
            {"frage": "Wie viele Finger hat eine Hand?", "antwort": "5"},
            {"frage": "Welche Farbe hat eine Banane?", "antwort": "Gelb"},
        ],
        "LVL2": [
            {"frage": "Wer ist Weltmeister im Fußball 2022 geworden?", "antwort": "Argentinien"},
            {"frage": "Wie viele Kontinente gibt es?", "antwort": "7"},
            {"frage": "Was ist die Hauptstadt von Frankreich?", "antwort": "Paris"},
            {"frage": "Wie viele Planeten hat unser Sonnensystem?", "antwort": "8"},
            {"frage": "Welches Element hat das Symbol O?", "antwort": "Sauerstoff"},
            {"frage": "Wer schrieb Faust?", "antwort": "Goethe"},
            {"frage": "Wie viele Saiten hat eine klassische Gitarre?", "antwort": "6"},
            {"frage": "Was ist die Hauptstadt von Italien?", "antwort": "Rom"},
            {"frage": "In welchem Jahr fiel die Berliner Mauer?", "antwort": "1989"},
            {"frage": "Wie heißt der längste Fluss Deutschlands?", "antwort": "Rhein"},
        ],
        "LVL3": [
            {"frage": "Wer ist der aktuelle Bundeskanzler Deutschlands?", "antwort": "Merz"},
            {"frage": "Wie viele Knochen hat ein erwachsener Mensch?", "antwort": "206"},
            {"frage": "Welcher Planet ist der Sonne am nächsten?", "antwort": "Merkur"},
            {"frage": "Wer malte die Mona Lisa?", "antwort": "da Vinci"},
            {"frage": "In welchem Jahr begann der Zweite Weltkrieg?", "antwort": "1939"},
            {"frage": "Wie heißt die Hauptstadt von Australien?", "antwort": "Canberra"},
            {"frage": "Welches chemische Element hat die Ordnungszahl 1?", "antwort": "Wasserstoff"},
            {"frage": "Wer komponierte die 9. Sinfonie?", "antwort": "Beethoven"},
            {"frage": "Wie viele Zeitzonen hat Russland?", "antwort": "11"},
            {"frage": "Welches Land hat die meisten Einwohner der Welt?", "antwort": "Indien"},
        ],
        "LVL4": [
            {"frage": "Wer war der erste Bundeskanzler der BRD?", "antwort": "Adenauer"},
            {"frage": "In welchem Jahr wurde die UNO gegründet?", "antwort": "1945"},
            {"frage": "Wie heißt die Hauptstadt von Kasachstan?", "antwort": "Astana"},
            {"frage": "Wer entwickelte die allgemeine Relativitätstheorie?", "antwort": "Einstein"},
            {"frage": "Wie viele Herzkammern hat der Mensch?", "antwort": "4"},
            {"frage": "Welcher Fluss ist der längste der Welt?", "antwort": "Nil"},
            {"frage": "In welchem Jahrhundert lebte Johann Sebastian Bach?", "antwort": "18. Jahrhundert"},
            {"frage": "Wie heißt das kleinste Land der Welt?", "antwort": "Vatikanstadt"},
            {"frage": "Wer schrieb den Roman Der Prozess?", "antwort": "Kafka"},
            {"frage": "Welches Gas macht den größten Anteil der Erdatmosphäre aus?", "antwort": "Stickstoff"},
        ],
        "LVL5": [
            {"frage": "Wer war Bundeskanzler während der deutschen Wiedervereinigung?", "antwort": "Kohl"},
            {"frage": "In welchem Jahr wurde die Relativitätstheorie veröffentlicht?", "antwort": "1905"},
            {"frage": "Wie heißt die Hauptstadt von Myanmar?", "antwort": "Naypyidaw"},
            {"frage": "Wer entdeckte das Penicillin?", "antwort": "Alexander Fleming"},
            {"frage": "Welcher Vertrag beendete den Ersten Weltkrieg?", "antwort": "Vertrag von Versailles"},
            {"frage": "Wie heißt das schwerste natürlich vorkommende chemische Element?", "antwort": "Uran"},
            {"frage": "Wer war der letzte Zar Russlands?", "antwort": "Nikolaus II."},
            {"frage": "In welchem Jahr wurde die Europäische Union gegründet?", "antwort": "1993"},
            {"frage": "Wie heißt der Erfinder des World Wide Web?", "antwort": "Berners-Lee"},
            {"frage": "Welche Schlacht gilt als Wendepunkt des Zweiten Weltkriegs an der Ostfront?", "antwort": "Stalingrad"},
        ],
    }

    def __init__(self, root):                                                                                       # __innit__ Funktion wird erstellt und variablen bestimmt
        self.root = root                                                                                            # Startfenster der App wird aufgebaut
        self.level = 1
        self.lives = 3
        self.joker = 2
        self.aktuelle_frage = None
        self.gestellte_fragen = {lvl: set() for lvl in self.fragen_liste}
        self.root.title("Quiz App")
        self.root.geometry("600x600")
        self.root.minsize(600, 600)
        self.root.maxsize(600, 600)

        self.root.columnconfigure(0, weight=1)                                                                      # Gitternetz wird erstellt um die Anordnung der einzelnen Elemente besser zu steuern
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=2)
        self.root.rowconfigure(2, weight=1)

        self.label_start = tk.Label(self.root, text="Willst du ein Spiel spielen?", font=("Gothic", 20), width=30, height=8)
        self.label_start.grid(row=0, column=1, padx=20)
        self.button_start = tk.Button(self.root, text="Start", font=("Gothic", 15), command=self.open_new_window, width=20, height=5)
        self.button_start.grid(row=1, column=1, padx=20)

    def open_new_window(self):                                                                                      # Das neue Fenster in dem gespielt wird, wird erstellt und definiert. Das alte wird zerstört!

        self.root.withdraw()

        new_window = tk.Toplevel(self.root)
        new_window.protocol("WM_DELETE_WINDOW", self.root.destroy)
        new_window.title("Quiz App")
        new_window.geometry("600x600")
        new_window.minsize(600, 600)
        new_window.maxsize(600, 600)

        frame_top = tk.Frame(new_window)
        frame_top.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

        self.label_lives = tk.Label(frame_top, text=f"Lives: {self.lives}", width=10, height=5)                     # Nutzeroberfläche wird auf das vorher erstellte Gitternetz gesetzt. Gitternetz wird vorher in mehrere Frames unterteilt.
        self.label_lives.grid(row=0, column=0, padx=10, pady=10)
        self.label_level = tk.Label(frame_top, text=f"LVL: {self.level}", width=10, height=5)
        self.label_level.grid(row=0, column=1, padx=10,pady=5)
        self.label_joker = tk.Label(frame_top, text=f"Joker: {self.joker}", width=10, height=5)
        self.label_joker.grid(row=0, column=2, padx=10,pady=10)
        self.label_frage = tk.Label(frame_top, text="Frage:", width=50, height=5)
        self.label_frage.grid(row=1, column=1, pady=5)

        frame_middle = tk.Frame(new_window)
        frame_middle.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

        self.antwort_var = tk.StringVar()
        self.entry = tk.Entry(frame_middle, textvariable=self.antwort_var, width=70)
        self.entry.bind("<Return>", lambda event: self.antwort_pruefen())
        self.entry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, ipady=10, ipadx=10)

        frame_bottom = tk.Frame(new_window)
        frame_bottom.grid(row=5, column=0, columnspan=3, padx=20, pady=20)

        button_enter = tk.Button(frame_bottom, text="Enter", command=self.antwort_pruefen, width=20, height=5)
        button_enter.grid(row=0, column=0, padx=20, pady=10)
        button_anderefrage = tk.Button(frame_bottom, text="Andere Frage", command=self.andere_frage, width=20, height=5)
        button_anderefrage.grid(row=0, column=1, padx=20, pady=10)

        self.neue_frage()

    def neue_frage(self):                                                                                           # Neue Frage wird generiert. Abhängig von LVL wird aus einem anderen Fragenpool geschöpft
        level_key = f"LVL{self.level}"
        fragen = self.fragen_liste.get(level_key,[])

        if not fragen:
            self.label_frage.config(text=f"Keine Fragen für {level_key} vorhanden.")
            self.aktuelle_frage = None
            return

        gestellt = self.gestellte_fragen[level_key]                                                                 # Sorgt dafür das die gleiche Frage nicht zufällig nochmal gestellt werden

        if len(gestellt) >= len(fragen):
            gestellt.clear()

        verbleibende = [f for f in fragen if f["frage"] not in gestellt]
        self.aktuelle_frage = random.choice(verbleibende)
        gestellt.add(self.aktuelle_frage["frage"])
        self.label_frage.config(text=self.aktuelle_frage["frage"])
        self.antwort_var.set("")

    def antwort_pruefen(self):                                                                                      # Antwort wird geprüft und mit den Einträgen verglichen
        if self.aktuelle_frage is None:
            return

        richtig = self.aktuelle_frage["antwort"].strip().lower()
        eingabe = self.antwort_var.get().strip().lower()

        if eingabe == richtig:                                                                                      # Falls die Frage richtig ist, LVL UP! Ansonsten neue Frage und Lebenscounter - 1
            self.label_frage.config(text="Richtig!")
            self.root.after(50, self.level_aufsteigen)
        else:
            self.label_frage.config(text="Falsch du Loser!")
            self.lives -= 1
            self.label_lives.config(text=f"Lives: {self.lives}")

            if self.lives == 0:
                self.label_frage.config(text="GAME OVER!")
                self.root.after(50, self.root.destroy)

        self.neue_frage()

    def level_aufsteigen(self):                                                                                     # Solange MaxLVL nicht erreicht ist, LVL UP!
        if self.level < 6:
            self.level += 1
            self.label_level.config(text=f"LVL: {self.level}")
            self.neue_frage()

    def andere_frage(self):                                                                                         # Solange Joker vorhanden, neue Frage aus selben Fragenpool stellen
        if self.joker > 0:
            self.joker -= 1
            self.label_joker.config(text=f"Joker: {self.joker}")
            self.neue_frage()


if __name__ == "__main__":                                                                                          # Lässt alles laufen solange der Name übereinstimmt (Basically ewig also)
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()