import json
import time
from selenium import webdriver
import tkinter as tk
import threading

class Output():
    def __init__(self):
        self.outfile = open("log.log","a")
    def write(self, what):
        self.outfile.write(what)

class Operations():
    def run(self):
        for count in range(int(app.agents.get())):
            t = threading.Thread(target=self.browse)
            t.start()

    def browse(self):
        browser = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        for step in range(int(app.run.get())):
            for address in app.address.get().split(";"):
                browser.get(address)
                time.sleep(int(app.delay.get()))

                for element in app.elements.get().split(";"):
                    browser.find_element_by_css_selector(element).click()
                    output.write(json.dumps((address, step, element, time.time())))
                    time.sleep(int(app.delay.get()))
        browser.close()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.address_label = tk.Label(self)
        self.address_label["text"] = "Addresses: "
        self.address_label.grid(row=1, column=0, sticky='', pady=5, padx=5)
        self.address_value = tk.StringVar()
        self.address_value.set("https://www.youtube.com/watch?v=mMNZi2rXDEo;https://www.youtube.com/watch?v=mMNZi2rXDEo")
        self.address = tk.Entry(self, textvariable=self.address_value, width=70)
        self.address.grid(row=1, column=1, sticky='W', padx=5)

        self.run_label = tk.Label(self)
        self.run_label["text"] = "Runs: "
        self.run_label.grid(row=2, column=0, sticky='', padx=5)
        self.run_value = tk.StringVar()
        self.run_value.set("250")
        self.run = tk.Entry(self, textvariable=self.run_value, width=10)
        self.run.grid(row=2, column=1, sticky='W', pady=5, padx=5)

        self.delay_label = tk.Label(self)
        self.delay_label["text"] = "Delays: "
        self.delay_label.grid(row=3, column=0, sticky='', padx=5)
        self.delay_value = tk.StringVar()
        self.delay_value.set("2")
        self.delay = tk.Entry(self, textvariable=self.delay_value, width=10)
        self.delay.grid(row=3, column=1, sticky='W', pady=5, padx=5)

        self.agents_label = tk.Label(self)
        self.agents_label["text"] = "Agents: "
        self.agents_label.grid(row=4, column=0, sticky='', padx=5)
        self.agents_value = tk.StringVar()
        self.agents_value.set("1")
        self.agents = tk.Entry(self, textvariable=self.agents_value, width=10)
        self.agents.grid(row=4, column=1, sticky='W', pady=5, padx=5)

        self.elements_label = tk.Label(self)
        self.elements_label["text"] = "Elements: "
        self.elements_label.grid(row=5, column=0, sticky='', padx=5)
        self.elements_value = tk.StringVar()
        self.elements_value.set(".ytp-progress-bar;.ytp-progress-bar")
        self.elements = tk.Entry(self, textvariable=self.elements_value, width=70)
        self.elements.grid(row=5, column=1, sticky='W', pady=5, padx=5)

        self.send = tk.Button(self, text="Run", fg="green", command=operations.run)
        self.send.grid(row=6, column=1, sticky='WE', padx=5)

        self.quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
        self.quit.grid(row=7, column=1, sticky='WE', padx=5, pady=(5))

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("PySel Loadtester")
    operations = Operations()
    output = Output()
    app = Application(master=root)
    app.mainloop()
