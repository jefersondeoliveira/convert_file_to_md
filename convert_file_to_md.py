import os
from docling.document_converter import DocumentConverter

source = "document.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)

# Gera o nome do arquivo de saída substituindo .pdf por .md
output_file = os.path.splitext(source)[0] + ".md"

# Salva o resultado em um arquivo .md
with open(output_file, "w", encoding="utf-8") as f:
    f.write(result.document.export_to_markdown())

print(f"Arquivo salvo como: {output_file}")