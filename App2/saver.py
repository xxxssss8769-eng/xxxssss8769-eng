import json
from tkinter import filedialog


def format_summary(data: dict) -> str:
    doc = data.get('doctor', {})
    patients = data.get('patients', [])
    pats = data.get('pats', [])
    day = data.get('day')
    details = data.get('details', {})
    lines = [f"Doctor name: {doc.get('doctor')}    The clinic: {doc.get('clinic')}   The number: {doc.get('number')}"]
    lines.append(f"The date: {day}")
    lines.append('Patients:')
    for p in patients:
        lines.append(f'  - {p}')
    lines.append('\nPatients details:')
    for summary in pats:
        lines.append(f'  - {summary}')
    return '\n'.join(lines)


def save_summary(data: dict, as_json: bool = False):
    filetypes = [('JSON files', '*.json')] if as_json else [('Text files', '*.txt'), ('All files', '*.*')]
    path = filedialog.asksaveasfilename(defaultextension='.json' if as_json else '.txt', filetypes=filetypes)
    if not path:
        return False
    if as_json:
        with open(path, 'w', encoding='utf-8') as f:
            # write a JSON string explicitly (avoids some type-checker warnings)
            f.write(json.dumps(data, default=str, indent=2))
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(format_summary(data))
    return True
