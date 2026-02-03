This MCP Server gets the stock info using yfinance library.
yfinance is a free to use library so no api or registration needed.
You can use any client, but we tested it with Claude Desktop
You will need to update the Claude Desktop config file which is avaiable in the source as well
Run the commands as follows form you IDE Terminal (we used VS Code) or root directory
  -> uv run mcp_stock_server from your stock folder
  -> uv pip install -e . --force-reinstall from your stock folder
  -> uv run mcp_stock_server from your stock folder # again to ensure weather is running, you can check from Task Manager to see weather.exe is running
Once mcp service is running, kill the mcp_stock_service and Claude Desktop from Task Manager
Restart Claude Desktop and try asking Apple stock in new chat. This should use the local mcp stock server to get the answer for you.
