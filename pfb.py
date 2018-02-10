from bottle import route, run
pfb_form = """
<html>
 <body>
   <h1>Form Page</h1>
   
   <form method=GET>
    <fieldset>
   <legend>Welcome to Pico Fermi Bagel</legend>
   <ul>
    <li>Name: <input name='first'></li>
    <li>Digits for Pico Fermi Bagel:  <input name='last'></li>
   </ul>
   <input type='submit' value='Submit Form'>
   </fieldset>
   </form>
   
 </body>
</html>
"""

@route('/pfb')
def hello():
    return pfb_form

run(host='localhost', port=8080, debug=True)


