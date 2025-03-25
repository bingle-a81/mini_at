html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Каталог протетика</title>
</head>
<body>
    <table style="width: 100%" border="1">
      <tbody>
      {% for row in ls %}
      <tr>
          <td width="400"><img src="{{row[1]}}" alt="{{row[0]}}">          
          </td> 
          <td> {{row[0]}}
          </td>  
            </tr>
      {% endfor %}
      </tbody>
    </table>
</body>
</html>
"""