import json
from pathlib import Path
from directories import json_path



class ProgressionManager:
    def __init__(self):
        self.progressions = json_path('progressions.json')

        #Setup initial information
        self.earned_scrap = 0
        self.item_cost = {}
        self.item_unlocked = set()


    def load_progressions(self):
        """
        Loads the progression state from progression.json.
        Handles cases where the file doesn't exist or is corrupted.
        """
        if not self.progressions.exists():
            self.create_default_path()

        try:
            with open(self.progressions, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.earned_scrap = data['earned_scrap', 0]
                self.item_cost = data['item_cost', {}]
                self.item_unlocked = set(data['item_unlocked', []])
        except (json.JSONDecodeError, IOError) as e:
            print(f"Could not load progression.json. Reason: {e}")

    def create_default_path(self):
        """Creates the default path for saving progression data."""
        default_data = {}
        """Writes default data to default path."""
        with open(self.progressions, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, ensure_ascii=False, indent=4)

    def save_progression(self):
        try:
            save_data = {'earned_scrap': self.earned_scrap,
                         'item_cost': self.item_cost,
                         'item_unlocked': sorted(list(self.item_unlocked))
                         }
            with open(self.progressions, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, ensure_ascii=False, indent=4)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Could not save progression. Reason: {e}")

    def add_scrap(self, amount):
        """Adds the scrap to the progression data."""
        if amount > 0:
            self.earned_scrap += amount
            self.save_progression()
            print(f"Added {amount} scrap. New total: {self.earned_scrap}")

    def get_scrap_total(self):
        """Returns the scrap total."""
        return self.earned_scrap

    def is_item_unlocked(self, item_name):
        """Checks if a specific item is unlocked."""
        return item_name in self.item_unlocked

    def get_unlock_status(self, item_name):
        """Returns the unlock status and cost of an item."""
        if item_name not in self.item_cost:
            return None, "Item Locked."
        cost = self.item_cost[item_name]
        if self.is_item_unlocked(item_name):
            return True, "Item Unlocked."
        elif self.earned_scrap >= cost:
            return f"Can unlock {item_name} for {self.item_cost} scrap."
        else:
            return f"{item_name} costs {cost} scrap to unlock."

    def unlock_item(self, item_name):
        """
        Unlocks an item if player has enough scrap.
        Returns True if unlock was successful. False for failure
        """
        if self.is_item_unlocked(item_name):
            return False
        cost = self.item_cost.get(item_name)
        if cost is None:
            return False

        """
        We check if the players total earned scrap meets the cost amount.
        If it does, we unlock the item.
        """
        if self.earned_scrap >= cost:
            self.item_unlocked.add(item_name)
            self.save_progression()
            print(f"Unlocked {item_name}.")

