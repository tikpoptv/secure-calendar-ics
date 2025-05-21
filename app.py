from flask import Flask, Response, request, abort
from datetime import datetime
import os
import json
import psycopg2
from psycopg2.extras import RealDictCursor
from config import Config, DataSource

app = Flask(__name__)

def get_db_connection():
    """Create a database connection"""
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.route("/")
def index():
    return (
        "<h2>The system is currently active and ready.</h2>"
        "<p>This page is not intended for direct access.</p>"
    )

def load_json_events():
    """Load events from JSON file"""
    try:
        with open(Config.JSON_FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)['events']
    except FileNotFoundError:
        return []

def load_db_events():
    """Load events from database"""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Query events
        cur.execute("""
            SELECT 
                uid,
                summary,
                start_time as start,
                end_time as end,
                description,
                location
            FROM events
            ORDER BY start_time
        """)
        
        events = cur.fetchall()
        cur.close()
        conn.close()
        
        # Convert datetime objects to ISO format strings
        for event in events:
            event['start'] = event['start'].isoformat()
            event['end'] = event['end'].isoformat()
        
        return events
    except Exception as e:
        app.logger.error(f"Database error: {str(e)}")
        return []

def generate_ics_content(events):
    now = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    
    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//SmartHome//Secure Calendar//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
"""
    
    for event in events:
        start_dt = datetime.fromisoformat(event['start'])
        end_dt = datetime.fromisoformat(event['end'])
        
        ics_content += f"""
BEGIN:VEVENT
UID:{event['uid']}
SUMMARY:{event['summary']}
DTSTART;TZID=Asia/Bangkok:{start_dt.strftime('%Y%m%dT%H%M%S')}
DTEND;TZID=Asia/Bangkok:{end_dt.strftime('%Y%m%dT%H%M%S')}
DTSTAMP:{now}
DESCRIPTION:{event['description']}
LOCATION:{event['location']}
END:VEVENT
"""
    
    ics_content += "\nEND:VCALENDAR"
    return ics_content

@app.route("/calendar.ics")
def calendar():
    token = request.args.get("token")
    if token not in Config.ALLOWED_TOKENS:
        abort(403)

    if Config.DATA_SOURCE == DataSource.JSON:
        events = load_json_events()
    else:
        events = load_db_events()
    
    ics_content = generate_ics_content(events)
    return Response(ics_content, mimetype='text/calendar')

if __name__ == "__main__":
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
