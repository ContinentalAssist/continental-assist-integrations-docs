class ContinetalMethodTest:
  marks = 0

  def compute_marks(self, obtained_marks):
    marks = obtained_marks
    print('Obtained Marks:', marks)

# convert compute_marks() to class method
ContinetalMethodTest.print_marks = classmethod(ContinetalMethodTest.compute_marks)
ContinetalMethodTest.print_marks(88)

# Output: Obtained Marks: 88