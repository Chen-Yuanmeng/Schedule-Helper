import pickle


def restore_excel():
    with open('./ui/template.dat', 'rb') as w:
        [a, b] = pickle.load(w)

    with open('./设置课程.xlsx', 'wb') as f:
        f.write(a)

    with open('./设置课节.xlsx', 'wb') as g:
        g.write(b)
