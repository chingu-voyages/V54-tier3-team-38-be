def generate_html(data):
    layout = data.get("layout")
    content = data.get("content", {})
    styles = data.get("styles", {})
    resolution = data.get("resolution")

    if not resolution or "width" not in resolution or "height" not in resolution:
        raise ValueError("Missing resolution information. Please provide { width, height }.")

    screen_width = resolution["width"]
    screen_height = resolution["height"]
    num_rows = len(layout)
    num_cols = len(layout[0])
    cell_height = screen_height // num_rows
    cell_width = screen_width // num_cols

    elements_html = ""
    tag_set = set()

    # First pass: calculate bounding boxes for merged elements
    bounding_boxes = {}
    for i in range(num_rows):
        for j in range(num_cols):
            key = layout[i][j]
            if not key:
                continue
            if key not in bounding_boxes:
                bounding_boxes[key] = {
                    "min_row": i,
                    "max_row": i,
                    "min_col": j,
                    "max_col": j,
                }
            else:
                bounding_boxes[key]["min_row"] = min(bounding_boxes[key]["min_row"], i)
                bounding_boxes[key]["max_row"] = max(bounding_boxes[key]["max_row"], i)
                bounding_boxes[key]["min_col"] = min(bounding_boxes[key]["min_col"], j)
                bounding_boxes[key]["max_col"] = max(bounding_boxes[key]["max_col"], j)

    rendered_keys = set()

    # Second pass: render cells and merged elements
    for i in range(num_rows):
        for j in range(num_cols):
            key = layout[i][j]
            # Calculate cell position
            cell_top = i * cell_height
            cell_left = j * cell_width
            if not key:
                # Render an empty cell to preserve grid structure
                style = f"""
                    position: absolute;
                    top: {cell_top}px;
                    left: {cell_left}px;
                    width: {cell_width}px;
                    height: {cell_height}px;
                """
                elements_html += f'<div style="{style}"></div>'
                continue

            if key in rendered_keys:
                continue  # Already rendered this merged element

            box = bounding_boxes[key]
            tag = key.split(".")[0]
            tag_set.add(tag)

            merged_top = box["min_row"] * cell_height
            merged_left = box["min_col"] * cell_width
            merged_width = (box["max_col"] - box["min_col"] + 1) * cell_width
            merged_height = (box["max_row"] - box["min_row"] + 1) * cell_height

            user_style = styles.get(key, "")
            # Base style to force proper absolute positioning and dimensions.
            base_style = f"""
                position: absolute;
                top: {merged_top}px;
                left: {merged_left}px;
                width: {merged_width}px;
                height: {merged_height}px;
                margin: 0;
                display: block;
            """
            # Concatenate user style first so our rules override any conflicting properties.
            final_style = user_style + " " + base_style
            inner = content.get(key, "")
            elements_html += f'<{tag} style="{final_style}">{inner}</{tag}>'
            rendered_keys.add(key)

    custom_tags_rule = ", ".join(tag_set) + " { display: block; }"

    # Note: Instead of using fixed positioning and overflow:hidden,
    # we now let the document scroll if the resolution is larger than the viewport.
    final_html = f"""<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated HTML Layout</title>
    <style>
      html, body {{
        margin: 0;
        padding: 0;
        overflow: auto;
      }}
      /* The container is sized according to the passed resolution.
         Since it's relative, if it's larger than the viewport, scrollbars will appear. */
      .container {{
        position: relative;
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
</html>"""

    return final_html
