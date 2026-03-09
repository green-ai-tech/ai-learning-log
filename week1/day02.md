## Day 02: 导入 GitHub 项目 - rich

- 项目地址：https://github.com/Textualize/rich
- 目的：学习现代终端美化、Rich 库用法、阅读优秀 Python 源码

### 导入步骤
~~~
1.  mkdir imported-projects 
    cd imported-projects
2.  git clone https://github.com/Textualize/rich.git
3.  cd rich
4. python -m venv .venv && source .venv/bin/activate
5. pip install -e .
~~~

### 测试成功命令
- python -m rich          → 看到彩色 demo 就成功！

### 今天学到/计划看的文件
- examples/ 目录下的所有 .py 文件（超级多小 demo）
- rich/console.py         → 核心 Console 类
- rich/table.py           → 表格实现
- rich/progress.py        → 进度条原理
### 测试
![rich demo 截图](/images/rich-demo-01.png)  
![rich demo 截图2](/images/rich-demo-02.png)