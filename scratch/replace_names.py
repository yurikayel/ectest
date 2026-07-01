import re
import os

files = ['minuta_contrato.md', 'contrato_parceria.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace "Explochip" with "Explochip do Brasil" avoiding double "do Brasil"
    # Case insensitive match for Explochip. We will handle Title case and UPPER case.
    
    # 1. Title case: Explochip
    text = re.sub(r'Explochip(?!\s+do\s+Brasil)', 'Explochip do Brasil', text)
    # 2. UPPER case: EXPLOCHIP
    text = re.sub(r'EXPLOCHIP(?!\s+DO\s+BRASIL)', 'EXPLOCHIP DO BRASIL', text)
    
    # Replace "DNA Network" with "DNA Network Ltda."
    # We will avoid double Ltda.
    text = re.sub(r'DNA Network(?!\s+Ltda\.?)', 'DNA Network Ltda.', text)
    
    # Also "DNA NETWORK"
    text = re.sub(r'DNA NETWORK(?!\s+LTDA\.?)', 'DNA NETWORK LTDA.', text)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

print("Replacement complete.")
