import tkinter as tk

def calc_bmi():#BMI計算
    h = float(textHeight.get()) / 100
    w = float(textWeight.get())
    bmi = w / h ** 2
    rw = h ** 2 * 22
    per = int(w / rw * 100) - 100
    s = "肥満 {0}% (bmi={1})".format(per, bmi)
    labelResult['text'] = s

win = tk.Tk()#win=ウインドウ
win.title("肥満判定")
win.geometry("500x250")

labelHeight = tk.Label(win, text=u'身長(cm):')
labelHeight.pack()

textHeight = tk.Entry(win)
textHeight.insert(tk.END, '身長を入力してください')
textHeight.pack()

labelWeight = tk.Label(win, text='体重(kg):')
labelWeight.pack()

textWeight = tk.Entry(win)
textWeight.insert(tk.END, '体重を入力してください')
textWeight.pack()


labelResult = tk.Label(win, text=u'---')
labelResult.pack()

calcButton = tk.Button(win, text=u'計算')
calcButton["command"] = calc_bmi
calcButton.pack()

win.mainloop()