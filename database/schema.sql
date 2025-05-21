-- Create events table
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    uid VARCHAR(255) NOT NULL UNIQUE,
    summary VARCHAR(255) NOT NULL,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    description TEXT,
    location VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create index for faster queries
CREATE INDEX idx_events_start_time ON events(start_time);
CREATE INDEX idx_events_end_time ON events(end_time);

-- Example data
INSERT INTO events (uid, summary, start_time, end_time, description, location) VALUES
    ('event-19may2025@example.com', 'กิจกรรมอุ่นเครื่องก่อนเริ่มงาน', 
     '2025-05-19 09:00:00+07', '2025-05-19 10:00:00+07',
     'กิจกรรมเตรียมความพร้อมประจำปี', 'ลานกิจกรรมหน้าอาคาร'),
    
    ('event-23may2025@example.com', 'กิจกรรมเริ่มต้นเดือน',
     '2025-05-23 15:00:00+07', '2025-05-23 16:00:00+07',
     'กิจกรรมเปิดต้นเดือนพฤษภาคม', 'ห้อง Creative ชั้น 6');

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Trigger to automatically update updated_at
CREATE TRIGGER update_events_updated_at
    BEFORE UPDATE ON events
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column(); 