# Conversor de arquivos CSV para TXT
A conversão de um arquivo CSV para um arquivo de texto simples é um procedimento relativamente direto, já que um arquivo CSV (Comma-Separated Values) é, por essência, um arquivo de texto estruturado com valores separados por vírgulas. No entanto, para preservar a confidencialidade dos dados e evitar o risco de vazamento ao utilizar sites online, decidi criar um script em Python utilizando a biblioteca Tkinter para uma interface gráfica. Isso me permite realizar a conversão de forma segura e local, sem a necessidade de recorrer a plataformas de terceiros que possam comprometer informações sensíveis

#### Bibliotecas Usadas:
**Tkinker** é usada para criar a interface gráfica.
**filedialog** é usado para exibir janelas de diálogo para abrir e salvar arquivos.
**csv** é usado para operações relacionadas a arquivos CSV.
**sys** é usado para interagir com o sistema operacional.

#### Função Usada:
convert_to_txt(): Esta função é chamada quando o botão "Converter CSV para TXT" é clicado. Ela abre uma janela de diálogo para selecionar um arquivo CSV, em seguida, pede um local para salvar o arquivo TXT convertido. Em seguida, lê o arquivo CSV, converte seu conteúdo para texto e salva o texto no arquivo TXT. Por fim, atualiza a interface gráfica com o resultado da operação. ╰(*°▽°*)╯

close_app(): Esta função é chamada quando o botão "Sair" é clicado. Ela fecha a janela principal (root) e sai do programa.

### Aos pouquinhos, vamos evoluindo!

![the-office-gif-9](https://github.com/mayumi1982/csv_txt1/assets/70608757/bfecef3b-624f-4cdc-b82c-2f7ca48f9e33)


