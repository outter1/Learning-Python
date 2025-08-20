import tkinter as tk
from datetime import datetime, timedelta

class Relogio:
    def __init__(self):
        self.horario = datetime.now()

    def mostrar_horario(self):
        return self.horario.strftime("%H:%M:%S")

    def ajustar_horario(self, horas=0, minutos=0, segundos=0):
        self.horario += timedelta(hours=horas, minutes=minutos, seconds=segundos)

    def resetar_para_horario_atual(self):
        self.horario = datetime.now()


# Funções para o front-end
def atualizar_horario():
    # Incrementa o horário do relógio em 1 segundo
    relogio.horario += timedelta(seconds=1)
    # Atualiza o texto do rótulo com o horário atual
    relogio_label.config(text=relogio.mostrar_horario())
    # Chama a função novamente após 1 segundo
    root.after(1000, atualizar_horario)

def ajustar_horario():
    try:
        horas = int(horas_entry.get()) if horas_entry.get() else 0
        minutos = int(minutos_entry.get()) if minutos_entry.get() else 0
        segundos = int(segundos_entry.get()) if segundos_entry.get() else 0
        relogio.ajustar_horario(horas, minutos, segundos)
        status_label.config(text="Horário ajustado com sucesso!", fg="gold")
    except ValueError:
        status_label.config(text="Erro: Insira valores válidos!", fg="red")

def resetar_horario():
    relogio.resetar_para_horario_atual()
    status_label.config(text="Horário resetado para o atual!", fg="gold")


# Instância do relógio
relogio = Relogio()

# Configuração do front-end
root = tk.Tk()
root.title("Relógio Digital")
root.geometry("400x300")
root.configure(bg="white")  # Fundo branco

# Estilo do relógio
relogio_label = tk.Label(root, text=relogio.mostrar_horario(), font=("Helvetica", 48), fg="red", bg="white")  # Números vermelhos
relogio_label.pack(pady=20)

# Entradas para ajustar o horário
ajuste_frame = tk.Frame(root, bg="white")
ajuste_frame.pack(pady=10)

tk.Label(ajuste_frame, text="Horas:", font=("Helvetica", 12), fg="gold", bg="white").grid(row=0, column=0, padx=5)  # Texto dourado
horas_entry = tk.Entry(ajuste_frame, width=5)
horas_entry.grid(row=0, column=1, padx=5)

tk.Label(ajuste_frame, text="Minutos:", font=("Helvetica", 12), fg="gold", bg="white").grid(row=0, column=2, padx=5)  # Texto dourado
minutos_entry = tk.Entry(ajuste_frame, width=5)
minutos_entry.grid(row=0, column=3, padx=5)

tk.Label(ajuste_frame, text="Segundos:", font=("Helvetica", 12), fg="gold", bg="white").grid(row=0, column=4, padx=5)  # Texto dourado
segundos_entry = tk.Entry(ajuste_frame, width=5)
segundos_entry.grid(row=0, column=5, padx=5)

# Botões
botao_ajustar = tk.Button(root, text="Ajustar Horário", command=ajustar_horario, bg="gold", fg="black", font=("Helvetica", 12))  # Botão dourado
botao_ajustar.pack(pady=10)

botao_resetar = tk.Button(root, text="Resetar para Atual", command=resetar_horario, bg="gold", fg="black", font=("Helvetica", 12))  # Botão dourado
botao_resetar.pack(pady=5)

# Status
status_label = tk.Label(root, text="", font=("Helvetica", 12), fg="gold", bg="white")  # Texto dourado
status_label.pack(pady=10)

# Atualiza o relógio automaticamente
atualizar_horario()

# Inicia o loop da interface gráfica
root.mainloop()