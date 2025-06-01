import csv
import sys
import os

# Usage: python csv_to_lua.py input.csv output.lua

def csv_to_lua(input_csv, output_lua):
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        # Use csv.QUOTE_MINIMAL to preserve multiline fields
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    lua_lines = ["champion_card_meta_data = {"]
    for row in rows:
        key = row.get('Name', '').strip()
        if not key:
            continue
        lua_lines.append(f"  ['{key}'] = {{")
        for k, v in row.items():
            if k in ('Count', 'Image'):
                continue
            k_lua = k.replace('"', '\"')
            v = v.replace('\r\n', '\\n').replace('\n', '\\n').replace('"', '\"').strip()
            if v.isdigit():
                lua_lines.append(f"    ['{k_lua}'] = {v},")
            else:
                lua_lines.append(f'    ["{k_lua}"] = "{v}",')
        lua_lines.append("  },")
    lua_lines.append("}")

    with open(output_lua, 'w', encoding='utf-8') as outf:
        outf.write('\n'.join(lua_lines))

if __name__ == '__main__':
    file_name = "Champion stats.csv"
    output_file = "champion_stats.lua"
    csv_to_lua(file_name, output_file)
