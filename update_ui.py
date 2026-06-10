import os
import re

css = """
/* Global Toast & Loader Styles */
#global-toast {
  position: fixed; bottom: 24px; right: 24px; background: #0b1c30; color: #fff; padding: 14px 22px;
  border-radius: 10px; font-size: 13px; font-weight: 500; z-index: 99999;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2); opacity: 0; pointer-events: none;
  transform: translateY(20px); transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex; align-items: center; gap: 10px;
}
#global-toast.show { opacity: 1; transform: translateY(0); }
#global-toast.success { background: #0f6e56; }
#global-toast.error { background: #e24b4a; }
.spinner-btn {
  display: inline-block; width: 14px; height: 14px;
  border: 2px solid rgba(255,255,255,0.4); border-top-color: #fff;
  border-radius: 50%; animation: spin 0.6s linear infinite; margin-right: 6px;
}
@keyframes spin { to { transform: rotate(360deg); } }
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add script tag if not exists
    if '<script src="ui.js"></script>' not in content:
        content = content.replace('</body>', '<script src="ui.js"></script>\n</body>')
        if '</body>' not in content:  # Fallback if no body tag
            content += '\n<script src="ui.js"></script>'

    # Replace window.location.href combinations
    content = re.sub(
        r'onclick="alert\(\'([^\']+)\'\);\s*window\.location\.href=\'([^\']+)\'"',
        r'onclick="simBtn(event, \'\1\', \'\2\')"',
        content
    )

    # Replace standalone alerts
    content = re.sub(
        r'onclick="alert\(\'([^\']+)\'\)"',
        r'onclick="simBtn(event, \'\1\')"',
        content
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("UI Update completed.")
