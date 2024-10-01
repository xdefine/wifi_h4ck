import subprocess
import tkinter as tk
import tkinter as ttk

def scanner_reseax_wifi():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Erreur lors du scan : {e}"

def afficher_reseaux():
    result = scanner_reseax_wifi()
    texte_affichage.delete(1.0, tk.END)
    texte_affichage.insert(tk.END, result)

fenetre = tk.Tk()
fenetre.title("Wi-Fi by xDefine")
fenetre.geometry("600x400")

titre = ttk.Label(fenetre, text="Liste des réseaux Wi-Fi", font=("Helvetica", 16, "bold"))
titre.pack(pady=10)

btn_scanner = ttk.Button(fenetre, text="Scanner les réseaux", command=afficher_reseaux)
btn_scanner.pack(pady=10)

texte_affichage = tk.Text(fenetre, wrap=tk.WORD, height=15, width=70)
texte_affichage.pack(pady=10)

fenetre.mainloop()
