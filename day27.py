# =============================================================================
# DAY 27: OBJECT-ORIENTED PROGRAMMING (OOP) - ABSTRACTION IN PYTHON
# Author: Harish
# Repository: DAY-27-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

"""
WHAT IS ABSTRACTION? (BASIC LEVEL GUIDE)
----------------------------------------
Abstraction is one of the four foundational pillars of Object-Oriented 
Programming (OOP), alongside Inheritance, Polymorphism, and Encapsulation.

DEFINITION:
  Abstraction is the process of hiding the internal complex implementation 
  details and showing only the essential, high-level features and interface 
  to the user.

  In simple terms:
  - It focuses on WHAT an object does rather than HOW it does it.
  - Users interact with intuitive, clean interfaces without needing to understand
    low-level background machinery or complex algorithms.

REAL-WORLD ANALOGIES:
  1. Car Driving:
     - You press the accelerator to speed up, press the brake to stop, and steer the wheel.
     - You DO NOT need to know how fuel injection, spark plugs, or engine cylinders work.
  2. TV Remote Control:
     - You press the "Power" or "Volume Up" button.
     - The circuit boards, infrared emitter signals, and microcontrollers inside
       the remote are completely hidden from you.
  3. ATM Machine / Payment Gateway:
     - You insert a card and tap "Withdraw Money".
     - The complex banking network, database queries, and cash dispensing mechanisms
       operate secretly in the background.

KEY FEATURES OF ABSTRACTION IN PYTHON:
  1. The `abc` Module:
     - Python does not have a native `abstract` keyword (like Java or C++).
     - Instead, Python provides the built-in `abc` (Abstract Base Classes) module:
       `from abc import ABC, abstractmethod`
  2. Abstract Base Class (ABC):
     - A class that inherits from `ABC`.
     - CANNOT be directly instantiated (cannot create objects of an abstract class).
  3. Abstract Method (`@abstractmethod`):
     - A method declared inside an abstract class without a concrete implementation.
     - Subclasses MUST override and provide an implementation for every abstract method.
  4. Enforcing Subclass Contracts:
     - Guarantees that any derived child class adheres to a standardized blueprint.
     - Prevents incomplete or broken implementations from ever being instantiated.
  5. Combining Abstract and Concrete Methods:
     - Abstract classes can contain both abstract methods (to be implemented) and
       regular concrete methods (reusable shared code).
  6. Abstract Properties:
     - Subclasses can be forced to declare specific properties using `@property` and `@abstractmethod`.
  7. Pure vs Partial Abstraction:
     - Pure Abstract Class (Interface): Contains ONLY abstract methods.
     - Partial Abstract Class: Contains both abstract and concrete methods.
  8. Abstraction vs Encapsulation:
     - Abstraction = Hiding complexity (Outer perspective: "What does it do?").
     - Encapsulation = Hiding data & bundling (Inner perspective: "Protect the data").

TOPICS COVERED IN THIS MODULE:
  1. Basic Abstraction & The `abc` Module (`ABC`, `@abstractmethod`)
  2. Enforcing Subclass Contracts (Preventing Incomplete Implementations)
  3. Combining Abstract Methods with Reusable Concrete Methods
  4. Abstract Properties (`@property` + `@abstractmethod`)
  5. Pure Abstraction / Interface-Style Design (Database Connectors)
  6. Abstraction vs. Encapsulation (Key Differences & Synergy)
  7. Real-World Project: Unified Payment Gateway System
  8. Summary Comparison Matrix
"""

import sys
from abc import ABC, abstractmethod
import time

# Ensure safe UTF-8 output on standard console environments
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def print_section(title: str) -> None:
    """Utility function to print cleanly formatted section headers."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


# =============================================================================
# 1. BASIC ABSTRACTION & THE ABC MODULE
# =============================================================================
# In Python, to create an abstract class:
# 1. Inherit from ABC (Abstract Base Class) from the `abc` module.
# 2. Decorate methods that subclasses MUST implement with `@abstractmethod`.
# If you attempt to instantiate an abstract class directly, Python raises a TypeError.

class Animal(ABC):
    """
    Abstract Base Class representing a generic Animal blueprint.
    Any class inheriting from Animal MUST implement `make_sound()`.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self) -> str:
        """Abstract method: Subclasses must define the specific sound."""
        pass


class Dog(Animal):
    """Concrete subclass of Animal."""

    def make_sound(self) -> str:
        return f"{self.name} says: Woof! Woof!"


class Cat(Animal):
    """Concrete subclass of Animal."""

    def make_sound(self) -> str:
        return f"{self.name} says: Meow! Meow!"


class Cow(Animal):
    """Concrete subclass of Animal."""

    def make_sound(self) -> str:
        return f"{self.name} says: Moo! Moo!"


def demo_basic_abstraction():
    print_section("1. BASIC ABSTRACTION & THE ABC MODULE")

    print("[Step 1] Attempting to instantiate the Abstract Base Class directly:")
    try:
        # This will fail because Animal has an unimplemented abstractmethod
        generic_animal = Animal("Generic")
    except TypeError as error:
        print(">> Expected TypeError caught successfully!")
        print(f"   Reason: {error}")
        print("   >> Key Rule: An Abstract Base Class cannot be instantiated directly.")

    print("\n[Step 2] Instantiating concrete subclasses that implement make_sound():")
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    cow = Cow("Daisy")

    print(f"-> {dog.make_sound()}")
    print(f"-> {cat.make_sound()}")
    print(f"-> {cow.make_sound()}")


# =============================================================================
# 2. ENFORCING SUBCLASS CONTRACTS (INCOMPLETE IMPLEMENTATION ERROR)
# =============================================================================
# A major feature of Abstraction is strict contract enforcement.
# If a subclass forgets to implement even one abstract method, Python will
# REFUSE to let you create an instance of that subclass!

class Appliance(ABC):
    """Abstract class defining the contract for home appliances."""

    @abstractmethod
    def turn_on(self) -> None:
        """Must turn the appliance on."""
        pass

    @abstractmethod
    def turn_off(self) -> None:
        """Must turn the appliance off."""
        pass


class CompleteToaster(Appliance):
    """Correctly implements all abstract methods."""

    def turn_on(self) -> None:
        print("[Toaster] Heating coils activated! Bread is toasting.")

    def turn_off(self) -> None:
        print("[Toaster] Coils cooled down. Toast popped up!")


class IncompleteMicrowave(Appliance):
    """
    BUGGY SUBCLASS: Forgets to implement `turn_off()`.
    Python will NOT allow creating instances of this class!
    """

    def turn_on(self) -> None:
        print("[Microwave] Magnetron active! Warming up food.")

    # Missing turn_off()!


def demo_contract_enforcement():
    print_section("2. ENFORCING SUBCLASS CONTRACTS (INCOMPLETE IMPLEMENTATIONS)")

    print("[Step 1] Instantiating class that implements all abstract methods:")
    toaster = CompleteToaster()
    toaster.turn_on()
    toaster.turn_off()

    print("\n[Step 2] Attempting to instantiate incomplete subclass (missing turn_off):")
    try:
        broken_microwave = IncompleteMicrowave()
    except TypeError as error:
        print(">> Expected TypeError caught successfully!")
        print(f"   Reason: {error}")
        print("   >> Key Takeaway: Python ensures all subclasses fulfill their contract!")


# =============================================================================
# 3. COMBINING ABSTRACT METHODS WITH CONCRETE METHODS
# =============================================================================
# An abstract class is not limited to abstract methods!
# It can also provide concrete (normal) methods with actual logic.
# Subclasses automatically inherit concrete methods, giving you both:
# - Contract enforcement (via abstract methods)
# - Code reuse (via concrete methods)

class Vehicle(ABC):
    """
    Abstract Vehicle demonstrating both abstract and concrete methods.
    """

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.is_running = False

    # Abstract methods: Subclasses must define how they start and stop
    @abstractmethod
    def start_engine(self) -> None:
        """How this specific vehicle powers on."""
        pass

    @abstractmethod
    def stop_engine(self) -> None:
        """How this specific vehicle powers off."""
        pass

    # Concrete methods: Shared reusable logic available to all vehicles
    def honk_horn(self) -> None:
        """Shared concrete method: Reusable horn logic."""
        print(f"[{self.brand} {self.model}] Honk! Honk!")

    def display_status(self) -> None:
        """Shared concrete method: Displays current running state."""
        status = "RUNNING" if self.is_running else "STOPPED"
        print(f"[{self.brand} {self.model}] Status: {status}")


class Car(Vehicle):
    """Concrete implementation of a Car."""

    def start_engine(self) -> None:
        self.is_running = True
        print(f"Car ({self.brand} {self.model}): Turning key ignition... Engine roars!")

    def stop_engine(self) -> None:
        self.is_running = False
        print(f"Car ({self.brand} {self.model}): Key turned off. Engine stopped.")


class ElectricScooter(Vehicle):
    """Concrete implementation of an Electric Scooter."""

    def start_engine(self) -> None:
        self.is_running = True
        print(f"Scooter ({self.brand} {self.model}): Pressing power button... Silent electric hum.")

    def stop_engine(self) -> None:
        self.is_running = False
        print(f"Scooter ({self.brand} {self.model}): Motor powered down.")


def demo_abstract_and_concrete_methods():
    print_section("3. ABSTRACT METHODS COMBINED WITH CONCRETE METHODS")

    vehicles = [
        Car("Toyota", "Corolla"),
        ElectricScooter("Ather", "450X")
    ]

    for vehicle in vehicles:
        print(f"\n--- Testing {vehicle.brand} {vehicle.model} ---")
        vehicle.display_status()   # Shared concrete method
        vehicle.start_engine()     # Subclass-specific abstract method
        vehicle.honk_horn()        # Shared concrete method
        vehicle.display_status()   # Shared concrete method
        vehicle.stop_engine()      # Subclass-specific abstract method


# =============================================================================
# 4. ABSTRACT PROPERTIES (@property + @abstractmethod)
# =============================================================================
# You can force subclasses to implement specific attributes/properties by
# stacking `@property` above `@abstractmethod`.

class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    Enforces that subclasses provide 'shape_name', 'calculate_area', and 'calculate_perimeter'.
    """

    @property
    @abstractmethod
    def shape_name(self) -> str:
        """Abstract property: must return the shape name."""
        pass

    @abstractmethod
    def calculate_area(self) -> float:
        """Abstract method: must calculate area."""
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """Abstract method: must calculate perimeter."""
        pass

    def display_details(self) -> None:
        """Concrete method using abstract properties and calculations."""
        print(f"Shape: {self.shape_name:<10} | Area: {self.calculate_area():>8.2f} sq. units | Perimeter: {self.calculate_perimeter():>8.2f} units")


class Rectangle(Shape):
    """Concrete Rectangle shape."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def shape_name(self) -> str:
        return "Rectangle"

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Concrete Circle shape."""

    PI = 3.14159

    def __init__(self, radius: float):
        self.radius = radius

    @property
    def shape_name(self) -> str:
        return "Circle"

    def calculate_area(self) -> float:
        return self.PI * (self.radius ** 2)

    def calculate_perimeter(self) -> float:
        return 2 * self.PI * self.radius


def demo_abstract_properties():
    print_section("4. ABSTRACT PROPERTIES (@property + @abstractmethod)")

    shapes = [
        Rectangle(width=10, height=5),
        Circle(radius=7)
    ]

    for shape in shapes:
        shape.display_details()


# =============================================================================
# 5. PURE ABSTRACTION (INTERFACES IN PYTHON)
# =============================================================================
# In languages like Java or C#, an "interface" is a contract with ONLY abstract
# methods and no state.
# In Python, we create an interface by subclassing ABC and defining ONLY
# abstract methods without any concrete logic or state.

class DatabaseConnector(ABC):
    """
    Pure Abstract Interface for Database Connections.
    Contains no implementation code or state.
    """

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def execute_query(self, query: str) -> list:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass


class MySQLConnector(DatabaseConnector):
    """MySQL specific implementation."""

    def connect(self) -> None:
        print("[MySQL] Connected to MySQL Server on port 3306.")

    def execute_query(self, query: str) -> list:
        print(f"[MySQL] Running query: '{query}'")
        return [{"id": 101, "db": "MySQL", "status": "Success"}]

    def disconnect(self) -> None:
        print("[MySQL] Connection closed.")


class SQLiteConnector(DatabaseConnector):
    """SQLite specific implementation."""

    def connect(self) -> None:
        print("[SQLite] Connected to local database file database.db.")

    def execute_query(self, query: str) -> list:
        print(f"[SQLite] Running query: '{query}'")
        return [{"id": 202, "db": "SQLite", "status": "Success"}]

    def disconnect(self) -> None:
        print("[SQLite] Connection closed.")


def run_database_operations(db: DatabaseConnector, query: str):
    """
    Client function demonstrating abstraction:
    The caller doesn't care whether it is MySQL or SQLite.
    It simply calls the standardized interface methods!
    """
    db.connect()
    results = db.execute_query(query)
    print(f"Results fetched: {results}")
    db.disconnect()


def demo_pure_abstraction_interface():
    print_section("5. PURE ABSTRACTION (INTERFACES IN PYTHON)")

    mysql_db = MySQLConnector()
    sqlite_db = SQLiteConnector()

    print("--- Client interacting with MySQL Connector ---")
    run_database_operations(mysql_db, "SELECT * FROM users LIMIT 5;")

    print("\n--- Client interacting with SQLite Connector ---")
    run_database_operations(sqlite_db, "SELECT name FROM students;")


# =============================================================================
# 6. ABSTRACTION VS. ENCAPSULATION
# =============================================================================
# - Abstraction: Hides COMPLEXITY. Focuses on *WHAT* the object does.
#   Achieved via Abstract Classes and Interfaces.
# - Encapsulation: Hides INTERNAL DATA and protects state. Focuses on *HOW* data is wrapped.
#   Achieved via Private attributes (`__`), Getters, and Setters.

class SmartThermostat(ABC):
    """
    Shows Abstraction and Encapsulation working harmoniously together.
    """

    def __init__(self, initial_temp: float):
        # ENCAPSULATION: Internal temperature is private (__temperature)
        self.__temperature = initial_temp

    # ENCAPSULATION: Controlled getter and setter
    @property
    def temperature(self) -> float:
        return self.__temperature

    @temperature.setter
    def temperature(self, target: float) -> None:
        if 15.0 <= target <= 32.0:
            self.__temperature = target
            print(f"[Thermostat] Target temperature updated to {self.__temperature} C")
        else:
            print(f"[Thermostat Error] {target} C is out of safe range (15 C - 32 C)!")

    # ABSTRACTION: User calls high-level method, hiding internal hardware logic
    @abstractmethod
    def activate_mode(self) -> None:
        """Abstract method showing only high-level command."""
        pass


class HomeThermostat(SmartThermostat):
    """Concrete implementation of HomeThermostat."""

    def activate_mode(self) -> None:
        # Abstraction hides complex hardware switching
        print(f"[HomeThermostat] Sensors active. Adjusting climate to {self.temperature} C.")


def demo_abstraction_vs_encapsulation():
    print_section("6. ABSTRACTION VS. ENCAPSULATION (WORKING TOGETHER)")

    thermostat = HomeThermostat(initial_temp=22.0)

    print("1. Encapsulation: Accessing protected state safely via properties:")
    print(f"Current temp: {thermostat.temperature} C")
    thermostat.temperature = 25.0       # Valid update
    thermostat.temperature = 55.0       # Rejected by encapsulation validation

    print("\n2. Abstraction: Calling high-level interface method:")
    thermostat.activate_mode()          # High-level command hides lower-level hardware steps


# =============================================================================
# 7. REAL-WORLD CASE STUDY: UNIFIED PAYMENT GATEWAY SYSTEM
# =============================================================================
# In e-commerce platforms, multiple payment methods exist (Credit Card, UPI).
# With Abstraction:
# - The checkout system only interacts with a generic `PaymentGateway`.
# - Each payment provider implements its own complex validation and transfer logic.

class PaymentGateway(ABC):
    """
    Abstract Base Class for all payment processors.
    """

    def __init__(self, amount: float, currency: str = "INR"):
        self.amount = amount
        self.currency = currency
        self.transaction_id = f"TXN-{int(time.time() * 1000)}"

    # Abstract methods: Every provider has a unique authorization and transfer process
    @abstractmethod
    def validate_payment_details(self) -> bool:
        """Subclass must validate credential details."""
        pass

    @abstractmethod
    def execute_transaction(self) -> bool:
        """Subclass must contact its server and transfer money."""
        pass

    # Concrete methods: Common receipt generation logic shared by all providers
    def generate_receipt(self, status: str) -> None:
        print("\n" + "-" * 45)
        print("              PAYMENT RECEIPT")
        print("-" * 45)
        print(f"Transaction ID : {self.transaction_id}")
        print(f"Amount         : {self.currency} {self.amount:,.2f}")
        print(f"Status         : {status}")
        print("-" * 45)


class CreditCardPayment(PaymentGateway):
    """Concrete implementation for Credit Card transactions."""

    def __init__(self, amount: float, card_number: str, cvv: str):
        super().__init__(amount)
        self.card_number = card_number
        self.cvv = cvv

    def validate_payment_details(self) -> bool:
        print(f"[Credit Card] Validating Card ending in ...{self.card_number[-4:]} with CVV...")
        return len(self.card_number) == 16 and len(self.cvv) == 3

    def execute_transaction(self) -> bool:
        if self.validate_payment_details():
            print(f"[Credit Card] Network authorized. Deducting {self.currency} {self.amount:,.2f}.")
            return True
        print("[Credit Card] Card validation failed!")
        return False


class UPIPayment(PaymentGateway):
    """Concrete implementation for UPI (Unified Payments Interface) transactions."""

    def __init__(self, amount: float, upi_id: str):
        super().__init__(amount)
        self.upi_id = upi_id

    def validate_payment_details(self) -> bool:
        print(f"[UPI] Verifying UPI ID: {self.upi_id} across payments network...")
        return "@" in self.upi_id

    def execute_transaction(self) -> bool:
        if self.validate_payment_details():
            print(f"[UPI] Notification sent to app... Mobile PIN verified successfully!")
            print(f"[UPI] Transferred {self.currency} {self.amount:,.2f} instantly.")
            return True
        print("[UPI] Invalid UPI ID provided!")
        return False


def process_checkout(payment_method: PaymentGateway) -> None:
    """
    High-level checkout processor demonstrating true abstraction.
    Does not know or care if the user chose Credit Card or UPI.
    It simply calls execute_transaction() and generate_receipt()!
    """
    print(f"\n[Checkout System] Initiating checkout for amount: {payment_method.currency} {payment_method.amount:,.2f}")
    is_successful = payment_method.execute_transaction()
    status = "SUCCESS" if is_successful else "FAILED"
    payment_method.generate_receipt(status)


def demo_payment_gateway_case_study():
    print_section("7. REAL-WORLD CASE STUDY: UNIFIED PAYMENT GATEWAY SYSTEM")

    card_txn = CreditCardPayment(amount=3499.00, card_number="4111222233334444", cvv="890")
    upi_txn = UPIPayment(amount=499.00, upi_id="harish@okhdfcbank")

    # Processing through universal checkout interface
    process_checkout(card_txn)
    process_checkout(upi_txn)


# =============================================================================
# 8. SUMMARY COMPARISON MATRIX
# =============================================================================

def print_abstraction_summary():
    print_section("8. ABSTRACTION QUICK SUMMARY MATRIX")
    table = """
| Feature / Concept    | Syntax / Mechanism            | Description & Purpose                                  |
|----------------------|-------------------------------|--------------------------------------------------------|
| Abstract Base Class  | class MyClass(ABC):           | Blueprint class that cannot be directly instantiated.  |
| Abstract Method      | @abstractmethod               | Declares a mandatory method that child classes MUST code.|
| Concrete Method      | def my_method(self):          | Normal method with shared logic inherited by children. |
| Abstract Property    | @property + @abstractmethod   | Forces child classes to expose a specific property.    |
| Interface Pattern    | ABC with ONLY abstract methods| Pure contract specifying operations without any state.  |
| Abstraction vs Encap | ABC vs Private Variables (__) | Abstraction hides complexity; Encapsulation hides data.|
"""
    print(table.strip())


# =============================================================================
# MAIN ENTRYPOINT
# =============================================================================

def main() -> None:
    print("=" * 70)
    print(" DAY 27: OBJECT-ORIENTED PROGRAMMING (OOP) - ABSTRACTION IN PYTHON")
    print(" Author: Harish | Repository: DAY-27-OF-PYTHON")
    print(" Motto: 'Not here to be known, here to build.'")
    print("=" * 70)

    demo_basic_abstraction()
    demo_contract_enforcement()
    demo_abstract_and_concrete_methods()
    demo_abstract_properties()
    demo_pure_abstraction_interface()
    demo_abstraction_vs_encapsulation()
    demo_payment_gateway_case_study()
    print_abstraction_summary()

    print("\n" + "=" * 70)
    print(" DAY 27 COMPLETE: Abstraction in Python Mastered Successfully!")
    print(" 'Not here to be known, here to build.'")
    print("=" * 70)


if __name__ == "__main__":
    main()
