import random
from fastmcp import FastMCP

mcp = FastMCP(name="Simple Calculator MCP")

@mcp.tool()
def roll_dice(n_dice: int = 1) -> list[int]:
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b


# def main():
#     print("Hello from expense-tracker-mcp-server!")
#     mcp.run()  # <-- actually starts the MCP server

if __name__ == "__main__":
    # main()
    mcp.run(transport="http", host="0.0.0.0", port=8000)