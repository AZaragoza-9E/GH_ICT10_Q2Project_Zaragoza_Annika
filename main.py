# SGC (Student Grade Calculator) i asked help from sofia :p so this is a code she gave me for my sw
from pyscript import document, display


firstn = str(document.getElementById('firstone').value)
lastn = str(document.getElementById('lasttime').value)

    
eng = float(document.getElementById('eng').value)
fil = float(document.getElementById('fil').value)
math = float(document.getElementById('math').value)
sci = float(document.getElementById('sci').value)
ss = float(document.getElementById('ss').value)
ve = float(document.getElementById('ve').value)

   
subjects = [eng, fil, math, sci, ss, ve]
units = (5, 3, 5, 5, 3, 2)

   
grade = ((subjects[0] * units[0])+(subjects [1]* units[1])+(subjects[2]*units[2])+(subjects[3]*units[3])+(subjects[4]*units[4])+(subjects[5]*units[5]))/23

    
display(f'Name: {firstn} {lastn}', target='nameofthesubject')

display(f"""English: Tongues of the Forgotten = {eng}
Filipino: Wikang Naluma sa Dilim or A language aged in darkness = {fil}
Math: Numerical Patterns of the Void = {math}
"""
, target='gradesset1')
display(f"""Science: Anatomy of the Unseen = {sci}
SS :Histories That Never Happened = {ss}
VE: Lessons of Obedient Silence= {ve}
"""
, target='gradesset2')
display(f'Your General Weighted Average is {round(grade, 2)}.', target='grade')