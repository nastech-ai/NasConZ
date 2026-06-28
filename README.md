<div align="center">
  <h1>📱 NasConZ — Phone Control for NasTech</h1>
  <p><strong>Full Android hardware control for NasTech Agent via Termux + Shizuku.</strong></p>
</div>

## What is NasConZ?

NasConZ is the **phone hardware bridge** for NasTech Agent. It gives NasTech full control over your Android device — screen, camera, sensors, UI, files, and more.

## Features

- **UI Control:** Read screen elements, tap, swipe, type text, open apps
- **Screenshots:** Capture screen via Shizuku privileged execution
- **Camera:** Take photos with front/back camera
- **Sensors:** Battery, WiFi, location, vibration
- **Communication:** Notifications, TTS speech, SMS
- **File Access:** Read and search files on device

## Requirements

- Termux (from F-Droid, not Play Store)
- Termux:API app (install + grant all permissions)
- Shizuku app (start service + export files)
- NasTech Agent (already running)

## Setup

```bash
# 1. Clone NasConZ
git clone https://github.com/nastech-ai/NasConZ.git ~/NasConZ

# 2. Set up Shizuku (copies rish binaries to Termux)
bash ~/NasConZ/scripts/setup_shizuku.sh

# 3. Test it
bash ~/NasConZ/scripts/mobile_tools.sh status
```

## Commands

```bash
# Sensors & Status
bash scripts/mobile_tools.sh status          # Battery, WiFi, location

# UI Control (Shizuku required)
bash scripts/mobile_tools.sh ui_dump        # Read screen elements
bash scripts/mobile_tools.sh tap 500 800     # Tap at coordinates
bash scripts/mobile_tools/sh swipe 100 500 100 200  # Swipe
bash scripts/mobile_tools.sh text "hello"   # Type text
bash scripts/mobile_tools.sh open_app com.android.settings

# Camera & Screen
bash scripts/mobile_tools.sh camera_snap /sdcard/photo.jpg
bash scripts/mobile_tools.sh screenshot /sdcard/screen.png

# Communication
bash scripts/mobile_tools.sh notify "Hello from NasTech"
bash scripts/mobile_tools.sh speak "Text to speech"
bash scripts/mobile_tools.sh vibrate 500

# Files
bash scripts/mobile_tools.sh read_file /sdcard/file.txt
bash scripts/mobile_tools.sh find_files /sdcard *.pdf
```

## Integration with NasTech

NasConZ is designed to work as a **NasTech skill or plugin**. When installed, NasTech can:

- "Take a screenshot of my phone"
- "Open Telegram and send a message"
- "Check my battery level"
- "Navigate to Settings and enable Dark Mode"

All commands execute locally on the phone via Termux.

## License

MIT — NasTech © 2026 Naswif Cohen Nsamba
