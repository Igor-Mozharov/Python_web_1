from classes.default_imaginator import DefaultImaginator


class NoteImaginator(DefaultImaginator):
    def imagination(self):
        print(self.value)
