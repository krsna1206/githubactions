class Main:
    # In Python, we use 'self' as the first argument for instance methods
    def add(self, a, b):
        return a + b
    
    def run(self):
        # We call the method using self.method_name
        print(self.add(5, 4))

# To run the code:
if __name__ == "__main__":
    obj = Main()
    obj.run()