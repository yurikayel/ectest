import os

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

with open('funil.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace link with style tag
html_content = html_content.replace('<link rel="stylesheet" href="style.css">', f'<style>\n{css_content}\n</style>')

# Replace script with script tag inline
html_content = html_content.replace('<script src="funil.js"></script>', f'<script>\n{js_content}\n</script>')

# Save standalone file
with open('explochip_whatsapp.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created explochip_whatsapp.html with embedded CSS and JS! (No logo manipulation needed)")
