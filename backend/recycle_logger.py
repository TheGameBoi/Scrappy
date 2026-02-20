from datetime import datetime, timezone
from typing import List, Dict, Any
from directories import json_path
import json



class RecycleLogManager:
    """
    Manages the application's recycle log, including adding entries,
    reading the log, and calculating statistics.
    """
    def __init__(self):
        self.log = json_path / "recycle_log.json"
        self.log_entry: List[Dict[str, Any]] = []
        self.load_log()

    def load_log(self):
        """Loads the log from JSON file into memory."""
        if not self.log.exists():
            self.log_entries = []
            return

        try:
            with open(self.log, "r") as f:
                self.log_entry = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Log file not found due to {e}. Creating a new one.")
            self.log_entry = []


    def save_log(self):
        """Saves the log to JSON file into memory."""
        try:
            with open(self.log, "w") as f:
                json.dump(self.log_entry, f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Log file not saved due to {e}.")

    def add_entry(self, item_name: str, quantity: int, location: str, results: Dict[str, int]):
        """Creates a new log entry and saves it."""
        timestamp = datetime.now(timezone.utc).isoformat()

        new_entry = {
            "timestamp": timestamp,
            "item_name": item_name,
            "quantity": quantity,
            "location": location,
            "results": results,
        }

        self.log_entry.append(new_entry)
        self.save_log()
        print(f"Logged entry. {quantity} x {item_name} x {location}")

    def all_entries(self):
        """Returns all log entries."""
        return list(self.log_entry)

    def total_earned_scrap(self):
        """
        Calculates the total amount of scrap ever earned from the log.
        This is the definitive source of truth for the player's total scrap.
        """
        total_scrap = 0
        for entry in self.all_entries():
            total_scrap += entry["results"]
        return total_scrap