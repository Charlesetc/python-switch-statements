
# Switch?

Switch statements in python using decorators

```python
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
```
