class DynamicStack:
    """Dynamic Stack"""

    def __init__(self):
        self.stack = []

    def __repr__(self):
        """Print the stack"""

        if self.is_empty():
            return "|__________|"

        else:
            longest = (
                10
                if max(len(str(i)) for i in self.stack) < 10
                else max(len(str(i)) for i in self.stack) + 10
            )
            stackstr = ""
            base = "‾" * longest
            mid = "-" * longest

            for item in list(reversed(self.stack[1:])):
                stackstr += "|" + str(item).center(longest) + "|" + "\n"
                stackstr += "|" + mid.center(longest) + "|" + "\n"

            stackstr += "|" + str(self.stack[0]).center(longest) + "|" + "\n"
            stackstr += " " + base.center(longest) + " "
            return stackstr

    def is_empty(self):
        """Returns False if stack is empty"""

        return len(self.stack) == 0

    def push(self, data):
        """Pushes an element into the stack"""

        if isinstance(data, list):
            for i in range(len(data)):
                self.stack.append(data[i])
        elif isinstance(data, (int, str, float)):
            self.stack.append(data)

    def pop(self):
        """Pops an element from the stack"""

        if not self.is_empty():
            return self.stack.pop()

        else:
            print("Cannot pop. Stack is Empty")
            return

    def peek(self):
        """Displays the top most element of the stack"""

        if self.is_empty():
            print("Cannot peak. Stack is empty")
            return None
        return self.stack[-1]
