class Foo:

    def x(self):    # 첫번째 아규먼트로 인스턴스 주소가 들어옴
        pass

    @classmethod
    def y(cls):     # 첫번째 아규먼트로 클래스 주소가 들어옴
        pass

    @staticmethod
    def z():
        pass

obj = Foo()

obj.x() # Foo.x(obj)
obj.y() # Foo.y(Foo)
obj.z() # Foo.z()