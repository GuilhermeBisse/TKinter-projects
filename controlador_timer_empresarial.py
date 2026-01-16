from tkinter import *
from tkinter import ttk


class Timer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.tempo = 0
        self.rodando = False
        self.comecou = False

        self.time_var = IntVar()

        Label(self, text="Tempo (s):").grid(row=0, column=0)
        Entry(self, textvariable=self.time_var, width=8).grid(row=0, column=1)

        self.lbl_time = ttk.Label(self, text="00:00", width=7)
        self.lbl_time.grid(row=0, column=2, padx=5)

        Button(self, text="Iniciar", command=self.iniciar).grid(row=0, column=3)
        Button(self, text="Parar", command=self.parar).grid(row=0, column=4)
        Button(self, text="Resetar", command=self.resetar).grid(row=0, column=5)

        self.grid(pady=5, sticky="w")

    def atualizar(self):
        if self.rodando and self.tempo >= 0:
            minutos = self.tempo // 60
            segundos = self.tempo % 60
            self.lbl_time.config(text=f"{minutos:02}:{segundos:02}")

            if self.tempo == 0:
                self.rodando = False
                return

            self.tempo -= 1
            self.after(1000, self.atualizar)

    def iniciar(self):
        if not self.rodando and not self.comecou:
            self.tempo = self.time_var.get()
            self.comecou = True
            self.rodando = True
            self.atualizar()
        elif not self.rodando and self.comecou:
            self.rodando = True
            self.atualizar()

    def parar(self):
        self.rodando = False

    def resetar(self):
        self.rodando = False
        self.comecou = False
        self.tempo = self.time_var.get()
        self.lbl_time.config(text="00:00")


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Contador empresarial independente")
        self.geometry("600x400")

        Button(self, text="Adicionar cronômetro", command=self.adicionar_cronometro).pack(pady=10)

        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

    def adicionar_cronometro(self):
        Timer(self.container)


if __name__ == "__main__":
    App().mainloop()
