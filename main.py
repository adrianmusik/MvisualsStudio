from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image as KivyImage
from kivy.uix.button import Button
from kivy.utils import platform
from PIL import Image, ImageOps
import os

class MvisualsStudio(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Platzhalter für das bearbeitete Bild
        self.img_widget = KivyImage(source='logo.png') 
        self.layout.add_widget(self.img_widget)
        
        # Kreativer Filter Button
        btn = Button(text="Kreativer Filter (Grayscale + Solarize)", 
                     size_hint=(1, 0.2),
                     background_color=(0.2, 0.7, 0.9, 1))
        btn.bind(on_press=self.apply_filter)
        self.layout.add_widget(btn)
        return self.layout

    def apply_filter(self, instance):
        # Beispielpfad: Sucht nach einem Testbild im Ordner
        input_path = 'input.jpg'
        output_path = 'mvisuals_output.jpg'
        
        if os.path.exists(input_path):
            with Image.open(input_path) as img:
                # Hier passiert die "kreative" Magie
                img = ImageOps.grayscale(img)
                img = ImageOps.solarize(img, threshold=128)
                img.save(output_path)
            self.img_widget.source = output_path
            self.img_widget.reload()
        else:
            print("Kein 'input.jpg' im Ordner gefunden!")

    def on_start(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, 
                                 Permission.WRITE_EXTERNAL_STORAGE])

if __name__ == '__main__':
    MvisualsStudio().run()
