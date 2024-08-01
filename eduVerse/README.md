# EduVarse Frontend

## Overview

EduVarse is a React-based frontend for a Learning Management System (LMS) designed to enhance student learning through personalized tests, efficient task management, and insightful teacher reports.

## Features

- Dynamic test generation based on student performance
- Customizable assignments and deadlines
- Real-time progress tracking and performance analytics
- User-friendly interface for both students and teachers

## Technologies Used

- React
- Redux (for state management)
- Material-UI (for UI components)
- Axios (for API interactions)

## Setup

### Prerequisites

- Node.js `v18.16.0` and npm `v9.5.1`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codewithpriya-522/eduVerse.git
   ```
2. Navigate to the project directory:
   ```bash
   cd EduVarse
   ```
3. Install dependencies:
   ```bash
   npm install
   ```

For the NVM installation instructions, you can use the following:

**Windows:**

```bash
# Install Chocolatey
Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" -Name "Programs" -Value "%AppData%\Roaming\Microsoft\Windows\Start Menu\Programs"
iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))
```

**Unix-based systems:**

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```

## Development

To start the development server, run:

```bash
npm start
```

## Testing

We use Jest for unit testing and React Testing Library for component testing. To run tests:

```bash
npm test
```

## License

MIT

## Contact

[Your email address]
