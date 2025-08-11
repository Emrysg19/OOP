# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

    def power_on(self):
        return f"{self.device_info()} is now ON."

    def power_off(self):
        return f"{self.device_info()} is now OFF."


# Subclass (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery_level):
        super().__init__(brand, model)  # Call base class constructor
        self.__storage = storage        # Encapsulated attribute (private)
        self.battery_level = battery_level

    # Getter for private storage
    def get_storage(self):
        return self.__storage

    # Setter for private storage
    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
            return f"Storage updated to {self.__storage}GB."
        else:
            return "Invalid storage value!"

    # Polymorphic method (overrides base class method)
    def device_info(self):
        return f"Smartphone: {self.brand} {self.model}, {self.__storage}GB storage"

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        return f"Battery charged to {self.battery_level}%."

    def use_app(self, app_name, battery_usage):
        if self.battery_level > battery_usage:
            self.battery_level -= battery_usage
            return f"Used {app_name}. Battery now at {self.battery_level}%."
        else:
            return f"Not enough battery to run {app_name}."


# Example usage
if __name__ == "__main__":
    my_phone = Smartphone("Samsung", "Galaxy S25", 256, 75)

    # Calling inherited and overridden methods
    print(my_phone.device_info())        # Polymorphism in action
    print(my_phone.power_on())

    # Encapsulation demo
    print("Current storage:", my_phone.get_storage())
    print(my_phone.set_storage(512))
    print("Updated storage:", my_phone.get_storage())

    # Using smartphone-specific methods
    print(my_phone.use_app("YouTube", 20))
    print(my_phone.charge(15))
    print(my_phone.power_off())
