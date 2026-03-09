# test_rich.py
from rich import print as rprint   # 推荐用这个，别覆盖内置 print
from rich.console import Console

console = Console()

rprint("[bold green]恭喜！[/bold green] rich 项目导入成功～ Day XX 达成！")

console.rule("学习进度", style="cyan")  # 加一条分隔线

data = {"name": "钗", "location": "Tokyo", "learning": ["Python", "rich", "AI"]}
rprint(data)  # 会自动漂亮打印字典/列表等