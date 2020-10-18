from abc import ABCMeta, abstractmethod

class Compiler(metaclass=ABCMeta):

    @abstractmethod
    def collectSource(self):
        pass
    
    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

    
class iOSCompiler(Compiler):
    def collectSource(self):
        print("Collecting Swift Source Code")

    def compileToObject(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Swift Program running on runtime environment")
    
class JavaCompiler(Compiler):
    def collectSource(self):
        print("Collecting Java Source Code")

    def compileToObject(self):
        print("Compiling Java code to JVM bitcode")

    def run(self):
        print("Java program running on runtime environment")


if __name__ == "__main__":
    # swift
    ios = iOSCompiler()
    ios.compileAndRun()

    # java
    java = JavaCompiler()
    java.compileAndRun()
