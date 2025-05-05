# PCAN Logger

A Python script to log CAN messages from a PCAN interface to the console or a file.

## Installation
1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd pcan-logger
    ```
2.  **Install dependencies:**
    Ensure you have Python 3 installed. Then, install the required package:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The script can be run from the command line with various options:

```bash
python pcan_logger.py [options]
```

### Options:

*   `-h`, `--help`: Show the help message and exit.
*   `-f FILE`, `--file FILE`: Path to the log file. If not specified, logs are printed to the console.
*   `-c CHANNEL`, `--channel CHANNEL`: PCAN channel name (e.g., `PCAN_USBBUS1`). Defaults to `PCAN_USBBUS1`.
*   `-b BITRATE`, `--bitrate BITRATE`: CAN bus bitrate in Hz (e.g., `250000`). Defaults to `250000`.

### Examples:

*   **Log to console (default settings):**
    ```bash
    python pcan_logger.py
    ```
    *(Uses PCAN\_USBBUS1, 250000 Hz bitrate)*

*   **Log to a file named `can_data.log`:**
    ```bash
    python pcan_logger.py -f can_data.log
    ```

*   **Log to console using a specific channel and bitrate:**
    ```bash
    python pcan_logger.py -c PCAN_USBBUS2 -b 500000
    ```

*   **Log to a file with specific channel and bitrate:**
    ```bash
    python pcan_logger.py --file my_log.txt --channel PCAN_USBBUS1 --bitrate 125000
    ```

## Log Format

Each log entry follows this format:

```
YYYY-MM-DD HH:MM:SS.fff ID=XXX DLC=Y Data=ZZ ZZ ZZ ...
```

*   `YYYY-MM-DD HH:MM:SS.fff`: Timestamp with milliseconds
*   `XXX`: CAN Arbitration ID (in hexadecimal)
*   `Y`: Data Length Code (number of data bytes)
*   `ZZ ZZ ZZ ...`: Data bytes (in hexadecimal) 