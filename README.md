# Calendar ICS Generator

A secure Flask-based web service that generates iCalendar (.ics) files for event scheduling. This service provides a protected endpoint that requires authentication via tokens to access calendar data.

## Features

- Secure calendar endpoint with token-based authentication
- Generates iCalendar (.ics) files compatible with most calendar applications
- Supports multiple events with detailed information
- Timezone-aware events (Asia/Bangkok)
- Flexible data source options (JSON or PostgreSQL Database)
- Docker support for easy deployment

## Prerequisites

- Python 3.x
- Docker (optional, for containerized deployment)
- PostgreSQL (if using database as data source)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tikpoptv/secure-calendar-ics
cd calendar
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `example.env` to `.env`
   - Configure your data source and settings in `.env`

## Configuration

### Data Source Selection

The service supports two data sources:

1. JSON File (Default):
```
DATA_SOURCE=json
```
Events are stored in `data/events.json` with the following structure:
```json
{
    "events": [
        {
            "uid": "event-1@example.com",
            "summary": "Event Title",
            "start": "2025-05-19T09:00:00",
            "end": "2025-05-19T10:00:00",
            "description": "Event Description",
            "location": "Event Location"
        }
    ]
}
```

2. PostgreSQL Database:
```
DATA_SOURCE=database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=calendar_db
DB_USER=postgres
DB_PASSWORD=your_password
```

Database Schema:
```sql
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
```

To set up the database:
1. Create a PostgreSQL database
2. Run the schema file:
```bash
psql -U postgres -d calendar_db -f database/schema.sql
```

### Security Settings

Configure access tokens in `.env`:
```
ALLOWED_TOKENS=your_token1,your_token2
```

## Usage

1. Start the server:
```bash
python app.py
```

2. Access the calendar:
   - Visit `http://localhost:5555/calendar.ics?token=YOUR_TOKEN`
   - The calendar will be available in iCalendar format

## Docker Deployment

Build and run using Docker:

```bash
docker build -t calendar-service .
```

For JSON data source:
```bash
docker run -p 5555:5555 \
  -e DATA_SOURCE=json \
  -e ALLOWED_TOKENS=your_token \
  calendar-service
```

For database configuration:
```bash
docker run -p 5555:5555 \
  -e DATA_SOURCE=database \
  -e DB_HOST=your_db_host \
  -e DB_PORT=5432 \
  -e DB_NAME=calendar_db \
  -e DB_USER=postgres \
  -e DB_PASSWORD=your_password \
  -e ALLOWED_TOKENS=your_token \
  calendar-service
```

## API Endpoints

- `GET /`: Health check endpoint
- `GET /calendar.ics`: Main calendar endpoint (requires token)

## Security

- Token-based authentication required for calendar access
- Tokens are configured via environment variables
- Unauthorized access attempts are rejected with 403 status

## Environment Variables

- `DATA_SOURCE`: Choose data source (`json` or `database`)
- `ALLOWED_TOKENS`: Comma-separated list of valid access tokens
- Database configuration (if using database):
  - `DB_HOST`: Database host
  - `DB_PORT`: Database port
  - `DB_NAME`: Database name
  - `DB_USER`: Database user
  - `DB_PASSWORD`: Database password
