import json

def generate_html_string(json_data):
    data = json.loads(json_data)
    
    layout = data.get("layout", [])
    content = data.get("content", {})
    styles = data.get("styles", {})
    resolution = data.get("resolution", {})
    
    if not resolution or "width" not in resolution or "height" not in resolution:
        raise ValueError("Missing resolution information. Please provide { width, height }.")
    
    screen_width = int(resolution["width"])
    screen_height = int(resolution["height"])
    num_rows = len(layout)
    num_cols = len(layout[0])
    
    cell_height = screen_height // num_rows
    cell_width = screen_width // num_cols
    
    elements_html = ""
    tag_set = set()
    merged_elements = {}
    
    for i in range(num_rows):
        for j in range(num_cols):
            key = layout[i][j]
            if not key:
                continue
            
            tag = key.split(".")[0]
            tag_set.add(tag)
            
            if key not in merged_elements:
                merged_elements[key] = {
                    "minRow": i,
                    "maxRow": i,
                    "minCol": j,
                    "maxCol": j,
                    "tag": tag,
                    "innerContent": content.get(key, ""),
                    "styles": styles.get(key, ""),
                }
            else:
                merged_elements[key]["maxRow"] = max(merged_elements[key]["maxRow"], i)
                merged_elements[key]["maxCol"] = max(merged_elements[key]["maxCol"], j)
    
    for key, el in merged_elements.items():
        top = el["minRow"] * cell_height
        left = el["minCol"] * cell_width
        width = (el["maxCol"] - el["minCol"] + 1) * cell_width
        height = (el["maxRow"] - el["minRow"] + 1) * cell_height
        
        merged_styles = (
            f"position: absolute; top: {top}px; left: {left}px; width: {width}px; height: {height}px; "
            f"margin: 0; display: block; {el['styles']}"
        )
        
        elements_html += f'<{el["tag"]} style="{merged_styles}">{el["innerContent"]}</{el["tag"]}>'
    
    custom_tags_rule = ", ".join(tag_set) + " { display: block; }"
    
    html_string = f'''
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Generated HTML</title>
        <style>
          html, body {{
            margin: 0;
            padding: 0;
            overflow: hidden;
            width: {screen_width}px;
            height: {screen_height}px;
          }}
          .container {{
            position: fixed;
            top: 0;
            left: 0;
            width: {screen_width}px;
            height: {screen_height}px;
          }}
          {custom_tags_rule}
        </style>
      </head>
      <body>
        <div class="container">
          {elements_html}
        </div>
      </body>
    </html>
    '''
    
    return html_string

