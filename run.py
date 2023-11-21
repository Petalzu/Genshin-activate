import ctypes
import tkinter as tk
import random
import time
import statistics
import os
import base64

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
#img = "AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAACUWAAAlFgAAAAAAAAAAAABUUFv/VFFa/zgzQv8jHTL/PDdF/1ZUX/9bXGb/WVpl/1ZWYv9GRlP/dXaA/5OUmv+TlZv/rq+1/4eIkv+Eho//gYON/5qbof91c3z/fHyD/5aVnf9eXWf/My4//ykjNf8lHUf/KCBa/yghWv8oIVr/KCFa/yghWv8oIVr/KCFa/1NPWv9TUFn/S0hP/0hFTf9fXGP/X15n/1tdZv9bWmX/Wlpl/1ZXY/+OkJf/vb/C/7y+wP+rrLH/r7C2/72+w/+io6f/jZCT/5qbn/+trLD/paaq/5KTmP9aWGL/VVJb/zk1Sv8qIFP/KCFP/ycgU/8nIVr/KCFa/yghWv8oIVr/UEtW/1NQWP9WVFr/YV5j/2FgY/9fXWP/W1tk/1xbZf9YWWL/SElU/1xcaf98fof/dHV+/3d4gP+PkZj/l5ed/3Fyev92d4L/lZac/5mYnv9+fYX/bW52/1xbZP9gXmP/XFpg/zo0UP8xKkf/KCFF/ykgWP8oIVn/JyFa/yghWf+EiJr/m6Gp/6yyuP+ssbn/qrG5/6ewuP+lrrj/oam1/3mDmf9bZYH/Ym2J/3uKpv94iab/hZay/4eVrv9seI7/eYmj/3mKpv+Pn7j/j52z/4yXqP+gqrf/pKy4/6evt/+rs7n/l5+p/2pvhf9QUnL/MCqD/zUxpv80Mab/NDGl/6650v/X5O3/7vv//+v5///q+P//5/b//+b1//+jsMf/cH2n/36Ruv9zha//lqzV/6fB5/+buN7/k6nJ/4idvv+cuuD/ocDp/6zL8P+72fv/rcbi/9Xl9v/j8v//5fX//+n3///o9f3/ucba/46Ytv8yMoH/PTzR/z9A5v8/P+X/mqO0/9Ph6v/s+v//6vf//+r3///p9///1+Xw/2dwkP80Omr/XGmV/2+Aq/+HmsX/fI65/3+Ttv+YqMb/nq/O/4igxf+Gn8r/k63U/4Wex/93jLH/qLjM/+X0/v/m9P7/6fb+/+v5///V4/D/tcPU/z5CcP8uLYL/OzjE/z493/+5tKX/0+Dm/+z6///r+P//6vf//+r4//+7yNf/q7bP/4aRrv9ia43/X22L/3aJsv9zhK7/g5O1/6m31f+mttb/jJ/C/3KEq/9qfqX/dIaw/25/qv98ja3/0+Tt/+r3///q9///6/n//+Px+f/V4uz/XGKH/yMkXv8pKGz/LC2H/+DTsv/Y4eP/7Pr//+v5///r+f//4fH4/6u4yv++y+L/t8Tc/7S/1P+yrKL/lZWb/2Ftkf+SoMT/oa3Q/5+tz/+XqMz/hJW5/3aHrP92iLD/c4Sv/219p/+ercP/6/n//+v4///r+f//6/j+/+v5/v+Tm7D/TlN4/01Rdf9dYoL/69q2/9zh3v/r+f//6/n//+z6///S4Ov/rLfN/8TQ5/+7x+D/mqTA/3t2if9oYnz/bG+U/6mxzf+7wdj/wsrc/7vE2f+jrcf/hJKz/26Bpv9peKD/XmSA/3Z7lP/e7fT/6/r//+v5///r+f//7Pr//8bT3/+tudD/rrnQ/7W/1//z37j/393T/+r4///r+f//6/n//8LP3f+qs8j/qrPN/2xymP9XWYT/i46u/8bL3f/n7ff/8Pf+//P6///z+v//8/r//+70+//S2uj/lqO8/0NJdP9bVmz/kY+P/8bV3//s+///6/n//+v5///s+///zdvk/6Svxf+8yN//tMDY//jluf/j3Mf/5vT6/+v5///n9vz/u8TT/4uGj/9EQ2v/dXiZ/9Tb6f/y+f//9Pr///L4///x+P//8vj///L4///x+P//8vj///T6///n7/f/jJCu/y4tZv8+QW//q7jK/+n4/v/r+f//6/n//+z7///Q3+f/rLjO/8PP5v/Czuf/2c2s/9rQtP/e6ev/6vj//9jo8/+fqcH/Pj5p/4SIqP/k7fX/8fr///D4///y+P//8vj///H3/v/s9P3/7PX+/+/4///x+P//8fj///L5///r8/v/io6v/zg5bf+Xorz/4O32/+z6///r+f//7Pr//9bl7f+4w9z/ws/n/7XA0//I0dv/wcjN/8vZ4P/W5PL/vMnf/5ikvv9teJn/qbrW/7nG3P/V3un/7/f9//L4///v9f3/5Oj0/+bs+P/g5vf/1971/+vz/f/w+P//8vj//+30+//b5PD/c3me/4eRrv/N2uj/6/n//+v5///s+v//1uXu/7K80v+wtL3/xbyq/8PR5f+/zeL/t8bY/7vJ3P/H1OP/0N7v/8rc9f+0yef/uMrh/9jj8P/u9v7/8vj///H3/v/w9v3/8fj//+rx+/+3uev/xMjs/+/3/v/y+P//3+bu/8HL2v+isMr/kZ65/7bE2f/b6PX/6vj+/+z6///U4ub/wb2u/+rYtf/+6sD/ydbg/7PB1v++zd7/3uz0/+r4///g7vv/uszj/7XK5P/K3/f/yd70/+Xw+v/w+P//8fj///D4/v/x+P//8/n//+jv+v/h6Pj/8Pj+//L4///t9fz/2uPu/7nI3P+su9H/qbfL/8XQ5//Y5fH/2eby/9La2f/z4bv//+zB///qwP+1wMv/ucbV/+b2+//s+v//6vj+/9Xj7v/Bz9//zNrt/3qS0P98teT/sNjw/+31/f/v9///5e76/+72/f/y+P//8vn///L5///x+P//8Pj//+rz+//P2+r/uMfe/8XU5//K1+X/tcHT/77M3/+8yd//qqy2/+/btv//7cL//+zB/6ezvf/g7vX/7Pr//+v5///q+f7/wtPk/6+yyP+dmb7/LD+y/5O/7f+IruD/4On1//H5///j6vf/7vX9//L5///y+f//8vn///D4///n8/7/3ez9/9Xm+v/H2ez/x9Xl/+Pw+v+4wtL/k522/5KduP9jZoX/ppyR/8y/pv+7r5n/vcvS/+v6///r+f//6/r//+Lx9v+Qn8H/aWON/4WSr/8xRq7/jZLQ/19kuP/i6PT/8vn///H5///u9vz/4+z1/+Lr9P/h6PP/5Oz4/+Ty///O5///yuX//8TZ7v/d6/b/t8HQ/3eAm/9tdpT/a3WT/1xkhP9mbYr/bneR/2pzjv/d6vD/7Pr//+v5///s+///z97o/3KAp/83Nlv/XFpx/xUaev8UEZb/amq3/+Hp8f/Z4uv/2OPu/8jX5/+/0er/vM3k/8vU5f+Qlb3/lJu0/6Kvw/+OnbT/mai7/93q8//U4er/maS4/4OOp/96haH/Zm6M/11mhP9kboz/WGJ+/+by9//w+/7/8Pr9/+/6/f/G0+H/kKLB/15meP8/PEb/FRU1/yMkYv+AhKb/vcnY/7/L3P/P3u//1uj7/9Xo/P/A0OT/zdnr/8DI3v96fo//WFpo/2BheP9/gpr/2eXt/+78///p+Pz/1uPv/7TA2f9nb4z/Q0tp/0RMav88QmD/5PL3/+z5///y+/7/8fj6/87b5v+putb/zNns/8TJz/+Ok5z/q7TC/8nV3//S3+r/3u33/+f0///l8///4O/6/8rX5P/g6/b/5u78/+bu9f/i6e//6vH5/8nR3v/Y5e3/7Pv//+Hw+P+3w9j/bneV/0hQbf9OVXP/T1d1/15mhP/k8vf/6/n//+36/v/q9Pj/1uTs/7fJ4P/J2vD/5/H5/9zl8P/U3+v/6Pb8/+j1/P/r+f//6vj//+r3///q9/7/4u71/+71/P/y+P//8fn+//H5///x+f//1eDt/87d6P/f7Pf/prDG/19ohP9GTmz/VV99/2Nsiv9dZoT/anWT/+Tx9//r+f//6/n//+Ty+P/Z5u3/vs/g/73P6P/h7fr/y9bi/+n1+v/t+v//6/n//+v5///r+f//6/n//+n4/v/d6e//8Pb9//L4///y+P//8vn//+bu9f/Czd7/ws7g/5uluv9YYHz/TFRy/1lhf/9oc5H/YmyK/1xlg/9sd5X/4+/1/+v5///r+f//5fP5/9nn7v/S4u3/p7nU/7TF3v/M2OT/9Pn6//P7/v/y+/7/7vr9/+36/f/r+v//5fP5/9nk7P/v9v7/7/f///H4///n7/b/1eHo/8nT4/+BiaL/VV16/1hhf/9pcpD/a3WS/2Fohf9pcpD/YWyJ/215lv+3wMf/7Pr//+v5///o9fz/0d3n/+Hw+P+qvNr/obXS/83a4//l8fT/8Pz+//T8/v/y+/3/+v7+//f9/v/e6fH/2OXx/+z1///t9v//5e73/9Pf5v/n9Pr/qrTE/1Rbd/9kbov/eIKc/5Sesv+xvcr/tsDM/1JZev9TWob/VVt7/1lhbP/d6/H/6/r+/+r4/v/I1eH/2+nz/62+1/+svdj/4/D5/+Xz+//o9fz/6/n9//H7/v/9/v//+v39/8HM2//BzuL/1+Tz/9nk8f/N2eP/5O/z/+v2+/+Gj6H/ZGqH/4mTqP/M2eL/6ff9/+/9///S3uP/Njlr/ystgv8tMVX/gImb/73J1f/l9Pz/0+Hu/7C7zv+yvtL/n6zD/5qpwf/Dz+b/x9Pq/83Z7v/S3/H/2uf0/+fx+f/q9Pr/sMPb/7PI4/+uwNX/vcvW/+Lr7//3+vr/7vX3/5afrf+orrv/5O3y/+37///r+f//7vz//7C6wf8qLVr/QU6E/y05Uf+9x9z/gIe2/2Nrfv9QVWP/VFhm/2lrev9tbn3/ZGh3/2Nmd/9lbHz/fISX/5ukuf+1wdj/xtPq/77M4v+etdr/rsTl/8TW5f/n9fr/7/v///H7///h7PH/2ebs/+/6/f/u+v//6/n//+v5///t+///eYCO/y80df9HVYH/MjlN/1xgw/88PM7/ICJ0/xcYK/8gISv/R0dV/2Bgb/8vLzv/IB8r/xwcKP8dHir/Jicz/z9CUP9rc4T/gY2o/4+hxP+xwtv/2uj0/+r4/v/r+v//6fj+/9Xj6v/n9fv/6/n//+v5///r+f//7Pr//9jk6v8+QVr/Jih1/yw8Wv9JT1b/PTza/z4/5f89Pdv/LSuR/x0cPv8tLj3/UFFf/yEhLf8fHyv/HiAr/x8fK/8fHir/HR0o/xwdKP8kJjL/TVFh/5CZrf+8yN7/1OLx/+Xz/P/W5O//1eLr/+v5///r+f//6/n//+v5///u/P//k52l/xkdOP86T27/QmBz/2pscP89Ptz/Pj/j/z4/5P8+P+L/MzO0/ycnaf8yMlD/ISMx/x4eKv8eHyv/Hx8r/x8fK/8fHyv/Hx8r/x8fKv8dHSj/JCUx/0tQXv+Llaf/vsre/8bT4//k8fn/6/n//+v5///r+f//7fv//83Z3/84Pkv/KjhP/0xtgf81TV//bG9r/0A93P8+P+P/Pj/j/z4/4/8+P+X/OzvU/y4tm/8gIVn/HBw2/xscLf8dHSv/Hx8s/x8fK/8fHyv/Hx8r/x8fK/8fHir/HBwo/yQlMf9QVWX/oKu6/+Lv+P/r+f//6/n//+z6///Z5ur/XGJq/yEsOv9igpf/V3iO/y49Vf9JWGn/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
#with open("1.ico", "wb") as f:
#            f.write(base64.b64decode(img))

class CustomDialog:
    def __init__(self, title, message):
        self.root = tk.Tk()
        self.root.title(title)
        label = tk.Label(self.root, text=message)
        label.pack(padx=20, pady=20)
        self.root.iconbitmap("1.ico")

    def show(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = random.randint(0, screen_width - 200)
        y = random.randint(0, screen_height - 100)
        self.root.geometry("+%d+%d" % (x, y))
        start_time = time.time()
        self.root.mainloop()
        end_time = time.time()
        return end_time - start_time


i = -1
duration = 0
times = [0]
while True:
    i = i + 1
    dialog = CustomDialog(
        "Genshin",
        "The {}th cue box \n This time took time {} and the average time {}".format(i + 1, round(duration, 2), round(statistics.mean(times),2)),
    )
    duration = dialog.show()
    times.append(duration)
    if 0 in times:
        times.remove(0)
    #os.remove("1.ico")


#pyinstaller -i 1.ico -F run.py --noconsole