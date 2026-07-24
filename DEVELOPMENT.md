# Shree Avadhut Traders - GST App Development Guide

## Getting Started

### Quick Start
```bash
# Clone and setup
git clone https://github.com/pranaykamdi691-dotcom/Shree-avadhut-traders.git
cd Shree-avadhut-traders
chmod +x setup.sh
./setup.sh

# Run app
python run.py
```

### Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
# FLASK_ENV=development
# SECRET_KEY=your-secret-key
# DATABASE_URL=sqlite:///gst_app.db
```

## Development Workflow

### Using Make Commands
```bash
make help          # Show all commands
make install       # Install dependencies
make run           # Run development server
make test          # Run test suite
make clean         # Clean cache files
make migrate       # Run migrations
make shell         # Open Flask shell
```

### Running Tests
```bash
# All tests
pytest

# Specific test file
pytest tests/test_auth.py -v

# With coverage
pytest --cov=app tests/
```

## Database Migrations

```bash
# Create a new migration
flask db migrate -m "Description of changes"

# Apply migrations
flask db upgrade

# Downgrade to previous version
flask db downgrade
```

## Code Structure

### Models (app/models/)
- Define database schema
- Add relationships between models
- Implement model methods

### Routes (app/routes/)
- Handle HTTP requests
- Process user input
- Return responses
- Authentication checks

### Templates (app/templates/)
- HTML forms and pages
- JavaScript for interactivity
- Bootstrap for styling
- Flash messages for feedback

### Static (app/static/)
- CSS stylesheets
- Client-side JavaScript
- Images and assets

## Adding New Features

### Adding a New Route

1. Create route file in `app/routes/`
```python
from flask import Blueprint
from flask_login import login_required

feature_bp = Blueprint('feature', __name__, url_prefix='/features')

@feature_bp.route('/')
@login_required
def list_features():
    return render_template('feature/list.html')
```

2. Register in `app/routes/__init__.py`
```python
from .feature import feature_bp
```

3. Register in `app/__init__.py`
```python
app.register_blueprint(feature_bp)
```

## Troubleshooting

### Port 5000 already in use
```bash
python run.py --port 5001
```

### Database errors
```bash
rm gst_app.db
python run.py
```

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Pytest](https://docs.pytest.org/)
