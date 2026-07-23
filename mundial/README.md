# Panini Mundial 2026 ⚽🏆

A Django web application displaying FIFA World Cup 2026 teams and players in Panini sticker collection style with **file upload support** for images.

## Features

- 10 sample teams from FIFA World Cup 2026
- **Player management** with photo uploads
- **File upload system** for flags, badges, and player photos
- Organized by confederations and groups
- Responsive Panini-style design
- Admin interface for managing teams, countries, and players

## Quick Start

1. **Clone and install:**
   ```bash
   git clone <repository-url>
   cd mundial_2026
   pip install -r requirements.txt
   ```

2. **Setup database:**
   ```bash
   python manage.py migrate
   python manage.py load_world_cup_data
   ```

3. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

4. **Run server:**
   ```bash
   python manage.py runserver
   ```

5. **Visit:**
   - **Countries:** http://localhost:8000/
   - **Players:** http://localhost:8000/players/
   - **Admin:** http://localhost:8000/admin/

## File Upload Features

### Countries
- **Flag images:** Upload country flag files (`flags/` folder)
- Supports common image formats (PNG, JPG, etc.)

### Teams  
- **Badge images:** Upload team badge/logo files (`badges/` folder)

### Players
- **Player photos:** Upload player portrait files (`players/` folder)
- **Jersey numbers:** Unique per team
- **Positions:** GK, DEF, MID, FWD
- **Age tracking**

## Models

- **Country:** Name, 2-letter code, confederation, flag image (file)
- **Team:** Name, country, group, badge image (file), ranking
- **Player:** Name, team, position, jersey number, age, photo (file)

## API Endpoints

- `/api/teams-by-group/` - Teams by World Cup groups
- `/api/teams-by-confederation/` - Teams by confederation
- `/api/players-by-team/` - Players organized by team

## Admin Features

Upload and manage:
- Country flags through file upload
- Team badges through file upload  
- Player photos through file upload
- Full CRUD operations for all models

## Sample Data Included

**Countries & Teams (10):**
- Ecuador 🇪🇨 | Canada 🇨🇦 (Group A)
- Japan 🇯🇵 | South Korea 🇰🇷 (Group B)  
- Argentina 🇦🇷 | Brazil 🇧🇷 (Group C)
- Germany 🇩🇪 | France 🇫🇷 (Group D)
- United States 🇺🇸 | Mexico 🇲🇽 (Group E)

**Sample Players:**
- Enner Valencia (Ecuador #13)
- Lionel Messi (Argentina #10)
- Vinícius Jr. (Brazil #7)
- And more...

## Technologies

- Django 6.0.7
- Pillow (for image handling)
- SQLite database
- Responsive CSS Grid

## File Structure

```
media/
├── flags/      # Country flag images
├── badges/     # Team badge images  
└── players/    # Player photo images
```