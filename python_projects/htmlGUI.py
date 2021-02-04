
import tkinter as tk     #Import all tkinter modules 
from tkinter import ttk
from tkinter import messagebox
import webbrowser


class MainApp:          #Main class to pass functions, create widgits and styles, used to pass information of functions to classes

    def __init__(self, master):
        master.title('Change your (HTML) body!')
        master.resizable(True, True)             #Able to resize GUI window, slight easy function changed by using TRUE not FALSE BOOLEAN

        self.style = ttk.Style()
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
       

        ttk.Label(self.frame_header, wraplength=500,                                       #Label widget, with some text
                  text=("In the field below, Enter some text to open a new webbrowser"),
                  justify='left').pack()

        self.frame_content = ttk.Frame(master)
        

        self.html_body = tk.Text(self.frame_content,                           #TEXT ENTRY widget
                                 width=78, height=40, font=('Arial', 10))
        self.html_body.pack()
        self.frame_content.pack()
        

        
   

        ttk.Button(self.frame_content, text='Submit',
                   command=self.submit).pack(expand='True', side='left') 
                                                                                  # SUBMIT & CLEAR BUTTON WIDGETS
        ttk.Button(self.frame_content, text='Clear', command=self.clear).pack(
            expand='True', side='right') 
       
        

    def Create_html(self, text):  #CREATE HTML Function used to pass text variable thru to the opening of a new web browser
        f=open("test.html","w")
        html_string="\
        <html>\n\
            <body>\n\
              <h1>\n\
              {}\n\
              <h1>\n\
            </body>\n\
        </html>".format(text)

        f.write(html_string)
        f.close()
        url ='test.html'
        webbrowser.open_new_tab(url)
        
        
    def submit(self):                                                   
        self.Create_html(self.html_body.get(1.0, 'end'))
        self.clear()
        messagebox.showinfo(title='Success!', message='Body text updated.')
 
                                                                                #BUTTON FUNCTIONS, these get information from the above BUTTON WIDGETS.
    def clear(self):
        self.html_body.delete(1.0, 'end')
        

if __name__ == '__main__':
    root = tk.Tk()
    MainApp = MainApp(root)
    root.mainloop()
