class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f'{self.content}'


class TitlePage(Page):
    def output(self):
        # 基底クラスのメソッドは自動で呼ばれないため
        # 明示的に呼び出す
        title = super().output()
        return title.upper()


class HTMLPageMixin:
    def to_html(self):
        return f'<html><body>{self.output()}</body></html>'


class WebPage(Page, HTMLPageMixin):
    pass


class A:
    def hello(self):
        print("Hello A")


class B(A):
    def hello(self):
        print("Hello B")
        super().hello()


class C(A):
    def hello(self):
        print("Hello C")
        super().hello()


class D(B, C):
    def hello(self):
        print('Hello D')
        super().hello()


if __name__ == "__main__":
    title = TitlePage(0, 'Python Practice Book')
    print(title.output())

    page = WebPage(0, 'web contetn')
    print(page.to_html())

    d = D()
    d.hello()
    print(D.__mro__)
