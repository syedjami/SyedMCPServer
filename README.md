This MCP Server gets the weather from openweathermap.org. You would need to register at the site and get an API key to be able to get the weather info.
You can use any client, but we tested it with Claude Desktop
You will need to update the Claue Desktop config file which is avaiable in the source as well
When you pull the source code, you would need to create an environment using UV, so UV is a prereq for it
Run the commands as follows form you IDE Terminal or root directory
  -> uv run weather
  -> uv pip install -e . --force-reinstall
  -> uv run weather # again to ensure weather is running
Once service is running, kill the weather service and Claude Desktop from Task Manager
Restart Claude Desktop and try asking it "Houston, TX Weather"
