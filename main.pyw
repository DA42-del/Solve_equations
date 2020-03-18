"""
原方程：x^4 - 15 = 0
求解方程的其中一个近似解，已知该解的范围(self.range_middle, self.range_large)
求解精度为0.01（指方程左右两边）
要求最后输出结果保留五位小数
"""

import tkinter as tk
import pickle

class solver:

    def __init__(self,
        equation_str,
        range_small = 0,
        range_large = 2,
        result_range = 0.001):
        """初始化"""

        self.equation_str = equation_str
        self.range_small = range_small
        self.range_large = range_large
        self.result_range = result_range
        self.process = ""

    def equation(self, x):
        """将方程转换成函数，并返回y值"""
         
        y = eval(self.equation_str[0:-4])
        return y

    def judge(self, range_small, range_large):
        """替换 x 的范围"""
        
        range_middle = (range_small + range_large) / 2
        D_value = abs(self.equation(range_middle))
        self.process += ("range_middle = {:>20}, \t\tD_value = {}\n"
                    .format(range_middle, D_value))
        
        if (self.equation(range_small)
            * self.equation(range_middle)) < 0:
            return range_small, range_middle, range_middle, D_value
        else:
            return range_middle, range_large, range_middle, D_value

    def solve(self):
        """解方程"""

        for i in range(20):
            """调用函数，循环更替 x 的范围"""

            (self.range_small,
            self.range_large, 
            self.range_middle, 
            self.D_value) = self.judge(self.range_small, self.range_large)
            
            if abs(self.D_value) <= self.result_range:
                # 方程两边误差小于规定的范围，退出循环
                
                self.result = self.range_middle
                break
        else:
            self.result = None

        # 返回计算结果
        return self.process, self.result

# test = solver("x ** 2 - 2 = 0", 0, 3)
# process, result = test.solve()
# print("process = {}result = {}".format(process, result))
def GUI():
    """创建GUI界面"""


    def Go():
        """开始"""
        
        e_str = e_e.get()
        s_str = int(e_s.get())
        m_str = int(e_m.get())
        
        if s_str == m_str:
            text.insert("insert", "Error:This is a wrong range")
            return
        
        if s_str > m_str:
            s_str, m_str = m_str, s_str
            e_s.delete('0', 'end')
            e_m.delete('0', 'end')
            e_s.insert("insert", s_str)
            e_m.insert("insert", m_str)

        equation = solver(e_str, s_str, m_str)
        process_str, result_str = equation.solve()
        
        if result_str == None:
            text.insert("insert",
                        "{}Error:Range too large\n"
                        .format(process_str) + \
                        "[> 0.001 × 2\u00b2\u00ba]\n" + \
                        " or 'x' is not in this range")
        else:
            text.insert("insert", "{}x ≈ {:.5f}\n"
                        .format(process_str, result_str))



    def Clear_Entry():
        """删除Entry框内容"""
        e_e.delete('0', 'end')
        e_s.delete('0', 'end')
        e_m.delete('0', 'end')

        
    def Clear_Text():
        """删除文本框内容"""

        text.delete('1.0', 'end')


    def Exit():
        """退出"""

        window.quit()
        
    window = tk.Tk() # 创建根窗口
    window.title('Welcome to our website')
    window.geometry('500x400')

    # 创建用于输入的标签和Entry控件，并摆放好位置
    tk.Label(window,
             text='Please enter the equation!',
             font=('Arial. 18')).pack()
    tk.Label(window,
             text='equation:',
             font=("Arial, 14")).place(x=50, y=100)
    tk.Label(window,
             text='< x <',
             font=('Arial, 14')).place(x=200, y=150)
    
    e_e = tk.Entry(window,
                   show=None,
                   highlightcolor = 'yellow',
                   highlightthickness = 1,
                   font=('Arial', 14)) # 输入方程的Entry控件
    e_e.place(x=200, y=105)
    e_s = tk.Entry(window,
                   show=None,
                   highlightcolor = 'red',
                   highlightthickness = 1,
                   font=('Arial', 9)) # 输入最小值的Entry控件
    e_s.place(x=50, y=150)
    e_m = tk.Entry(window,
                   show=None,
                   highlightcolor = 'black',
                   highlightthickness = 1,
                   font=('Arial', 9)) # 输入最大值的Entry控件
    e_m.place(x=260, y=150)

    window_menu = tk.Menu()
    window_menu.add_command(label = "Go", command = Go)
    window_menu.add_command(label = "Entry", command = Clear_Entry)
    window_menu.add_command(label = "Text", command = Clear_Text)
    window_menu.add_command(label = "Exit", command = Exit)
    
    
    # 显示菜单
    window.config(menu = window_menu)
    
    # 绑定快捷键
    window.bind_all("<Control-g>", lambda event: Go())
    window.bind_all("<Control-e>", lambda event: Clear_Entry())
    window.bind_all("<Control-t>", lambda event: Clear_Text())
    window.bind_all("<Control-q>", lambda event: Exit())
    
    # 创建文本框
    text = tk.Text(window,
                   width = 69,
                   height = 10,
                   highlightcolor = 'blue',
                   highlightthickness = 1)
    text.place(x=5, y=200)
    
    window.mainloop()

if __name__ == '__main__':
    # 测试
    GUI()
