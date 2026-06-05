

```markdown
# Django Web Crawler

A simple web crawler built with Django that extracts links and content from web pages and saves them to a database.

## Features
- Automatically fetch page content using `requests`
- Extract text and links using `BeautifulSoup`
- Save results to database (SQLite or PostgreSQL)
- Handle errors and timeouts during requests

## Quick Installation

```bash
# 1. Clone the project
git clone https://github.com/jamall-mahmoudi-dev/Django_Web_Crawler.git
cd Django_Web_Crawler

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Set up the database (run migrations)
python manage.py migrate

# 5. Create an admin user (optional)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```

## How to Use

### Method 1: Command Line
```bash
python manage.py crawl https://example.com
```

### Method 2: Admin Panel
1. Go to `/admin` in your browser
2. Add a new **URL** to crawl
3. Click **Start Crawl**

## Output

After crawling, the following information is saved to the database:
- Page URL
- Page title
- Main text content (without HTML tags)
- List of internal and external links
- Crawl date and time

## Project Structure
```
Django_Web_Crawler/
├── manage.py
├── requirements.txt
├── crawler/              ← Main crawler app
│   ├── models.py         ← Database models
│   ├── crawler.py        ← Crawling logic
│   └── management/       ← Command line commands
└── config/               ← Django settings
```

## Environment Variables (Optional)

Create a `.env` file:
```ini
SECRET_KEY=your-secret-key-here
DEBUG=True
# If using PostgreSQL:
DATABASE_URL=postgres://user:pass@localhost/dbname
```

## Important Notes
- Only **public and static** pages are crawled (JavaScript execution is NOT supported)
- For crawling large websites, always add `time.sleep()` between requests
- Respect the target website's `robots.txt` file

## Common Issues

| Problem | Solution |
|---------|----------|
| SSL Error | `pip install certifi` (already in requirements) |
| Brotli Error | `pip install brotli` (already in requirements) |
| PostgreSQL connection | Make sure `psycopg2` is installed and database is running |

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Commit your changes
4. Submit a pull request

## License
[Add your license name here, e.g., MIT]
```