# Python Classes – README

## Overview
This project covers the basics of Python classes, including class and instance attributes, magic methods, and object creation. It is designed to introduce object-oriented programming (OOP) concepts in Python.

## Classes
- A class is a blueprint for creating objects (instances).  
- Example:

class Square:
    """Empty class that defines a square"""
    pass

## Instance vs Class Attributes

| Attribute Type | Definition | Scope |
|----------------|------------|-------|
| Class attribute | Shared by all instances of the class | Accessed via ClassName.attr or instance if no instance attribute exists |
| Instance attribute | Unique to a specific instance | Defined in __init__ with self.attr |

## Magic Methods (Dunder Methods)

| Method | Purpose | Example |
|--------|---------|---------|
| __init__ | Called when a new instance is created | u = User("John") |
| __str__ | Returns informal, human-readable string | print(u) |
| __repr__ | Returns official string representation | repr(u) |
| __del__ | Called when an instance is deleted | del u |
| __doc__ | Returns docstring of the class or object | print(User.__doc__) |

## Key Points
- __init__ initializes instance attributes.  
- Instance attributes are specific to each object; class attributes are shared.  
- Instance attributes override class attributes.  
- __str__ and __repr__ control how objects are represented as strings.  
- __del__ is called when the object is deleted (destructor).  
- __doc__ provides documentation of the class or object.
