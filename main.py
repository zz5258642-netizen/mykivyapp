from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=20, **kwargs)

        self.lbl = Label(text="✅ 你的APK已经能运行Kivy界面了", font_size=24)
        self.btn = Button(text="点我一下", font_size=24, size_hint=(1, None), height=80)
        self.btn.bind(on_press=self.on_btn)

        self.add_widget(self.lbl)
        self.add_widget(self.btn)

    def on_btn(self, *_):
        self.lbl.text = "🎉 按钮点击成功！"


class MyKivyApp(App):
    def build(self):
        return MainUI()


if __name__ == "__main__":
    MyKivyApp().run()
