# Mutable and Immutable Objects

# Mutable Objects

- **Mutable Objects**: Lists, Sets, Dictionaries
- **Mutable objects** are great for when you need to change the size of the object, example list.append() or list.remove().
- **Mutable objects** are cheaper to change, but are potentially more error prone.
- **Mutable objects** are not hashable, meaning that we cannot use them as dictionary keys.
- **Mutable objects** are side-effect prone, meaning that when you pass them into a function, they can be changed.
- **Mutable objects** are thread-unsafe, meaning that you must protect them when passing them between threads.
- **Mutable objects** are cheaper to change, but are potentially more error prone.
- **Mutable objects** are good for representing things that are changing.
- **Mutable objects** are good for representing changing collections.
- **Mutable objects** are good for representing the world as it is.

# Immutable Objects

- **Immutable Objects**: Strings, Tuples, Numbers
- **Immutable objects** are used when you need to ensure that the object you made will always stay the same, and you don't want to worry about it being changed.
- **Immutable objects** are fundamentally expensive to “change”, because doing so involves creating a copy.
- **Immutable objects** are hashable, meaning that we can use them as dictionary keys.
- **Immutable objects** are side-effect free, meaning that when you pass them into a
- function, they will not be changed.
- **Immutable objects** are fundamentally expensive to “change”, because doing so involves creating a copy.
- **Immutable objects** are thread-safe, meaning that it is safe to pass them between threads.
- **Immutable objects** are good for representing values, but are bad for representing entities.
- **Mutable objects** are good for representing entities, but are bad for representing values.
- **Immutable objects** are good for representing fixed collections.
- **Immutable objects** are good for representing things that will never change.
- **Immutable objects** are good for representing the world as we know it.
