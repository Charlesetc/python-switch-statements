# Switch.py

def default_switch_default():
    raise LookupError("Value not covered in switch statement")

class Switcher():

    all_mem = []

    @staticmethod
    def current():
        return Switcher.all_mem[-1]

    @staticmethod
    def get(val):
        return Switcher.current().mem[val]

    @staticmethod
    def put(key, val):
        Switcher.current().mem[key] = val

    @staticmethod
    def enter():
        Switcher.all_mem.append(Switcher())

    @staticmethod
    def exit():
        Switcher.all_mem = Switcher.all_mem[:-2]

    @staticmethod
    def default():
        return Switcher.current().default()

    @staticmethod
    def put_default(default):
        Switcher.current().default = default

    def __init__(self):
        self.mem = {}
        self.default = default_switch_default
    

def switch(item):
    Switcher.enter()

    def make_class(cls):
        class NewClass(cls):
            pass

        try:
            a = Switcher.get(item)
        except KeyError:
            a = Switcher.default()
        
        Switcher.exit()
        try:
            a ()
        finally:
            return NewClass

    return make_class

def when(value):

    def decorator(function):
        Switcher.put(value, function)

        def wrapped(self):
            pass

        return wrapped
    return decorator

def default():

    def decorator(function):
        Switcher.put_default(function)

        def wrapped(self):
            pass
        return wrapped

    return decorator

def use_switch_in_a_function(param1, param2):

    @switch(param1)
    class switcher():

        @when(4)
        def this():

            @switch(param2)
            class switcher():

                @when(2)
                def this():
                    print "4 and 2"

                @when(20)
                def this():
                    print "4 and 20"

                @default()
                def this():
                    print "4 and change"

        @when(5)
        def this():
            print 8

        @default()
        def this():
            print "unknown"

use_switch_in_a_function(4, 21)

def spell_number(n):

  @switch(n)
  class switcher():

      @when(1)
      def _():
        print("1st")

      @when(2)
      def _():
        print("2nd")

      @when(3)
      def _():
        print("3rd")

      @default()
      def _():
        print(str(n) + "th")

spell_number(20)
