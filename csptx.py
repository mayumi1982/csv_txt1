import tkinter as tk
from tkinter import filedialog
import csv
import sys

def convert_to_txt():
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo CSV",
        filetypes=[("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")]
    )

    if file_path:
        csv_file = open(file_path, 'r')  # Abre o arquivo CSV selecionado para leitura

        output_path = filedialog.asksaveasfilename(
            title="Salvar como",
            defaultextension=".txt",
            filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )

        if output_path:
            with open(output_path, 'w', newline='', encoding='utf-8') as txtfile:
                csv_reader = csv.reader(csv_file)  # Cria um leitor CSV

                for row in csv_reader:
                    # Escreve cada linha do arquivo CSV como uma linha no arquivo de texto
                    txtfile.write(','.join(row) + '\n')  # Separa os valores por vírgula

            csv_file.close()
            result_label.config(text="Arquivo CSV convertido para TXT e salvo em " + output_path, fg="green", font=("Arial", 10))
        else:
            result_label.config(text="Nenhum local de salvamento selecionado.", fg="red", font=("Arial", 10))

def close_app():
    root.destroy()
    sys.exit()

root = tk.Tk()
root.title("Conversor de CSV para TXT")

font_name = "Segoe UI"

label = tk.Label(root, text="Selecione um arquivo CSV para converter:", font=(font_name, 12))
label.pack()

convert_button = tk.Button(root, text="Converter CSV para TXT", command=convert_to_txt, font=(font_name, 10))
convert_button.pack()

result_label = tk.Label(root, font=(font_name, 10))
result_label.pack()

exit_button = tk.Button(root, text="Sair", command=root.destroy, font=(font_name, 10), bg="red", fg="white")
exit_button.pack(pady=10)

root.mainloop()
