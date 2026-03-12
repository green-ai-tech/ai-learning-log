import tkinter as tk
from tkinter import messagebox
import random


class ExponentGame:
    def __init__(self, root):
        # 初始化主窗口
        self.root = root
        self.root.title("指数判断小游戏")
        self.root.geometry("400x300")  # 设置窗口大小
        self.root.resizable(False, False)  # 禁止调整窗口大小

        # 游戏变量
        self.base = 0  # 底数
        self.exponent = 0  # 指数
        self.correct_answer = 0  # 正确答案
        self.score = 0  # 得分

        # 创建界面元素
        self.create_widgets()
        # 生成第一题
        self.generate_question()

    def create_widgets(self):
        # 标题标签
        self.title_label = tk.Label(
            self.root,
            text="指数判断小游戏",
            font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=10)

        # 题目显示标签
        self.question_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14)
        )
        self.question_label.pack(pady=10)

        # 输入框
        self.answer_entry = tk.Entry(
            self.root,
            font=("Arial", 14),
            width=15
        )
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind("<Return>", self.check_answer)  # 按回车提交

        # 提交按钮
        self.submit_btn = tk.Button(
            self.root,
            text="提交答案",
            font=("Arial", 12),
            command=self.check_answer
        )
        self.submit_btn.pack(pady=5)

        # 得分显示
        self.score_label = tk.Label(
            self.root,
            text=f"当前得分: {self.score}",
            font=("Arial", 12)
        )
        self.score_label.pack(pady=10)

        # 下一题按钮
        self.next_btn = tk.Button(
            self.root,
            text="下一题",
            font=("Arial", 12),
            command=self.generate_question,
            state=tk.DISABLED  # 初始禁用
        )
        self.next_btn.pack(pady=5)

    def generate_question(self):
        """生成随机的指数题目"""
        # 生成1-10之间的随机底数，1-3之间的随机指数（难度适中）
        self.base = random.randint(1, 10)
        self.exponent = random.randint(1, 3)
        self.correct_answer = self.base ** self.exponent

        # 更新题目显示
        self.question_label.config(text=f"{self.base} 的 {self.exponent} 次方等于多少？")

        # 清空输入框并聚焦
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()

        # 重置按钮状态
        self.submit_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.DISABLED)

    def check_answer(self, event=None):
        """检查用户输入的答案"""
        try:
            # 获取用户输入并转换为整数
            user_answer = int(self.answer_entry.get())

            # 判断答案是否正确
            if user_answer == self.correct_answer:
                messagebox.showinfo("正确！", "恭喜你，回答正确！🎉")
                self.score += 1  # 得分+1
            else:
                messagebox.showerror("错误！", f"答错了😞，正确答案是：{self.correct_answer}")

            # 更新得分显示
            self.score_label.config(text=f"当前得分: {self.score}")

            # 禁用提交按钮，启用下一题按钮
            self.submit_btn.config(state=tk.DISABLED)
            self.next_btn.config(state=tk.NORMAL)

        except ValueError:
            # 处理非数字输入
            messagebox.warning("输入错误", "请输入有效的数字！")
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.focus()


if __name__ == "__main__":
    # 创建主窗口并启动游戏
    root = tk.Tk()
    game = ExponentGame(root)
    root.mainloop()