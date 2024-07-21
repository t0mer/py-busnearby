import json
from datetime import datetime
import asyncio
import aiohttp
from typing import List, Dict



class BusNearBy(object):
    def __init__(self):
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://app.busnearby.co.il/",
    }
        self.base_url = "https://app.busnearby.co.il"

    async def get_station_data(self,session: aiohttp.ClientSession, station: str) -> Dict:
        url = f"{self.base_url}/stopSearch?query={station}&locale=he"
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()

    async def get_bus_times_data(self, session: aiohttp.ClientSession, stop_id: str, current_time: int) -> List[Dict]:
        url = f"{self.base_url}/directions/index/stops/1:{stop_id}/stoptimes?numberOfDepartures=1&timeRange=86400&startTime={current_time}&locale=he"
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()

    async def get_bus_times(self, station: str, bus_lines: str) -> Dict:
        bus_lines = set(bus_lines.split(','))
        current_time = int(datetime.now().timestamp())
        async with aiohttp.ClientSession(headers=self.headers) as session:
            try:
                station_data = await self.get_station_data(session, station)
                if not station_data:
                    raise ValueError("Station not found")

                stop_id = station_data[0]['stop_id']
                times_data = await self.get_bus_times_data(session, stop_id, current_time)

                all_buses = [
                    {
                        "lineNumber": bus['times'][0]['routeShortName'],
                        "arrivalSeconds": (bus['times'][0]['serviceDay'] + bus['times'][0]['realtimeArrival']) - current_time
                    }
                    for bus in times_data
                    if (bus['times'][0]['serviceDay'] + bus['times'][0]['realtimeArrival']) - current_time >= 0
                ]

                filtered_buses = [bus for bus in all_buses if bus['lineNumber'] in bus_lines]

                # If any specified bus line is not found, return all buses
                if len(filtered_buses) < len(bus_lines):
                    result = all_buses
                else:
                    result = filtered_buses

                result.sort(key=lambda x: x['arrivalSeconds'])

                final_result = {
                    "stationName": station_data[0]['stop_name'],
                    "time": f"{datetime.now()}",
                    "buses": result
                }

                return final_result
            except (aiohttp.ClientError, json.JSONDecodeError) as e:
                raise RuntimeError(f"Error fetching or decoding data: {e}")
