from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 添加标题
        title = Label(text='我的第一个Kivy应用', font_size=30)
        layout.add_widget(title)
        
        # 添加按钮
        btn = Button(text='点击这里', size_hint=(1, 0.3))
        btn.bind(on_press=self.on_button_click)
        layout.add_widget(btn)
        
        # 添加状态显示
        self.status_label = Label(text='等待点击...', font_size=20)
        layout.add_widget(self.status_label)
        
        return layout
    
    def on_button_click(self, instance):
        self.status_label.text = '按钮被点击了！\n应用运行正常！'

if __name__ == '__main__':
    MyApp().run()
