# Day 27: Object-Oriented Programming (OOP) - Abstraction in Python 🧩🏗️🐍

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-27-OF-PYTHON](https://github.com/harish-0987/DAY-27-OF-PYTHON)

Welcome to **Day 27 of Python**! Today's session explores **Abstraction in Python**—one of the four pillars of Object-Oriented Programming (OOP)—explained with clean, basic-level concepts, practical code examples, and real-world architectures.

> [!NOTE]
> **Scope for Today**: We cover what Abstraction is, real-world analogies (car dashboard, TV remote, ATM), the built-in `abc` module (`ABC` and `@abstractmethod`), enforcing subclass contracts, mixing abstract and concrete methods, abstract properties, interface patterns, the difference between Abstraction and Encapsulation, and a real-world **Unified Payment Gateway System**.

---

## 📌 Table of Contents

1. [What is Abstraction? (Basic Level)](#-what-is-abstraction-basic-level)
2. [Real-World Analogies](#-real-world-analogies)
3. [Why Use Abstraction?](#-why-use-abstraction)
4. [The `abc` Module in Python](#-the-abc-module-in-python)
5. [Core Features of Abstraction](#-core-features-of-abstraction)
   - [1. Abstract Base Class (`ABC`) & Direct Instantiation Restriction](#1-abstract-base-class-abc--direct-instantiation-restriction)
   - [2. Enforcing Subclass Contracts (`@abstractmethod`)](#2-enforcing-subclass-contracts-abstractmethod)
   - [3. Combining Abstract Methods with Concrete Methods](#3-combining-abstract-methods-with-concrete-methods)
   - [4. Abstract Properties (`@property` + `@abstractmethod`)](#4-abstract-properties-property--abstractmethod)
   - [5. Pure Abstraction (Interfaces in Python)](#5-pure-abstraction-interfaces-in-python)
6. [Abstraction vs. Encapsulation](#-abstraction-vs-encapsulation)
7. [Real-World Case Study: Unified Payment Gateway](#-real-world-case-study-unified-payment-gateway)
8. [Summary Comparison Matrix](#-summary-comparison-matrix)
9. [How to Run the Code](#-how-to-run-the-code)

---

## 💡 What is Abstraction? (Basic Level)

**Abstraction** is the process of hiding internal complex implementation details and showing only the essential, high-level features and interface to the user.

- **Focus**: It focuses on **WHAT** an object does rather than **HOW** it does it.
- **Mental Model**: As a user or client programmer, you only need to know which methods are available and what they do; you don't need to know the complex inner code or low-level algorithms running them.

```
       ┌────────────────────────────────────────────────────────┐
       │                 CLIENT / EXTERNAL USER                 │
       │                                                        │
       │   Interacts ONLY with the high-level public interface  │
       │   Calls: .start_engine() | .process_payment()          │
       └───────────────────────────┬────────────────────────────┘
                                   │
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │              ABSTRACT BASE CLASS (INTERFACE)           │
       │                                                        │
       │   Defines standard blueprints and contracts (@abstract) │
       └───────────────────────────┬────────────────────────────┘
                                   │
             ┌─────────────────────┴─────────────────────┐
             ▼                                           ▼
┌───────────────────────────┐               ┌───────────────────────────┐
│   SUBCLASS IMPLEMENTATION │               │   SUBCLASS IMPLEMENTATION │
│   (e.g., CreditCard)      │               │   (e.g., UPI)             │
│   Complex internal logic  │               │   Complex internal logic  │
│   hidden from caller      │               │   hidden from caller      │
└───────────────────────────┘               └───────────────────────────┘
```

---

## 🚗 Real-World Analogies

1. **Driving a Car**:
   - You press the **gas pedal** to accelerate and the **brake** to stop.
   - You do **not** need to know how fuel injection, engine cylinders, spark plugs, or hydraulic braking lines operate behind the dashboard.
2. **TV Remote Control**:
   - You press the **Power** button or **Volume Up**.
   - The circuit board, infrared pulse frequencies, and microprocessor inside the remote are abstracted away.
3. **ATM Machine / Online Checkout**:
   - You click **"Pay via UPI"** or **"Withdraw Cash"**.
   - The banking servers, network encryption protocols, and mechanical cash dispensers operate invisibly in the background.

---

## 🎯 Why Use Abstraction?

1. **Reduces Complexity**: Allows programmers to work with simple high-level concepts rather than overwhelming low-level details.
2. **Enforces Code Contracts**: Guarantees that any developer writing a child class *must* provide implementations for critical methods.
3. **Avoids Incomplete Objects**: Prevents developers from instantiating generic, half-baked classes.
4. **Improves Maintainability**: You can refactor or replace underlying subclass implementations without breaking the client code using them.
5. **Enables Polymorphism**: Code can treat diverse concrete objects uniformly through a common abstract interface.

---

## 🛠️ The `abc` Module in Python

Unlike languages such as Java or C++ which have an explicit `abstract` keyword, Python implements abstraction using the standard library module named **`abc`** (*Abstract Base Classes*):

```python
from abc import ABC, abstractmethod
```

- **`ABC`**: The base class to inherit from to make a class abstract.
- **`@abstractmethod`**: A decorator used to mark methods that must be implemented by subclasses.

---

## 🔑 Core Features of Abstraction

### 1. Abstract Base Class (`ABC`) & Direct Instantiation Restriction

An Abstract Base Class cannot be instantiated directly if it contains any abstract methods.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self) -> str:
        """Abstract method: Subclasses must define their own sound."""
        pass

# Attempting direct instantiation:
# animal = Animal("Generic") 
# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'make_sound'
```

### 2. Enforcing Subclass Contracts (`@abstractmethod`)

If a child class forgets to implement *any* abstract method defined in the parent, Python raises a `TypeError` when you try to create an object of that child class.

```python
class Dog(Animal):
    def make_sound(self) -> str:
        return f"{self.name} says: Woof! Woof!"

dog = Dog("Buddy")  # Works perfectly!
```

If an incomplete subclass is defined:
```python
class IncompleteAnimal(Animal):
    pass

# a = IncompleteAnimal("Ghost")
# TypeError: Can't instantiate abstract class IncompleteAnimal without an implementation for abstract method 'make_sound'
```

### 3. Combining Abstract Methods with Concrete Methods

An abstract class does **not** have to be 100% abstract. It can provide normal (concrete) methods that offer shared, reusable code across all subclasses:

```python
class Vehicle(ABC):
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.is_running = False

    # Abstract methods: Subclasses must provide custom implementation
    @abstractmethod
    def start_engine(self) -> None:
        pass

    @abstractmethod
    def stop_engine(self) -> None:
        pass

    # Concrete method: Shared by all vehicles (Code Reuse)
    def honk_horn(self) -> None:
        print(f"[{self.brand} {self.model}] Honk! Honk!")
```

### 4. Abstract Properties (`@property` + `@abstractmethod`)

You can force subclasses to declare specific read-only or calculated properties:

```python
class Shape(ABC):
    @property
    @abstractmethod
    def shape_name(self) -> str:
        pass

    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def shape_name(self) -> str:
        return "Rectangle"

    def calculate_area(self) -> float:
        return self.width * self.height
```

### 5. Pure Abstraction (Interfaces in Python)

When an abstract class contains **only** abstract methods and no internal state or concrete logic, it acts as a pure **Interface**:

```python
class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def execute_query(self, query: str) -> list:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass
```

Any client function can interact with `DatabaseConnector` interchangeably without knowing whether the database is MySQL, SQLite, or PostgreSQL.

---

## ⚖️ Abstraction vs. Encapsulation

Beginners often confuse Abstraction with Encapsulation. Here is the key distinction:

| Dimension | Abstraction | Encapsulation |
|---|---|---|
| **Primary Goal** | **Hiding Complexity** (WHAT to do) | **Hiding Data** (HOW data is protected) |
| **Focus** | High-level interface & design contract | Internal data protection & grouping |
| **Implementation** | `ABC`, `@abstractmethod` | Private variables (`__`), `@property`, Getters/Setters |
| **Perspective** | **Outer perspective**: How clients use the class | **Inner perspective**: How internal state is shielded |
| **Example** | Turning key to start a car without knowing combustion | Masking ATM PIN and checking funds before balance deduction |

---

## 💳 Real-World Case Study: Unified Payment Gateway

In modern e-commerce systems, customers can pay using Credit Cards, UPI, or Net Banking. With Abstraction, the checkout system handles all payment methods uniformly.

```python
class PaymentGateway(ABC):
    def __init__(self, amount: float, currency: str = "INR"):
        self.amount = amount
        self.currency = currency
        self.transaction_id = f"TXN-{int(time.time() * 1000)}"

    @abstractmethod
    def validate_payment_details(self) -> bool:
        pass

    @abstractmethod
    def execute_transaction(self) -> bool:
        pass

    def generate_receipt(self, status: str) -> None:
        print(f"Receipt: {self.transaction_id} | Amount: {self.currency} {self.amount} | Status: {status}")
```

### Subclasses (`CreditCardPayment` and `UPIPayment`):
```python
class CreditCardPayment(PaymentGateway):
    def __init__(self, amount: float, card_number: str, cvv: str):
        super().__init__(amount)
        self.card_number = card_number
        self.cvv = cvv

    def validate_payment_details(self) -> bool:
        return len(self.card_number) == 16 and len(self.cvv) == 3

    def execute_transaction(self) -> bool:
        return self.validate_payment_details()

class UPIPayment(PaymentGateway):
    def __init__(self, amount: float, upi_id: str):
        super().__init__(amount)
        self.upi_id = upi_id

    def validate_payment_details(self) -> bool:
        return "@" in self.upi_id

    def execute_transaction(self) -> bool:
        return self.validate_payment_details()
```

### Universal Checkout Processor:
```python
def process_checkout(payment_method: PaymentGateway) -> None:
    # High-level caller doesn't care which payment gateway was passed!
    is_success = payment_method.execute_transaction()
    status = "SUCCESS" if is_success else "FAILED"
    payment_method.generate_receipt(status)
```

---

## 📊 Summary Comparison Matrix

| Feature / Concept | Syntax / Mechanism | Purpose & Explanation |
|---|---|---|
| **Abstract Base Class** | `class MyClass(ABC):` | Base class that defines a blueprint; cannot be instantiated directly. |
| **Abstract Method** | `@abstractmethod` | Declares a method signature that subclasses **must** override. |
| **Concrete Method** | Normal `def method(self):` | Shared, reusable logic inherited by all child classes. |
| **Abstract Property** | `@property` + `@abstractmethod` | Forces child classes to implement a specific attribute/property. |
| **Interface Pattern** | `ABC` with *only* abstract methods | Pure contract specifying behavior with zero implementation code. |
| **Subclass Enforcement**| `TypeError` on missing methods | Guarantees architectural compliance across your entire codebase. |

---

## 🚀 How to Run the Code

Clone the repository and run the Python script directly:

```bash
# 1. Clone the repository
git clone https://github.com/harish-0987/DAY-27-OF-PYTHON.git

# 2. Navigate to the project directory
cd DAY-27-OF-PYTHON

# 3. Execute the script
python day27.py
```

---

> *"Not here to be known, here to build."*  
> **Created with ❤️ by Harish**
