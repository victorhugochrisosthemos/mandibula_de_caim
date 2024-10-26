import PyPDF2

# Abrir o arquivo PDF
with open('A Mandibula de Caim.pdf', 'rb') as pdf_file:
    # Criar um leitor de PDF
    leitor_pdf = PyPDF2.PdfReader(pdf_file)

    # Contar o número de páginas
    numero_de_paginas = len(leitor_pdf.pages)

    # Lista para armazenar o texto de cada página
    texto = []

    # Iterar pelas páginas e extrair o texto a partir da página 10, porque o livro tem considerações iniciais
    for pagina in range(9, numero_de_paginas):  # Começa da página 10
        pagina_atual = leitor_pdf.pages[pagina]
        texto_pagina = pagina_atual.extract_text()

        # Verifica se o texto extraído não é None
        if texto_pagina:
            texto.append(texto_pagina)  # Adiciona o texto extraído à lista

# Exibe a quantidade de páginas processadas e o número de blocos de texto
print(f"Número de blocos de texto extraídos: {len(texto)}")

# Opcional: para ver o texto extraído
#print("\n".join(texto))

#print(texto[0])
