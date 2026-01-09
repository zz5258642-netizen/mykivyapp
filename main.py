# -*- coding: utf-8 -*-

# 关键：在任何 kivy 组件 import 之前，先把默认字体改成我们打包进去的中文字体
from kivy.config import Config

Config.set("kivy", "default_font", [
    "NotoSansSC",
    "fonts/NotoSansSC-Regular.otf",
    "fonts/NotoSansSC-Regular.otf",
    "fonts/NotoSansSC-Regular.otf",
    "fonts/NotoSansSC-Regular.otf",
])

from kivy.core.text import LabelBase
LabelBase.register(name="NotoSansSC", fn_regular="fonts/NotoSansSC-Regular.otf")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=40, spacing=20)

        root.add_widget(Label(
            text="✅ 中文显示正常！\\n如果你看到这行中文不是口口口，就成功了。",
            font_name="NotoSansSC",
            font_size=26
        ))

        btn = Button(
            text="点我测试按钮（中文）",
            font_name="NotoSansSC",
            font_size=22,
            size_hint=(1, None),
            height=120
        )

        def on_press(_):
            # 点击后改变文字，继续验证中文字体
            btn.text = "你点到了 ✅（中文仍然正常）"

        btn.bind(on_press=on_press)
        root.add_widget(btn)

        return root


if __name__ == "__main__":
    MainApp().run()
