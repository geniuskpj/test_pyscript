import js
from js import Option,console,document
from pyodide.ffi import create_proxy
import asyncio
def capture(e):
    console.log("Attempted file upload: " + e.target.value)
    file_list = e.target.files
    first_item = file_list.item(0)
    document.getElementById('output').appendChild(first_item)
    return js.getPixels(first_item)

document.getElementById('cam').addEventListener('change',capture)

