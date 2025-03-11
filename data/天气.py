import httpx
import sys
import asyncio
import json

async def get_weather(city: str, raw_data: bool = False):
    api_url = "https://v3.alapi.cn/api/tianqi"
    params = {
        "city": city,
        "token": "YOUR TOKEN"  # 请替换为有效的token
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data.get('code') == 200:
                if raw_data:
                    # 返回原始API数据，格式化为可读的JSON
                    return json.dumps(data['data'], indent=4, ensure_ascii=False)
                else:
                    # 提取并格式化天气信息
                    day_data = data['data']
                    aqi_data = day_data.get('aqi', {})  # 空气质量数据
                    index_data = day_data.get('index', [])  # 生活指数数据
                    alarm_data = day_data.get('alarm', [])  # 气象预警数据
                    
                    # 解析小时数据，获取白天和夜晚信息
                    day_info = next((h for h in day_data['hour'] if int(h['time'][11:13]) in range(6, 19)), {})
                    night_info = next((h for h in day_data['hour'] if int(h['time'][11:13]) not in range(6, 19)), {})

                    # 格式化输出天气信息
                    weather_info = (
                        f"省份：{day_data.get('province', 'N/A')}\n"
                        f"城市：{day_data.get('city', 'N/A')}\n"
                        f"日期：{day_data.get('date', 'N/A')}\n"
                        f"白天天气：{day_data.get('weather', 'N/A')}\n"
                        f"白天温度：{day_data.get('temp', 'N/A')}℃\n"
                        f"最低温度：{day_data.get('min_temp', 'N/A')}℃\n"
                        f"最高温度：{day_data.get('max_temp', 'N/A')}℃\n"
                        f"白天风向：{day_data.get('wind', 'N/A')}\n"
                        f"白天风力等级：{day_data.get('wind_power', 'N/A')}\n"
                        f"夜晚天气：{night_info.get('wea', 'N/A')}\n"
                        f"夜晚温度：{night_info.get('temp', 'N/A')}℃\n"
                        f"夜晚风向：{night_info.get('wind', 'N/A')}\n"
                        f"夜晚风力等级：{night_info.get('wind_level', 'N/A')}\n"
                        f"湿度：{day_data.get('humidity', 'N/A')}\n"
                        f"能见度：{day_data.get('visibility', 'N/A')}\n"
                        f"气压：{day_data.get('pressure', 'N/A')}hPa\n"
                        f"空气质量指数：{aqi_data.get('air', 'N/A')}\n"
                        f"空气质量级别：{aqi_data.get('air_level', 'N/A')}\n"
                        f"PM2.5：{aqi_data.get('pm25', 'N/A')}\n"
                        f"PM10：{aqi_data.get('pm10', 'N/A')}\n"
                        f"降水量：{day_data.get('rain', 'N/A')}mm\n"
                        f"日出时间：{day_data.get('sunrise', 'N/A')}\n"
                        f"日落时间：{day_data.get('sunset', 'N/A')}\n"
                    )

                    # 添加生活指数
                    if index_data:
                        weather_info += "生活指数：\n"
                        for idx in index_data:
                            weather_info += f"  {idx.get('name', 'N/A')} ({idx.get('level', 'N/A')})：{idx.get('content', 'N/A')}\n"

                    # 添加气象预警
                    if alarm_data:
                        weather_info += "气象预警：\n"
                        for alarm in alarm_data:
                            weather_info += f"  {alarm.get('title', 'N/A')} ({alarm.get('level', 'N/A')})：{alarm.get('content', 'N/A')}\n"

                    return weather_info
            else:
                return f"请求失败：{data.get('msg', '未知错误')}"
                
        except Exception as e:
            return f"发生异常：{str(e)}"

async def main():
    # 解析命令行参数
    if len(sys.argv) > 1:
        city = sys.argv[1]
        # 检查是否提供了“原始数据”作为第二个参数
        raw_data = len(sys.argv) > 2 and sys.argv[2] == "原始数据"
    else:
        # 默认查询北京的格式化天气信息
        city = "北京"
        raw_data = False
    
    # 调用天气查询函数
    weather_info = await get_weather(city, raw_data=raw_data)
    print(weather_info)

if __name__ == "__main__":
    asyncio.run(main())