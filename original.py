import tkinter as tk
from tkinter import ttk
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import math

# def App(tk.Tk):
#     def __init__(self, title, window_dim):
#         super().__init__()
#         self.title(title)
#         self.bind('<Escape>', lambda event: window.quit())
        
#         screen_width = self.winfo_screenwidth()
#         screen_height = self.winfo_screenheight()
#         midpoint = (int(screen_width/2),int(screen_height/2))
#         offsetx = midpoint[0]-int(window_dim[0]/2)
#         offsety = midpoint[1]-int(window_dim[1]/2)
#         window.geometry(f'{window_dim[0]}x{window_dim[1]}+{offsetx}+{offsety}')

#         window.mainloop()

def update(*args):
    temp_x = axes.get_xlim()
    temp_y = axes.get_ylim()
    axes.clear()
    axes.set_xlim(temp_x[0],temp_x[1])
    axes.set_ylim(temp_y[0],temp_y[1])
    axes.grid(True)

    # Dependent Variables
    DepVars['c_1'] = k_1.get()/(1+e.get()+k_1.get())
    DepVars['v_1'] = (1-DepVars['c_1'])/(1+e.get())
    DepVars['s_1'] = e.get()*DepVars['v_1']
    DepVars['c_2'] = k_2.get()/(1+e.get()+k_2.get())
    DepVars['v_2'] = (1-DepVars['c_2'])/(1+e.get())
    DepVars['s_2'] = e.get()*DepVars['v_2']
    DepVars['b'] = 1-a.get()
    DepVars['golden_pi'] = 1/((0.5)*(DepVars['c_1']+DepVars['v_2']+((DepVars['c_1']-DepVars['v_2'])**2+4*DepVars['v_1']*DepVars['c_2'])**0.5))-1
    # Still need the j's

    DepVars['M_11'] = DepVars['c_1']
    DepVars['M_12'] = DepVars['c_2']
    DepVars['M_21'] = (DepVars['b']*DepVars['s_1']*DepVars['c_1']+DepVars['v_1'])/(1-DepVars['b']*DepVars['s_2'])
    DepVars['M_22'] = (DepVars['b']*DepVars['s_1']*DepVars['c_2']+DepVars['v_2'])/(1-DepVars['b']*DepVars['s_2'])
    # Still need the N's

    # I have to compute all of the eigenschtuff myself because the fucking numpy eigen function auto-orders the vectors, infuriating
    mu_1 = 0.5*(DepVars['M_11']+DepVars['M_22'] + np.sqrt((DepVars['M_11']-DepVars['M_22']) ** 2 + 4*DepVars['M_12']*DepVars['M_21']))
    mu_2 = 0.5*(DepVars['M_11']+DepVars['M_22'] - np.sqrt((DepVars['M_11']-DepVars['M_22']) ** 2 + 4*DepVars['M_12']*DepVars['M_21']))
    m_11 = 1
    m_12 = (mu_1-DepVars['M_11'])/DepVars['M_12']*m_11
    m_21 = 1
    m_22 = -(DepVars['M_11']-mu_2)/DepVars['M_12']*m_21
    P = np.array([[m_11,m_21],[m_12,m_22]])
    P_inverse = np.linalg.inv(P)
    y_vec = np.array([[y_1i.get()],[y_2i.get()]])
    eta_vec = np.matmul(P_inverse,y_vec)

    t_range = np.linspace(-3,7,300)
    exp_1 = (1/mu_1) ** t_range
    if k_2.get() > k_1.get():
        exp_2 = (-1/mu_2) ** t_range
        exp_2 = exp_2 * np.cos(math.pi*t_range)
    else:
        exp_2 = 1/mu_2 ** t_range

    y_1 = (exp_1 * eta_vec[0] * m_11) + (exp_2 * eta_vec[1] * m_21)
    y_2 = (exp_1 * eta_vec[0] * m_12) + (exp_2 * eta_vec[1] * m_22)
    axes.plot(t_range,y_1)
    axes.plot(t_range,y_2)
    canvas.draw()
    return y_1,y_2
    
def initialize_controls(ex=1,comp_one=1,comp_two=1,reinvest=1,y1=1,y2=1):
    control_frame = tk.Frame(master = root)
    control_frame.grid(column = 0, row = 0, padx=20)

    exploitation_label = tk.Label(control_frame,text='e')
    exploitation_entry = ttk.Entry(control_frame,textvariable=e_text)
    #exploitation_entry.insert(0,)
    exploitation_slider = tk.Scale(control_frame,from_=0,to=10,orient=tk.HORIZONTAL,
                                   resolution=0.01, command=update, variable=e)
    exploitation_slider.set(ex)
    exploitation_label.grid(row=0,column=0)
    exploitation_entry.grid(row=0,column=1)
    exploitation_slider.grid(row=1,column=1)

    comp_one_label = tk.Label(control_frame,text='k1')
    comp_one_entry = ttk.Entry(control_frame)
    #comp_one_entry.insert(0,comp_one)
    comp_one_scale = tk.Scale(control_frame,from_=0,to=10,orient=tk.HORIZONTAL,
                              resolution=0.01, command=update, variable=k_1) 
    comp_one_scale.set(comp_one)
    comp_one_label.grid(row=2,column=0)
    comp_one_entry.grid(row=2,column=1)
    comp_one_scale.grid(row=3,column=1)

    comp_two_label = tk.Label(control_frame,text='k2')
    comp_two_entry = ttk.Entry(control_frame)
    #comp_two_entry.insert(0,comp_two)
    comp_two_scale = tk.Scale(control_frame,from_=0,to=10,orient=tk.HORIZONTAL,
                              resolution=0.01, command=update, variable=k_2)
    comp_two_scale.set(comp_two)
    comp_two_label.grid(row=4,column=0)
    comp_two_entry.grid(row=4,column=1)
    comp_two_scale.grid(row=5,column=1)

    a_label = tk.Label(control_frame,text='a')
    a_entry = ttk.Entry(control_frame)
    #a_entry.insert(0,reinvest)
    a_slider = tk.Scale(control_frame,from_=0.0,to=1.0,orient=tk.HORIZONTAL,
                        resolution=0.01, command=update,variable=a)
    a_slider.set(reinvest)
    a_label.grid(row=6,column=0)
    a_entry.grid(row=6,column=1)
    a_slider.grid(row=7,column=1)

    y_1_label = tk.Label(control_frame,text='y1')
    y_1_entry = ttk.Entry(control_frame)
    #y_1_entry.insert(0,y1)
    y_1_slider = tk.Scale(control_frame,from_=0.0,to=1.0,orient=tk.HORIZONTAL,
                          resolution=0.01,command=update,variable=y_1i)
    y_1_slider.set(y1)
    y_1_label.grid(row=8,column=0)
    y_1_entry.grid(row=8,column=1)
    y_1_slider.grid(row=9,column=1)

    y_2_label = tk.Label(control_frame,text='y2')
    y_2_entry = ttk.Entry(control_frame)
    #y_2_entry.insert(0,y2)
    y_2_slider = tk.Scale(control_frame,from_=0.0,to=1.0,orient=tk.HORIZONTAL,
                          resolution=0.01, command=update,variable=y_2i)
    y_2_slider.set(y2)
    y_2_label.grid(row=10,column=0)
    y_2_entry.grid(row=10,column=1)
    y_2_slider.grid(row=11,column=1)

def initialize_display():
    display_frame = tk.Frame(master = root)
    display_frame.grid(column = 1, row = 0)
    fig,axes = plt.subplots(layout='constrained')
    canvas = FigureCanvasTkAgg(fig, master=display_frame)
    canvas.get_tk_widget().pack()
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, display_frame, pack_toolbar=False)
    toolbar.update()
    toolbar.pack()
    return canvas,axes

root = tk.Tk()
root.title("Marx Visualizer")

# User manipulated variables 
e = tk.DoubleVar()
e_text = tk.StringVar()
e.set(2.65)
#e_text.set(str(e.get()))
# ??? nothing online makes any sense wrt this
#e_text.trace_add('write',callback(e_text))
k_1 = tk.DoubleVar()
k_1.set(1.5)
k_2 = tk.DoubleVar()
k_2.set(3.6)
y_1i = tk.DoubleVar()
y_1i.set(1)
y_2i = tk.DoubleVar()
y_2i.set(0.67)
a = tk.DoubleVar()
a.set(0.5)

# Dependent Variables
DepVars = {}
initialize_controls(e.get(),k_1.get(),k_2.get(),a.get(),y_1i.get(),y_2i.get())
display_frame = tk.Frame(master = root)
display_frame.grid(column = 1, row = 0)
fig,axes = plt.subplots(layout='constrained')
canvas = FigureCanvasTkAgg(fig, master=display_frame)
canvas.get_tk_widget().pack()
toolbar = NavigationToolbar2Tk(canvas, display_frame, pack_toolbar=False)
toolbar.update()
toolbar.pack()

axes.set_ylim(-4,4)
axes.set_xlim(-1,7)
y_1,y_2 = update()
print(DepVars)

root.mainloop()


