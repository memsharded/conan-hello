from conans import ConanFile, CMake
   
class HelloConan(ConanFile):
    name = "Hello"
    version = "0.1"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/memsharded/conan-hello.git"

    def source(self):
        self.run("git clone https://github.com/memsharded/hello.git")

    def build(self):
        cmake = CMake(self)
        self.run('cd hello && cmake . %s' % cmake.command_line)
        self.run("cd hello && cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*.lib", dst="lib", src="hello/lib")
        self.copy("*.a", dst="lib", src="hello/lib")

    def package_info(self):
        self.cpp_info.cxxflags = [
            "-static-libgcc",
            "-static-libstdc++"
        ]
        self.cpp_info.libs = ["hello"]
