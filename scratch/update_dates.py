import os
import glob

def update_dates(folder):
    replacements = {
        '01/09/2026': '01/07/2026',
        '01 de setembro de 2026': '01 de julho de 2026',
        '31/08/2028': '30/06/2028',
        '31 de agosto de 2028': '30 de junho de 2028',
        '29/11/2026': '29/09/2026' # if 90 days from Sept to Nov, July to Sept is 29/09/2026
    }
    
    files = glob.glob(os.path.join(folder, '*.md')) + glob.glob(os.path.join(folder, '*.html'))
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            
        original_text = text
        for old, new in replacements.items():
            text = text.replace(old, new)
            
        if text != original_text:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)
                
update_dates('.')
print("Dates updated.")
