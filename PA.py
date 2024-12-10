import tkinter as tk
from tkinter import ttk, messagebox


# Función para calcular la progresión aritmética
def calcular_pa():
    try:
        a1 = float(entry_a1.get())
        d = float(entry_d.get())
        n = int(entry_n.get())

        if n <= 0:
            raise ValueError("La cantidad de términos debe ser mayor que cero.")
        
        pa = [a1 + (i - 1) * d for i in range(1, n + 1)]
        
        # Mostrar los resultados
        result_text.set(
            f"Progresión Aritmética:\n{pa}\n\n"
            f"Fórmula del término general:\n"
            f"a_n = {a1} + (n-1) * {d}"
        )
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")


# Crear ventana principal
root = tk.Tk()
root.title("Calculadora de Progresión Aritmética")
root.geometry("500x400")
root.resizable(False, False)

# Estilo moderno
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Variables de entrada
entry_a1 = tk.StringVar()
entry_d = tk.StringVar()
entry_n = tk.StringVar()
result_text = tk.StringVar()

# Diseño de la interfaz
frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Primer término (a₁):").grid(row=0, column=0, sticky="w", pady=5)
ttk.Entry(frame, textvariable=entry_a1).grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Diferencia común (d):").grid(row=1, column=0, sticky="w", pady=5)
ttk.Entry(frame, textvariable=entry_d).grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Cantidad de términos (n):").grid(row=2, column=0, sticky="w", pady=5)
ttk.Entry(frame, textvariable=entry_n).grid(row=2, column=1, pady=5)

ttk.Button(frame, text="Calcular PA", command=calcular_pa).grid(row=3, column=0, columnspan=2, pady=20)

ttk.Label(frame, text="Resultado:", anchor="w").grid(row=4, column=0, columnspan=2, sticky="w")
ttk.Label(frame, textvariable=result_text, wraplength=400, background="white", relief="solid", anchor="w", padding=10).grid(
    row=5, column=0, columnspan=2, pady=5, sticky="ew"
)

# Iniciar la aplicación
root.mainloop()
