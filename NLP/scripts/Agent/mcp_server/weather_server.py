from fastmcp import FastMCP

mcp = FastMCP("weather-server")

@mcp.tool()
def get_weather(city: str) -> dict:
    """Get the current weather for a given city. Returns temperature in Celsius and a short weather condition."""

    weather_data = {
        "Mumbai": {"temperature": 31, "condition": "Clear"},
        "Delhi":  {"temperature": 33, "condition": "Sunny"},
        "London": {"temperature": 18, "condition": "Cloudy"},
    }

    return weather_data.get(city, {
        "temperature": "unknown",
        "condition": "unknown"
    })

if __name__ == "__main__":
    print("🌤️  Weather MCP Server starting at http://127.0.0.1:8000")
    print("    SSE endpoint : http://127.0.0.1:8000/sse")
    print("    Press Ctrl+C to stop.\n")
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
