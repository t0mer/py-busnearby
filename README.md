# py-busnearby
A Python library to get bus times from the Bus Nearby API https://www.busnearby.co.il/


## Installation

You can install the library from PyPI:

```bash
pip install busnearby
```

Alternatively, you can install it directly from the source:

```bash
git clone https://github.com/t0mer/py-busnearby.git
cd bus_times
pip install .
```

## Usage
Here are some examples of how to use the library:


## Get Bus Times
To get bus times for a specific station and bus lines, you can use the get_bus_times function.

```python
from busnearby import BusNearBy
import asyncio

bus = BusNearBy()

async def main():
    station = "34501"
    bus_lines = "609,636,10,15"
    try:
        result = await bus.get_bus_times(station, bus_lines)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")

asyncio.run(main())
```

## Example Output

```json
{
    "stationName": "שדרות וייצמן/עקיבא",
    "time": "2024-07-22 13:10:43.974935",
    "buses": [
        {
            "lineNumber": "10",
            "arrivalSeconds": 644
        },
        {
            "lineNumber": "15",
            "arrivalSeconds": 1501
        },
        {
            "lineNumber": "609",
            "arrivalSeconds": 2210
        },
        {
            "lineNumber": "636",
            "arrivalSeconds": 3532
        },
        {
            "lineNumber": "636",
            "arrivalSeconds": 6728
        }
    ]
}
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.
