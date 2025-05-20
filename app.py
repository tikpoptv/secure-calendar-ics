from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)

@app.route("/calendar.ics")
def calendar():
    now = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Your Company//My Calendar//EN
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

BEGIN:VEVENT
UID:event-23may2025@example.com
SUMMARY:กิจกรรมเริ่มต้นเดือน
DTSTART;TZID=Asia/Bangkok:20250523T150000
DTEND;TZID=Asia/Bangkok:20250523T160000
DTSTAMP:{now}
DESCRIPTION:กิจกรรมเปิดต้นเดือนพฤษภาคม
LOCATION:ห้อง Creative ชั้น 6
END:VEVENT

BEGIN:VEVENT
UID:event-26may2025-v8@example.com
SUMMARY:กิจกรรมเวอร์ชันล่าสุด
DTSTART;TZID=Asia/Bangkok:20250526T100000
DTEND;TZID=Asia/Bangkok:20250526T113000
DTSTAMP:{now}
DESCRIPTION:กิจกรรมวันที่ 26 พ.ค. (อัปเดตเมื่อ {now})
LOCATION:ชั้น 5 อาคารฝึกอบรม
END:VEVENT

BEGIN:VEVENT
UID:event-27may2025@example.com
SUMMARY:กิจกรรมเพิ่มเติมวันที่ 27
DTSTART;TZID=Asia/Bangkok:20250527T140000
DTEND;TZID=Asia/Bangkok:20250527T150000
DTSTAMP:{now}
DESCRIPTION:กิจกรรมวันที่ 27 พ.ค.
LOCATION:ห้องสัมมนาเล็ก ชั้น 2
END:VEVENT

BEGIN:VEVENT
UID:event-28may2025@example.com
SUMMARY:กิจกรรมเสริมวันที่ 28
DTSTART;TZID=Asia/Bangkok:20250528T090000
DTEND;TZID=Asia/Bangkok:20250528T100000
DTSTAMP:{now}
DESCRIPTION:กิจกรรมวันที่ 28 พ.ค.
LOCATION:ห้องประชุมใหญ่ ชั้น 1
END:VEVENT

BEGIN:VEVENT
UID:event-30may2025@example.com
SUMMARY:กิจกรรมปิดท้ายเดือนพฤษภาคม
DTSTART;TZID=Asia/Bangkok:20250530T130000
DTEND;TZID=Asia/Bangkok:20250530T140000
DTSTAMP:{now}
DESCRIPTION:กิจกรรมวันที่ 30 พ.ค.
LOCATION:ห้องจัดเลี้ยง ชั้น 3
END:VEVENT

END:VCALENDAR
"""
    return Response(ics_content, mimetype='text/calendar')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
