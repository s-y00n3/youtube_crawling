import csv
import re
import json

import requests


            
video_id = "6OugH2W1cG8"
url = f"https://www.youtube.com/watch?v={video_id}"
response = requests.get(url)
html_content = response.text
with open(f"{video_id}.html", "w", encoding='utf-8') as f:
    f.write(response.text)


match = re.search(r'var ytInitialData = ({.*?});</script>', html_content, re.DOTALL)

if match:
    json_str = match.group(1)
    try:
        data = json.loads(json_str)
        
        results = data['contents']['twoColumnWatchNextResults']['secondaryResults']['secondaryResults']['results']
        
        json_file =f"관련동영상/{video_id}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
            
        filename = f"관련동영상/{video_id}.csv"
        with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            
            writer.writerow(['비디오ID', '썸네일URL', '제목', '채널명'])
            
            
            for item in results:
                if 'compactVideoRenderer' in item:
                
                    renderer = item['compactVideoRenderer']
                    video_id = renderer.get('videoId', 'N/A')
                    
                    thumbnail_image = renderer.get('thumbnail', {}).get('thumbnails', [{}])[0].get('url', 'N/A')
                    title = renderer.get('title', {}).get('simpleText', 'N/A')
                    channel_name = renderer.get('longBylineText', {}).get('runs', [{}])[0].get('text', 'N/A')

                    writer.writerow([video_id, thumbnail_image, title, channel_name])

        print("Data extraction and CSV writing complete!")

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    except KeyError as e:
        print("Key error:", e)
        print("Make sure the JSON structure has not changed and your keys are correct.")
else:
    print("Could not find ytInitialData in the HTML content.")