from rich.console import Console

_console = Console()

def get_logger():
    class L:
        def info(self, msg): _console.log(f"[blue]INFO[/]: {msg}")
        def warn(self, msg): _console.log(f"[yellow]WARN[/]: {msg}")
        def error(self, msg): _console.log(f"[red]ERROR[/]: {msg}")
    return L()
