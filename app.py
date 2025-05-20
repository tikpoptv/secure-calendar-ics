from flask import Flask, Response, request, abort
from datetime import datetime
from dotenv import load_dotenv
import os

# โหลด environment variables จาก .env
load_dotenv()

app = Flask(__name__)

# ดึง token ที่อนุญาตจาก ENV แล้วแปลงเป็น set
ALLOWED_TOKENS = set(os.getenv("ALLOWED_TOKENS", "").split(","))

@app.route("/calendar.ics")
def calendar():
    token = request.args.get("token")
    if token not in ALLOWED_TOKENS:
        abort(403)

    now = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Your Company//Secure Calendar//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH

BEGIN:VEVENT
UID:event-19may2025@example.com
SUMMARY:กิจกรรมอุ่นเครื่องก่อนเริ่มงาน
DTSTART;TZID=Asia/Bangkok:20250519T090000
DTEND;TZID=Asia/Bangkok:20250519T100000
DTSTAMP:{now}
DESCRIPTION:กิจกรรมเตรียมความพร้อมประจำปี
LOCATION:ลานกิจกรรมหน้าอาคาร
END:VEVENT

... (กิจกรรมอื่นๆ เช่น 23, 26, 27, 28, 30) ...

END:VCALENDAR
"""
    return Response(ics_content, mimetype='text/calendar')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
