# StreamEase - Streamer's Toolkit

StreamEase is a simple Python application designed to make streaming easier for content creators. Whether you're a Twitch streamer, YouTuber, or live broadcaster on any platform, StreamEase helps you manage your streams more efficiently.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Description

StreamEase provides essential functionalities to streamline your streaming experience. It allows you to start and stop your stream with ease, configure key streaming settings, and manage your stream title, resolution, and bitrate—all from a simple command-line interface.

## Features

- Start and stop your stream with a single command.
- Configure stream settings, including title, resolution, and bitrate.
- User-friendly command-line interface.
- Save your stream settings in a JSON configuration file.

## Getting Started

### Prerequisites

- Python 3 installed on your system.

### Installation

1. Clone this repository or download the source code to your local machine.

2. Ensure you have Python 3 installed. You can check your Python version with the following command:

3. Create a `config.json` file with your initial stream settings. See the [Configuration](#configuration) section below for details on the configuration file format.

4. Open a terminal or command prompt and navigate to the directory where you placed the StreamEase files.

5. Run the StreamEase application:

## Usage

StreamEase offers a straightforward command-line menu for managing your stream. Here's how to use it:

1. **Start Stream**: Initiates your stream. If you're already streaming, it will inform you that you're already live.

2. **Stop Stream**: Ends your stream. If you're not streaming, it will inform you that you're not currently live.

3. **Configure Settings**: Allows you to modify your stream settings, including stream title, resolution, and bitrate.

4. **Exit**: Exits the StreamEase application.

## Configuration

StreamEase stores your stream settings in a `config.json` file. You can customize the following settings:

- `streaming` (boolean): Indicates whether you are currently streaming (true or false).
- `stream_title` (string): Your stream's title.
- `stream_resolution` (string): Your stream's resolution (e.g., "1920x1080").
- `stream_bitrate` (integer): Your stream's bitrate in Kbps.

Here's an example `config.json` file:

```json
{
 "streaming": false,
 "stream_title": "My Awesome Stream",
 "stream_resolution": "1920x1080",
 "stream_bitrate": 2500
}

## License

This project is licensed under the MIT License - see the LICENSE file for details.
