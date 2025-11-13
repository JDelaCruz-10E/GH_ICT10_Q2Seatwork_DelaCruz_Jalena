from pyscript import display, document

def average(e):
    document.getElementById('output').innerHTML = " "
    sub1 = document.getElementById('sci').value
    sub2 = document.getElementById('eng').value
    sub3 = document.getElementById('math').value
    sub4 = document.getElementById('filo').value
    sub5 = document.getElementById('ict').value
    sub6 = document.getElementById('pe').value
    first = document.getElementById('first').value
    last = document.getElementById('last').value

    average = (float(sub1.value) * sub1.check <=
             float(sub2.value) * sub2.check <= 
             float(sub3.value) * sub3.check <=
             float(sub4.value) * sub4.check <=
             float(sub5.value) * sub5.check <=
             float(sub6.value) * sub6.check)

    display(f'Name: {first} {last}', target='output')
    display(f'Science: {sub1}', target='output')
    display(f'English: {sub2}', target='output')
    display(f'Math: {sub3}', target='output')
    display(f'Filipino: {sub4}', target='output')
    display(f'ICT: {sub5}', target='output')
    display(f'PE: {sub6}', target='output')
    display(f'Your general weighted average is {average}', target='output') 