from datetime import date, timedelta
import os

todayS = date.today()
magasins = ["bc", "back-to-bc", "calvinandhobbes", "garfield",  "heathcliff",  "nancy", "nancy-classics", "peanuts", "peanuts-begins", "wizardofid", "wizard-of-id-classics"]

for magasin in magasins:
    file_name = f"{magasin}.rss"
    file_path = f"outputs/{file_name}"  # outputs klasörüne kaydedeceğiz
    dateF = date.today() - timedelta(days=91)

    with open(file_path, 'w') as file:
        file.write(f"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
        file.write(f"<rss version=\"2.0\">\n")
        file.write(f"<channel>\n")
        file.write(f"<title>{magasin}</title>\n")
        file.write(f"<link>http://www.gocomics.com/{magasin}</link>\n")
        file.write(f"<description>Gocomics {magasin}</description>\n")
        while dateF <= todayS:
            file.write(f"<item>\n")
            file.write(f"<title>{magasin} {dateF.strftime("%-d %B %Y")}</title>\n")
            file.write(f"<link>http://www.gocomics.com/{magasin}/{dateF.strftime("%Y/%m/%d")}</link>\n")
            file.write(f"<guid>http://www.gocomics.com/{magasin}/{dateF.strftime("%Y/%m/%d")}</guid>\n")
            file.write(f"<pubDate>{dateF.strftime("%a, %-d %b %Y")} 13:00:00 GMT</pubDate>\n")
            file.write(f"<description>{magasin} {dateF.strftime("%-d %B %Y")}</description>\n")
            file.write(f"</item>\n")
            dateF += timedelta(days=1)
        file.write(f"</channel>\n")
        file.write(f"</rss>")
        file.close()
