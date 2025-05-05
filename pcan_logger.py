import can
from datetime import datetime
import argparse

def log_message(msg, log_file=None):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    log_entry = f"{timestamp} ID={msg.arbitration_id:X} DLC={msg.dlc} Data={' '.join(f'{byte:02X}' for byte in msg.data)}"
    if log_file:
        with open(log_file, "a") as f:
            f.write(log_entry + "\n")
    else:
        print(log_entry)

def main():
    parser = argparse.ArgumentParser(description="Log CAN messages from a PCAN interface.")
    parser.add_argument(
        '-f', '--file',
        type=str,
        default=None,
        help="Path to the log file. If not specified, logs to console."
    )
    parser.add_argument(
        '-c', '--channel',
        type=str,
        default="PCAN_USBBUS1",
        help="PCAN channel name (e.g., PCAN_USBBUS1)."
    )
    parser.add_argument(
        '-b', '--bitrate',
        type=int,
        default=250000,
        help="CAN bus bitrate in Hz (e.g., 250000)."
    )
    args = parser.parse_args()

    if args.file:
        print(f"Starting CAN logging to file: {args.file}...")
    else:
        print("Starting CAN logging to console...")
    print(f"Using channel: {args.channel}, bitrate: {args.bitrate}")

    try:
        bus = can.interface.Bus(bustype='pcan', channel=args.channel, bitrate=args.bitrate)
        while True:
            msg = bus.recv(timeout=1.0)
            if msg is not None:
                log_message(msg, log_file=args.file)
    except KeyboardInterrupt:
        print("\nLogging stopped by user.")
    except can.CanError as e:
        print(f"CAN Error: {e}")
        print("Please ensure the PCAN drivers are installed and the device is connected.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
