# Reference: https://realpython.com/python-gui-tkinter/

import tkinter as tk
from tkinter import scrolledtext
from io import StringIO
import contextlib

from Compi.parser import compile_code
from VM.virtualMachine import *
from VM.Memory import Memory

def compile_and_run():
    source_code = txt_edit.get("1.0", tk.END).strip()
    output_stream = StringIO()
    
    with contextlib.redirect_stdout(output_stream):
        try:
            # Send the source code to compile
            cte_directory, quadruples = compile_code(source_code)
            
            # Initialize memory with contants directory
            memory = Memory()
            memory.initialize_constants(cte_directory)
            
            # Execute quadruples and output array
            output = execute_quadruples(quadruples, memory)

            # Print the output
            for line in output:
                print(line)

        except Exception as e:
            print(e)
    

    execution_output = output_stream.getvalue()
    
    output_console.config(state='normal')
    output_console.delete("1.0", tk.END)
    output_console.insert(tk.END, execution_output)
    output_console.config(state='disabled')

window = tk.Tk()
window.title("Little Duck")

window.rowconfigure(0, minsize=400, weight=1)
window.rowconfigure(1, minsize=200, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_run = tk.Button(frm_buttons, text="Run Code", command=compile_and_run)

output_console = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled', height=10)

btn_run.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
output_console.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

window.mainloop()