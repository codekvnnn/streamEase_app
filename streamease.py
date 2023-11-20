import json
import time

# Load configuration from config.json
def load_config():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        print("Config file not found. Please create 'config.json' with your settings.")
        exit(1)
    except json.JSONDecodeError:
        print("Invalid JSON format in 'config.json'. Please check your configuration.")
        exit(1)

# Save configuration to config.json
def save_config(config):
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)

# Main menu
def main_menu():
    while True:
        print("\n===== StreamEase - Streamer's Toolkit =====")
        print("1. Start Stream")
        print("2. Stop Stream")
        print("3. Configure Settings")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            start_stream()
        elif choice == '2':
            stop_stream()
        elif choice == '3':
            configure_settings()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start streaming
def start_stream():
    config = load_config()
    if config['streaming']:
        print("You are already streaming.")
        return
    
    print("Starting the stream...")
    time.sleep(2)  # Simulate starting the stream
    print("Stream is now live!")
    config['streaming'] = True
    save_config(config)

# Stop streaming
def stop_stream():
    config = load_config()
    if not config['streaming']:
        print("You are not currently streaming.")
        return
    
    print("Stopping the stream...")
    time.sleep(2)  # Simulate stopping the stream
    print("Stream has ended.")
    config['streaming'] = False
    save_config(config)

# Configure settings
def configure_settings():
    config = load_config()
    
    print("\n===== StreamEase Settings =====")
    print(f"1. Stream Title: {config['stream_title']}")
    print(f"2. Stream Resolution: {config['stream_resolution']}")
    print(f"3. Stream Bitrate: {config['stream_bitrate']} Kbps")
    print("4. Back")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        new_title = input("Enter new stream title: ")
        config['stream_title'] = new_title
        save_config(config)
        print("Stream title updated.")
    elif choice == '2':
        new_resolution = input("Enter new stream resolution: ")
        config['stream_resolution'] = new_resolution
        save_config(config)
        print("Stream resolution updated.")
    elif choice == '3':
        new_bitrate = input("Enter new stream bitrate (Kbps): ")
        config['stream_bitrate'] = int(new_bitrate)
        save_config(config)
        print("Stream bitrate updated.")
    elif choice == '4':
        pass
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
