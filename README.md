<<<<<<< HEAD
# Check IN - AI-Powered Classroom Assistant

Check IN is an innovative classroom management system that leverages AI to enhance the teaching and learning experience. The application provides automated attendance tracking through voice recognition, lecture recording and summarization, quick voice-based note-taking, and text-to-speech capabilities for accessibility.

## Features

- **Smart Attendance Management**: Automated attendance tracking using teacher voice recognition
- **Lecture Recording & Summarization**: Real-time lecture transcription and AI-powered summarization
- **Quick Notes**: Voice-based note-taking for instant capture of important points
- **Text-to-Speech**: Built-in accessibility features for reading text content aloud
- **Role-Based Access**: Separate interfaces for teachers, students, and administrators
- **Real-time Updates**: Live attendance tracking and lecture status updates

## Tech Stack

### Frontend
- React.js
- TailwindCSS
- Firebase Authentication
- React Speech Recognition
- React Speech Kit

### Backend
- Spring Boot
- Firebase Admin SDK
- MongoDB

### AI Modules
- Faster-Whisper (Speech-to-Text)
- Silero-VAD (Voice Activity Detection)
- LanguageTool (Grammar Correction)

## Project Structure

```
Check-IN/
├── client/                 # React frontend application
├── server/                 # Spring Boot backend
├── ai_modules/            # AI processing modules
└── firebase/              # Firebase configuration
```

## Getting Started

### Prerequisites
- Node.js (v16+)
- Java JDK (v11+)
- Python (v3.8+)
- Firebase CLI
- MongoDB

### Installation

1. Clone the repository
2. Install frontend dependencies:
   ```bash
   cd client
   npm install
   ```
3. Install backend dependencies:
   ```bash
   cd server
   ./mvnw install
   ```
4. Set up Firebase:
   - Create a Firebase project
   - Enable Authentication, Firestore, and Storage
   - Add configuration files

### Development

1. Start the frontend:
   ```bash
   cd client
   npm start
   ```

2. Start the backend:
   ```bash
   cd server
   ./mvnw spring-boot:run
   ```

3. Start AI modules:
   ```bash
   cd ai_modules
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   python main.py
   ```

## Environment Configuration

Create `.env` files in respective directories with necessary configuration:

- `client/.env`
- `server/.env`
- `ai_modules/.env`

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
=======
# Check-IN
lassroom assistant designed to automate attendance, generate clean lecture summaries, enable quick note-taking, and enhance auditory learning through text-to-speech. The system listens to the teacher's voice during class, intelligently marks attendance based on voice input (especially detecting the keyword "absent")
