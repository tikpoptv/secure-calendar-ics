from flask import Flask, Response

app = Flask(__name__)

@app.route("/calendar.ics")
def calendar():
    ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Your Company//My Calendar//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
UID:event-21may2025@example.com
SUMMARY:กิจกรรมสำคัญ
DTSTART;TZID=Asia/Bangkok:20250521T100000
DTEND;TZID=Asia/Bangkok:20250521T110000
DESCRIPTION:นัดหมายทดสอบระบบ webcal
LOCATION:สำนักงานกลาง
END:VEVENT
END:VCALENDAR
"""
    return Response(ics_content, mimetype='text/calendar')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)
