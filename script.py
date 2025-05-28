from datetime import date, timedelta
import os

todayS = date.today()
magasins = ["bc", "back-to-bc", "calvinandhobbes", "garfield",  "heathcliff",  "nancy", "nancy-classics", "peanuts", "peanuts-begins", "wizardofid", "wizard-of-id-classics"]

for magasin in magasins:
    file_name = f"{magasin}.rss"
    file_path = f"outputs/{file_name}"  # outputs klasörüne kaydedeceğiz
    dateF = date.today() - timedelta(days=91)

    with open(file_path, 'w') as file:
        file.write(f"<?xml version="1.0" encoding="utf-8"?>")
        file.write(f"<rss version="2.0">")
        file.write(f"<channel>")
        file.write(f"<title>{magasin}</title>")
        file.write(f"<link>http://www.gocomics.com/{magasin}</link>")
        file.write(f"<description>Gocomics {magasin}</description>")
        while dateF <= todayS:
            file.write(f"<item>")
            file.write(f"<title>{magasin} {dateF.strftime("%-d %B %Y")}</title>")
            file.write(f"<link>http://www.gocomics.com/{magasin}/{dateF.strftime("%Y/%m/%d")}</link>")
            file.write(f"<guid>http://www.gocomics.com/{magasin}/{dateF.strftime("%Y/%m/%d")}</guid>")
            file.write(f"<pubDate>{dateF.strftime("%a, %-d %b %Y")} 13:00:00 GMT</pubDate>")
            file.write(f"<description>{magasin} {dateF.strftime("%-d %B %Y")}</description>")
            file.write(f"</item>")
            dateF += timedelta(days=1)
        file.write(f"</channel>")
        file.write(f"</rss>")
        file.close()
