from tkinter import *
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
root = Tk()
ap=ctrl.Antecedent(np.arange(0,11,1),'ap')
an=ctrl.Antecedent(np.arange(0,11,1),'an')
da=ctrl.Antecedent(np.arange(0,11,1),'da')
vom=ctrl.Antecedent(np.arange(0,11,1),'vom')
wl=ctrl.Antecedent(np.arange(0,11,1),'wl')
bmi = ctrl.Antecedent(np.arange(0, 41, 1), 'bmi')
cd = ctrl.Consequent(np.arange(0, 101, 1), 'cd')
ap['Mild']=fuzz.trimf(ap.universe,[0,0,4])
ap['Mod']=fuzz.trimf(ap.universe,[1,5,9])
ap['Sev']=fuzz.trimf(ap.universe,[6,10,10])
an['Mild']=fuzz.trimf(an.universe,[0,0,4])
an['Mod']=fuzz.trimf(an.universe,[1,5,9])
an['Sev']=fuzz.trimf(an.universe,[6,10,10])
da['Mild']=fuzz.trimf(da.universe,[0,0,4])
da['Mod']=fuzz.trimf(da.universe,[1,5,9])
da['Sev']=fuzz.trimf(da.universe,[6,10,10])
vom['OnceWeek']=fuzz.trimf(vom.universe,[0,0,4])
vom['ThriceWeek']=fuzz.trimf(vom.universe,[1,5,9])
vom['Daily']=fuzz.trimf(vom.universe,[6,10,10])
wl['US']=fuzz.trimf(wl.universe,[0,0,4])
wl['UL']=fuzz.trimf(wl.universe,[2,10,10])
bmi['UW'] = fuzz.trimf(bmi.universe, [0,0,22])
bmi['Normal'] = fuzz.trimf(bmi.universe, [15,22,29])
bmi['OW'] = fuzz.trimf(bmi.universe, [22,40,40])
cd['NCD'] = fuzz.trimf(cd.universe, [0, 0, 1])
cd['EL'] = fuzz.trimf(cd.universe, [0, 10, 20])
cd['VVL'] = fuzz.trimf(cd.universe, [10,20,30])
cd['VL'] = fuzz.trimf(cd.universe, [20,30,40])
cd['L'] = fuzz.trimf(cd.universe, [30,40,50])
cd['ML'] = fuzz.trimf(cd.universe, [40,50,60])
cd['M'] = fuzz.trimf(cd.universe, [50,60,70])
cd['MH'] = fuzz.trimf(cd.universe, [60,70,80])
cd['H'] = fuzz.trimf(cd.universe, [70,80,90])
cd['VH'] = fuzz.trimf(cd.universe, [80,90,100])
cd['VVH'] = fuzz.trimf(cd.universe, [90,100,100])
def Check():
    flag_chk = 0
    
    return flag_chk

def Result(result):
    result_root = Tk()
    Celiac_Disease_Probability_label = Label(result_root, text='Celiac Disease Probability is : ', font=("Helvetica", 15)).grid(
        rowspan=1, row=1, columnspan=2, column=0)
    Celiac_Disease_Probability_label = Label(result_root, text=str(result), font=("Helvetica", 15), width=18).grid(
        rowspan=1, row=1, column=3, columnspan=2)
    Celiac_Disease_Probability_val = float(result)
   
    
   


   
def Calculate():
    Check_Flag = Check()
    if Check_Flag == 0:
        global BMI_var, BMI_Scale, Weight_Loss_var, Weight_Loss_Scale, Vomiting_var, Vomiting_Scale, Diarrhea_var, Diarrhea_Scale, Anemia_var, Anemia_Scale, Abdominal_Pain_var, Abdominal_Pain_Scale
        BMI_value = str(BMI_var.get())
        BMI_value = BMI_value.strip()
        BMI_value = BMI_value.replace(" ", "")
        BMI_value = float(BMI_value)
        BMI_Scale.set(BMI_value)
        Weight_Loss_value = str(Weight_Loss_var.get())
        Weight_Loss_value = Weight_Loss_value.strip()
        Weight_Loss_value = Weight_Loss_value.replace(" ", "")
        Weight_Loss_value = float(Weight_Loss_value)
        Weight_Loss_Scale.set(Weight_Loss_value)
        Vomiting_value = str(Vomiting_var.get())
        Vomiting_value = Vomiting_value.strip()
        Vomiting_value = Vomiting_value.replace(" ", "")
        Vomiting_value = float(Vomiting_value)
        Vomiting_Scale.set(Vomiting_value)
        Diarrhea_value = str(Diarrhea_var.get())
        Diarrhea_value = Diarrhea_value.strip()
        Diarrhea_value = Diarrhea_value.replace(" ", "")
        Diarrhea_value = float(Diarrhea_value)
        Diarrhea_Scale.set(Diarrhea_value)
        Anemia_value = str(Anemia_var.get())
        Anemia_value = Anemia_value.strip()
        Anemia_value = Anemia_value.replace(" ", "")
        Anemia_value = float(Anemia_value)
        Anemia_Scale.set(Anemia_value)
        Abdominal_Pain_value = str(Abdominal_Pain_var.get())
        Abdominal_Pain_value = Abdominal_Pain_value.strip()
        Abdominal_Pain_value = Abdominal_Pain_value.replace(" ", "")
        Abdominal_Pain_value = float(Abdominal_Pain_value)
        Abdominal_Pain_Scale.set(Abdominal_Pain_value)
        rule1 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['UW'], cd['NCD'])
        rule2 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['Normal'], cd['NCD'])
        rule3 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['US'] & bmi['OW'], cd['NCD'])
        rule4 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['UW'], cd['NCD'])
        rule5 = ctrl.Rule(ap['Mild'] & an['Mild'] & da['Mild'] & vom['OnceWeek'] & wl['UL'] & bmi['Normal'], cd['NCD'])
        
        rule = []
        for i in range(1, 5):
            rule.append(eval("rule" + str(i)))
        cdlevel = ctrl.ControlSystemSimulation(fuzz.control.ControlSystem(rule))
        cdlevel.input['ap'] = Abdominal_Pain_value=1
        cdlevel.input['an'] = Anemia_value=1
        cdlevel.input['da'] = Diarrhea_value=1
        cdlevel.input['vom'] = Vomiting_value=1
        cdlevel.input['wl'] = Weight_Loss_value=1
        cdlevel.input['bmi'] = BMI_value=1
        x=cdlevel.compute()
       
        Result(cdlevel.output['cd'])                        
def get_BMI_value(val):
    global BMI_value, BMI_entry
    BMI_entry.delete( 0, END)
    BMI_entry.insert(END, val)
    y = StringVar()
    BMI_text = '                                                           '
    y.set(BMI_text)
    BMI_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=13, column=3)
def get_Weight_Loss_value(val):
    global Weight_Loss_value, Weight_Loss_entry
    Weight_Loss_entry.delete(0, END)
    Weight_Loss_entry.insert(END, val)
    y = StringVar()
    Weight_Loss_text = '                                                          '
    y.set(Weight_Loss_text)
    Weight_Loss_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=11, column=3)
def get_Vomiting_value(val):
    global Vomiting_value, Vomiting_entry
    Vomiting_entry.delete(0, END)
    Vomiting_entry.insert(END, val)
    y = StringVar()
    Vomiting_text = '                                                          '
    y.set(Vomiting_text)
    Vomiting_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=9, column=3)
def get_Diarrhea_value(val):
    global Diarrhea_value, Diarrhea_entry
    Diarrhea_entry.delete(0, END)
    Diarrhea_entry.insert(END, val)
    y = StringVar()
    Diarrhea_text = '                                                          '
    y.set(Diarrhea_text)
    Diarrhea_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=7, column=3)
def get_Anemia_value(val):
    global Anemia_value, Anemia_entry
    Anemia_entry.delete(0, END)
    Anemia_entry.insert(END, val)
    y = StringVar()
    Anemia_text = '                                                          '
    y.set(Anemia_text)
    Anemia_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=5, column=3)
def get_Abdominal_Pain_value(val):
    global Abdominal_Pain_value, Abdominal_Pain_entry
    Abdominal_Pain_entry.delete(0, END)
    Abdominal_Pain_entry.insert(END, val)
    y = StringVar()
    Abdominal_Pain_text = '                                                          '
    y.set(Abdominal_Pain_text)
    Abdominal_Pain_error_label = Label(root, textvariable=str(y), font=("Helvetica", 10), width=30).grid(rowspan=1, row=3, column=3)


def Create_GUI():
    global Abdominal_Pain_Scale, Abdominal_Pain_var, Abdominal_Pain_entry, Anemia_Scale, Anemia_var, Anemia_entry, Diarrhea_var, Diarrhea_entry, Diarrhea_Scale,Weight_Loss_Scale, Vomiting_Scale, Vomiting_var, Vomiting_entry, Weight_Loss_var, Weight_Loss_entry,BMI_var, BMI_entry, BMI_Scale
    Abdominal_Pain_var, Anemia_var, Diarrhea_var, Vomiting_var, Weight_Loss_var, BMI_var = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()










   
    # enter_details_label = Label(root, padx=70, pady=10, text='Enter Details -->', font=("Helvetica", 14)).grid(row=1)
    Abdominal_Pain_label_button = Button(root, pady=10, text='Abdominal Pain', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: Abdominal_Pain_label_func()).grid(rowspan=1, row=2,columnspan=2)

    Abdominal_Pain_Scale = Scale(root, label = '', from_=0, to=10, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=5, command = get_Abdominal_Pain_value)
    Abdominal_Pain_Scale.grid(rowspan=1, row=2, column=2, columnspan=2)

    Abdominal_Pain_entry = Entry(root, textvariable=Abdominal_Pain_var, width=10)
    Abdominal_Pain_entry.grid(rowspan=1, row=2, column=4)
    
    Anemia_label_button = Button(root, pady=10, text='Anemia', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: Anemia_label_func()).grid(rowspan=1, row=4, columnspan=2)
    Anemia_Scale = Scale(root, label='', from_=0, to=10, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=5, command=get_Anemia_value)
    Anemia_Scale.grid(rowspan=1, row=4, column=2,  columnspan=2)
    Anemia_entry = Entry(root, textvariable=Anemia_var, width=10)
    Anemia_entry.grid(rowspan=1, row=4, column=4)
  
    Diarrhea_label_button = Button(root, pady=10, text='Diarrhea', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: Diarrhea_label_func()).grid(rowspan=1, row=6, columnspan=2)
    Diarrhea_Scale = Scale(root, label='', from_=0, to=10, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=5, command=get_Diarrhea_value)
    Diarrhea_Scale.grid(rowspan=1, row=6, column=2,  columnspan=2)
    Diarrhea_entry = Entry(root, textvariable=Diarrhea_var, width=10)
    Diarrhea_entry.grid(rowspan=1, row=6, column=4)
  
    Vomiting_label_button = Button(root, pady=10, text='Vomiting', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: Vomiting_label_func()).grid(rowspan=1, row=8, columnspan=2)
    Vomiting_Scale = Scale(root, label='', from_=0, to=10, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=5, command=get_Vomiting_value)
    Vomiting_Scale.grid(rowspan=1, row=8, column=2, columnspan=2)
    Vomiting_entry = Entry(root, textvariable=Vomiting_var, width=10)
    Vomiting_entry.grid(rowspan=1, row=8, column=4)
    
    Weight_Loss_label_button = Button(root, pady=10, text='Weight Loss', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: Weight_Loss_label_func()).grid(rowspan=1, row=10, columnspan=2)
    Weight_Loss_Scale = Scale(root, label='', from_=0, to=10, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=5, command=get_Weight_Loss_value)
    Weight_Loss_Scale.grid(rowspan=1, row=10, column=2, columnspan=2)
    Weight_Loss_entry = Entry(root, textvariable=Weight_Loss_var, width=10)
    Weight_Loss_entry.grid(rowspan=1, row=10, column=4)
   
    space_label = Label(root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=11, column=1)
    BMI_label_button = Button(root, text='              BMI', font=("Helvetica", 12), fg='black', borderwidth=0, command=lambda: BMI_label_func()).grid(rowspan=1, row=12, column=0)
    Calculate_BMI_button = Button(root, padx= 20, pady=10, text='CALCULATE BMI', fg='black', command=lambda: Calculate_BMI_func()).grid(rowspan=1, row=12,column=1)
    BMI_Scale = Scale(root, label='', from_=0, to=40, resolution=0.001, orient=HORIZONTAL, sliderlength=10, length=250, tickinterval=10, command=get_BMI_value)
    BMI_Scale.grid(rowspan=1, row=12, column=2, columnspan=2)
    BMI_entry = Entry(root, textvariable=BMI_var, width=10)
    BMI_entry.grid(rowspan=1, row=12, column=4)
   
    Calculate_button = Button(root, padx=30, pady=10, text='CALCULATE', fg='black', command=lambda: Calculate()).grid(rowspan=1, row=14, column=3)
    space_label = Label(root, text='', font=("Helvetica", 10), width=30).grid(rowspan=1, row=15, column=1)
Create_GUI()
root.mainloop()