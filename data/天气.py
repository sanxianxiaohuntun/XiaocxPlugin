import httpx
import sys
import asyncio

async def get_weather(city: str):
    api_url = "https://v3.alapi.cn/api/tianqi"
    params = {
        "city": city,
        "token": "YOUR_TOKEN"  # 请将这里的'YOUR_TOKEN'替换为你实际获取的token
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data.get('code') == 200:
                day_data = data['data']
                aqi_data = day_data.get('aqi', {})
                
                # 解析小时数据获取首个白天和夜晚数据
                day_info = next((h for h in day_data['hour'] if int(h['time'][11:13]) in range(6, 19)), {})
                night_info = next((h for h in day_data['hour'] if int(h['time'][11:13]) not in range(6, 19)), {})

                weather_info = (
                    f"省份：{day_data.get('province', 'N/A')}\n"
                    f"城市：{day_data.get('city', 'N/A')}\n"
                    f"日期：{day_data.get('date', 'N/A')}\n"
                    f"白天天气：{day_data.get('weather', 'N/A')}\n"
                    f"白天温度：{day_data.get('temp', 'N/A')}\n"
                    f"白天风向：{day_data.get('wind', 'N/A')}\n"
                    f"白天风力等级：{day_data.get('wind_power', 'N/A')}\n"
                    f"夜晚天气：{night_info.get('wea', 'N/A')}\n"
                    f"夜晚温度：{night_info.get('temp', 'N/A')}\n"
                    f"夜晚风向：{night_info.get('wind', 'N/A')}\n"
                    f"夜晚风力等级：{night_info.get('wind_level', 'N/A')}\n"
                    f"空气质量指数：{aqi_data.get('air', 'N/A')}\n"
                    f"空气质量级别：{aqi_data.get('air_level', 'N/A')}\n"
                    f"降水量：{day_data.get('rain', 'N/A')}mm\n"
                    f"日出时间：{day_data.get('sunrise', 'N/A')}\n"
                    f"日落时间：{day_data.get('sunset', 'N/A')}"
                )
                return weather_info
            else:
                return f"请求失败：{data.get('msg', '未知错误')}"
                
        except Exception as e:
            return f"发生异常：{str(e)}"

async def main():
    city = sys.argv[1] if len(sys.argv) > 1 else "北京"
    weather_info = await get_weather(city)
    print(weather_info)

if __name__ == "__main__":
    asyncio.run(main())
