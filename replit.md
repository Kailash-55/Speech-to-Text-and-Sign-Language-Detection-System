# Agentic - AI-Based Adaptive Learning Platform

## Overview
Agentic is an AI-based adaptive learning platform designed specifically for differently abled students, focusing on UG Computer Science education. The platform provides accessibility features, multimodal AI interaction, adaptive learning logic, and a clean dashboard UI.

## Project Goals
- Personalizes learning material based on each student's ability
- Supports voice, text, sign language detection, and visual interaction
- Adapts difficulty level using rule-based logic
- Tracks student behavior, progress, and performance
- Provides a simple, accessible web UI with ADHD-friendly design

## Tech Stack
- **Backend**: Python 3.11, Flask, Flask-SQLAlchemy, Flask-Login
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap 5, Feather Icons
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Speech Recognition**: SpeechRecognition library
- **Charts**: Matplotlib
- **Data Processing**: NumPy, Pandas

## Project Structure
```
/
├── main.py                 # Application entry point
├── app.py                  # Flask app configuration
├── routes.py               # All Flask routes
├── models.py               # Database models
├── seed_data.py            # Database seeding script
├── /modules/               # Core functionality modules
│   ├── tts_engine.py       # Text-to-Speech
│   ├── stt_engine.py       # Speech-to-Text
│   ├── sign_language_detector.py
│   ├── adaptive_engine.py  # Learning adaptation logic
│   ├── content_personalization.py
│   ├── emotion_detector.py
│   ├── progress_tracker.py
│   ├── adaptive_agent.py   # AI Adaptive Learning Agent
│   ├── accessibility_agent.py  # AI Accessibility Agent
│   └── assistant_agent.py  # Parent & Teacher AI Assistant
├── /utils/                 # Utility functions
│   ├── helpers.py          # General helpers
│   ├── plot_utils.py       # Chart generation
│   └── scheduler.py        # Automated weekly reports scheduler
├── /templates/             # HTML templates
│   ├── base.html           # Base layout with navigation
│   ├── index.html          # Login page
│   ├── register.html       # Registration
│   ├── dashboard.html      # Main dashboard with quick actions
│   ├── lesson.html         # Lesson viewer
│   ├── quiz.html           # Quiz interface
│   ├── quiz_result.html    # Results page
│   ├── games.html          # Games hub
│   ├── play_game.html      # Individual game player
│   ├── attendance.html     # Student attendance
│   ├── parent_login.html   # Parent portal login
│   ├── parent_dashboard.html # Parent progress view
│   ├── progress.html       # Analytics
│   ├── settings.html       # User settings
│   ├── help.html           # Help & accessibility
│   └── error.html          # Error pages
├── /static/
│   ├── /css/style.css      # Main stylesheet
│   ├── /audio/             # Generated TTS audio
│   └── /js/
│       ├── emotion_agent.js    # Browser-based emotion detection
│       └── accessibility.js    # Accessibility behavior tracking
└── design_guidelines.md    # UI/UX guidelines
```

## Key Features

### Accessibility Features
- **Text-to-Speech**: Audio playback for lesson content
- **High Contrast Mode**: For visually impaired users
- **Large Font Options**: Adjustable font sizes (14-24px)
- **Reduce Motion**: Disable animations
- **Keyboard Navigation**: Full keyboard support
- **Sign Language Mode**: Gesture-based navigation (placeholder)
- **Voice Commands**: Voice-based attendance marking

### Adaptive Learning
- Three difficulty levels: Easy, Medium, Advanced
- Automatic difficulty adjustment based on quiz performance
- Personalized content for each level
- Progress tracking and recommendations
- UG Computer Science curriculum including:
  - Core: Programming, Variables, Control Structures, Functions, Data Structures, Algorithms
  - Databases, Networking, Object-Oriented Programming
  - Advanced: Computer Architecture, Software Engineering, Compiler Design
  - Theory: Theory of Computation, Machine Learning

### Audio Explanations (NEW - Dec 2025)
- Every lesson has a "Listen" button to hear the lesson content
- On-demand text-to-speech generation using gTTS
- "Read Aloud" sidebar control for audio playback
- Pause/resume functionality
- Works for all lessons including new UG-level topics

### Educational Games (NEW)
- ADHD-friendly design: Big buttons, large fonts, high-contrast colors
- Slow-paced gameplay with positive-only feedback (no losing screens)
- Game types: Matching, Sequence ordering, Memory cards, Drag-and-drop
- Unlock after completing 2 quizzes
- Rewards system: Coins, Stars, and Badges
- Difficulty progression based on performance

### Attendance System (NEW)
- Student self-attendance marking
- Voice-based attendance with audio confirmation
- Daily, weekly, and monthly attendance tracking
- Teacher attendance management

### Parent Dashboard (NEW)
- Separate parent login portal
- View child's quiz scores and progress
- ADHD focus pattern indicators
- Dyslexia reading speed tracking
- Optional audio mode for accessibility
- Strengths and improvement recommendations

### Analytics
- Quiz score tracking
- Progress charts (Matplotlib)
- Weekly activity reports
- Achievement badges
- Personalized recommendations

### AI Agents (NEW)
Four intelligent agents power the adaptive learning experience:

**1. Adaptive Learning Agent** (`modules/adaptive_agent.py`)
- Analyzes quiz history to detect learning patterns (fail streaks, fast completions, stuck behavior)
- Automatically adjusts lesson difficulty (easy/medium/advanced) based on performance
- Generates encouraging mistake summaries using LLM with rule-based fallback
- Provides personalized content recommendations

**2. Accessibility Agent** (`modules/accessibility_agent.py`)
- Tracks user behavior (reading speed, zoom levels, scroll patterns, struggle events)
- Auto-enables accessibility features based on detected needs:
  - Audio mode for slow readers
  - Large text for high zoom users
  - Reduced motion for struggling users
- Provides AI-recommended accessibility settings

**3. Emotion Detection Agent** (`static/js/emotion_agent.js`)
- Browser-based emotion detection using TensorFlow.js/face-api.js
- Detects: happy, sad, frustrated, confused, bored
- Sends emotion data to backend for adaptive responses
- Privacy-first: all processing happens in browser

**4. Parent & Teacher AI Assistant** (`modules/assistant_agent.py`)
- Generates weekly progress summaries (attendance, quizzes, lessons, games)
- Analyzes strengths and weaknesses by subject
- Creates LLM-powered improvement recommendations
- Provides comprehensive dashboard data for parents/teachers

**Scheduler Utility** (`utils/scheduler.py`)
- Automated weekly report generation
- Daily cleanup of old emotion logs
- Background task management

**Dashboard AI Controls**
- Toggle AI Mode on/off for adaptive learning
- Quick access to Accessibility Settings
- Toggle Emotion Monitor with webcam permission

**API Endpoints**
- `/api/emotion/detect` - POST emotion data
- `/api/accessibility/settings` - GET/POST settings
- `/api/accessibility/track` - POST behavior events
- `/api/accessibility/recommendations` - GET AI recommendations
- `/api/adaptive/status` - GET adaptive status
- `/api/adaptive/adjust` - POST trigger adjustment
- `/api/ai/toggle` - POST toggle AI mode
- `/api/emotion/toggle` - POST toggle emotion monitor
- `/api/assistant/weekly-summary/<id>` - GET weekly summary
- `/api/assistant/report/<id>` - GET strengths/weaknesses report
- `/api/ai/preferences` - GET current AI preferences

## Database Models
- **Student**: User profiles with accessibility settings, coins, stars
- **Lesson**: Learning content at three difficulty levels
- **Quiz**: Assessment questions per lesson/difficulty
- **QuizQuestion**: Individual questions with options
- **QuizResult**: Student quiz performance
- **LessonProgress**: Lesson completion tracking
- **Game**: Educational game definitions
- **GameSession**: Individual game play sessions
- **GameReward**: Earned badges and rewards
- **AttendanceRecord**: Student attendance records
- **Teacher**: Teacher accounts
- **TeacherAttendance**: Teacher attendance records
- **ParentAccount**: Parent login accounts
- **ParentStudentLink**: Parent-student relationships
- **FocusSession**: ADHD focus tracking
- **ReadingProgress**: Dyslexia reading tracking
- **EmotionLog**: Emotion detection records
- **ActivityLog**: User activity tracking
- **UserPreferences**: AI-detected accessibility preferences (audio_mode, large_text, reduced_motion, sign_language, reading_speed_avg, zoom_preference, ai_mode_enabled, emotion_monitor_enabled)

## Running the Application
The application runs on port 5000 using Gunicorn:
```
gunicorn --bind 0.0.0.0:5000 --reload main:app
```

## Seeding Data
Run the seed script to populate sample lessons and quizzes:
```
python seed_data.py
```

## Demo Accounts
- **Student**: DEMO001 (Demo Student)
- **Teacher**: TEACH001 (Demo Teacher)
- **Parent**: PARENT001 (Demo Parent)

## Recent Changes
- December 2024: Initial MVP implementation
  - Created complete Flask application structure
  - Implemented all accessibility modules
  - Built responsive, accessible UI
  - Added adaptive quiz system
  - Created progress analytics with charts

- December 2024: Educational Games & Extended Features
  - Added ADHD-friendly educational games (matching, sequence, memory, drag-drop)
  - Games unlock after completing 2 quizzes
  - Implemented attendance tracking with voice-based marking
  - Created parent dashboard with special education indicators
  - Updated lesson content to UG Computer Science curriculum
  - Added rewards system (coins, stars, badges)
  - Extended navigation with Games and Attendance links
  - Added quick action cards to dashboard

- December 2024: AI Agents Implementation
  - Added Adaptive Learning Agent for performance-based difficulty adjustment
  - Added Accessibility Agent for automatic accessibility feature detection
  - Added Emotion Detection Agent (browser-based TensorFlow.js)
  - Added Parent & Teacher AI Assistant for progress reports
  - Added UserPreferences model for storing AI-detected preferences
  - Added Scheduler utility for automated weekly reports
  - Created 12 new API endpoints for AI agent functionality
  - Added AI control toggles to student dashboard
  - OpenAI GPT integration with rule-based fallback

- December 2024: Lesson Templates & API Enhancements
  - Created 6 new lesson templates (programming_basics, data_structures, databases, networking, operating_systems, oops) with difficulty-based content
  - Added lesson_difficulty.json configuration file for course progression
  - Enhanced adaptive_agent.py with get_lesson_version, get_next_lesson, update_learning_path functions
  - Added TTS API route (/api/tts) with security validation (login required, text limits)
  - Added STT API route (/api/stt) with audio format validation (login required)
  - Created accessibility CSS for high-contrast, large-text, reduced-motion modes
  - Added accessibility toggle functions to dashboard with settings persistence
  - Enhanced security: input validation on TTS/STT routes, file type checking, language whitelisting

- December 2024: Sign Language & Dashboard Enhancements
  - Added "Next Recommended Lesson" section to dashboard with AI-powered recommendations
  - Created sign_language.html template with webcam-based gesture detection interface
  - Added /api/sign-language POST endpoint for processing webcam images
  - Enhanced sign_language_detector.py with detect_gesture() method
  - Updated lesson_difficulty.json to support 3 difficulty levels (beginner, intermediate, advanced) per lesson
  - Added Sign Language Detection quick action card to dashboard

- December 2025: Voice Commands System Integration
  - Created voice_commands.js using Web Speech API for continuous microphone listening
  - Floating microphone button on all authenticated pages (bottom-right corner)
  - Voice command support:
    - "Start lesson <name>" - Opens and plays lesson audio
    - "Stop" / "Pause" - Stops currently playing audio
    - "Repeat" / "Again" - Replays current audio
    - "Next" / "Previous" - Navigate between lessons
    - "Open quiz" / "Take quiz" - Opens quiz for current lesson
    - "Option A/B/C/D" or "Select A/B/C/D" - Selects quiz answer
    - "Submit" - Submits quiz answers
    - "Read question" / "Read options" - Reads quiz content aloud
    - "Help" / "Commands" - Lists available voice commands
    - "Home" / "Dashboard" - Returns to dashboard
    - "Volume up/down", "Mute/Unmute" - Audio controls
  - Added /api/lessons endpoint for lesson data
  - Added /api/quiz/<id>/questions endpoint for quiz data
  - Quiz page "Read Aloud" button for TTS playback of all questions
  - Visual feedback for voice command recognition
  - Automatic quiz mode detection with spoken answer support

## Demo Accounts
The database is seeded with demo accounts for testing:
- **Student**: DEMO001 (select from dropdown on login page)
- **Teacher**: TEACH001 (use at /teacher/login, leave password blank)
- **Parent**: PARENT001 (use at /parent/login)

Students can also create new profiles from the login page.

## User Preferences
- Accessibility-first design
- WCAG AAA compliance where possible
- Atkinson Hyperlegible font for readability
- Touch-friendly targets (min 48px)
- Clear visual feedback for all interactions
- ADHD-friendly: Big buttons, slow pace, positive feedback only
- Dyslexia-friendly: Large fonts, high contrast options
