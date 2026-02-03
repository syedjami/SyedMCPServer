This MCP Server gets the weather info from openweathermap.org.
You would need to register at the openweathermap.org and get WEATHER_API_KEY to be able to get the weather info from the website. 
You can use any client, but we tested it with Claude Desktop
You will need to update the Claude Desktop config file which is avaiable in the source as well
You would also need to update the WEATHER_API_KEY="PLACE YOUR API KEY" in the config file
When you pull the source code, you would need to create an environment using UV, so UV lib is a prereq for it
Run the commands as follows form you IDE Terminal (we used VS Code) or root directory
  -> uv pip install -e . --force-reinstall from your weather folder
  -> uv run mcp_weather_server from your weather folder # again to ensure weather is running, you can check from Task Manager to see weather.exe is running
Once mcp weather service is running, kill the weather service and Claude Desktop from Task Manager
Restart Claude Desktop and try asking it "Houston, TX Weather". This should use the locall mcp server to get the answer for you.
