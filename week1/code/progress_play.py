from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# 1. 彩色 + 样式文字
rprint("[bold red]警告！[/bold red] 这是一个 [italic yellow]重要[/italic yellow] 消息")

# 2. 带面板的突出显示
console.print(Panel(
    "[bold magenta]钗的学习日志 Day 02[/bold magenta]\n已导入 rich 并成功运行",
    title="成就解锁",
    border_style="green",
    expand=False
))

# 3. 自定义 Text 对象（更灵活）
text = Text("学习进度：", style="cyan")
text.append(" 70%", style="bold green")
text.append(" → 继续加油！", style="blue underline")
console.print(text)