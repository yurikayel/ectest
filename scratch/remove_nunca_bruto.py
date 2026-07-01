import os
import glob

def remove_nunca_bruto(folder):
    files = glob.glob(os.path.join(folder, '*.md')) + glob.glob(os.path.join(folder, '*.html'))
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # Replace "(nunca Bruto) " and "(nunca Bruto)"
        original_text = text
        text = text.replace(' (nunca Bruto)', '')
        text = text.replace('(nunca Bruto)', '')
            
        if text != original_text:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)
                
remove_nunca_bruto('.')
print("Removed '(nunca Bruto)' from all files.")
