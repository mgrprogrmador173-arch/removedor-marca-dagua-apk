from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
import cv2
import numpy as np
from moviepy.editor import VideoFileClip
import os

class WatermarkRemoverApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="Selecione um vídeo para remover a marca d'água")
        self.file_chooser = FileChooserListView(filters=['*.mp4', '*.avi', '*.mov'])
        self.process_button = Button(text="Processar Vídeo", on_press=self.process_video)
        self.download_button = Button(text="Baixar Vídeo", disabled=True, on_press=self.download_video)

        layout.add_widget(self.label)
        layout.add_widget(self.file_chooser)
        layout.add_widget(self.process_button)
        layout.add_widget(self.download_button)

        return layout

    def process_video(self, instance):
        selected = self.file_chooser.selection
        if not selected:
            self.show_popup("Erro", "Nenhum arquivo selecionado!")
            return

        video_path = selected[0]
        self.label.text = f"Processando: {os.path.basename(video_path)}"

        # Exemplo de seleção manual (substitua por lógica real)
        selection = (100, 100, 200, 50)  # x, y, width, height
        blur_level = 30

        # Processar o vídeo
        self.process_video_logic(video_path, "output.mp4", selection, blur_level)

        self.label.text = "Vídeo processado! Clique em 'Baixar Vídeo'."
        self.download_button.disabled = False

    def process_video_logic(self, input_path, output_path, selection, blur_level):
        cap = cv2.VideoCapture(input_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('temp.mp4', fourcc, fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            x, y, w, h = selection
            roi = frame[y:y+h, x:x+w]
            blurred_roi = cv2.GaussianBlur(roi, (blur_level, blur_level), 0)
            frame[y:y+h, x:x+w] = blurred_roi

            out.write(frame)

        cap.release()
        out.release()

        # Adicionar áudio ao vídeo processado
        video_clip = VideoFileClip('temp.mp4')
        audio_clip = VideoFileClip(input_path).audio
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

        # Remover arquivo temporário
        os.remove('temp.mp4')

    def download_video(self, instance):
        self.show_popup("Sucesso", "Vídeo processado e pronto para download!")

    def show_popup(self, title, message):
        popup = Popup(title=title, size_hint=(0.8, 0.4))
        popup.content = Label(text=message)
        popup.open()

if __name__ == '__main__':
    WatermarkRemoverApp().run()