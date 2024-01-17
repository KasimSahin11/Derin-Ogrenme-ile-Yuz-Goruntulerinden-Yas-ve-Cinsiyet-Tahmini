import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Input, GlobalAveragePooling2D, Dense

# Load and prepare the models
def load_models():
    # Age Model
    base_model_age = ResNet50(weights='imagenet', include_top=False, input_tensor=Input(shape=(224, 224, 3)))
    x_age = GlobalAveragePooling2D()(base_model_age.output)
    x_age = Dense(64, activation='relu')(x_age)
    output_age = Dense(1, activation='relu', name='age_output')(x_age)
    age_model = Model(inputs=base_model_age.input, outputs=output_age)
    age_model.load_weights('C:/Users/kasim/age_model_weights.h5')

    # Gender Model
    base_model_gender = ResNet50(weights='imagenet', include_top=False, input_tensor=Input(shape=(224, 224, 3)))
    x_gender = GlobalAveragePooling2D()(base_model_gender.output)
    x_gender = Dense(64, activation='relu')(x_gender)
    output_gender = Dense(1, activation='sigmoid', name='gender_output')(x_gender)
    gender_model = Model(inputs=base_model_gender.input, outputs=output_gender)
    gender_model.load_weights('C:/Users/kasim/gender_model_weights.h5')

    return age_model, gender_model

age_model, gender_model = load_models()

# GUI Class
class AgeGenderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Yaş ve Cinsiyet Tahmin Uygulaması")
        self.geometry("440x330")

        self.panel = tk.Label(self)
        self.panel.pack(padx=10, pady=10)

        btn = tk.Button(self, text="Resim Seç", command=self.open_image)
        btn.pack(pady=5)

        self.result_label = tk.Label(self, text="Tahminler burada görünecek")
        self.result_label.pack(pady=5)

    import os

    def open_image(self):
        path = filedialog.askopenfilename()
        if path:
            if not os.path.isfile(path):
                messagebox.showerror("Hata", "Seçilen dosya mevcut değil.")
                return

            try:
                self.process_image(path)
            except Exception as e:
                messagebox.showerror("Hata", f"Resim işlenirken bir hata meydana geldi: {e}")
                print(f"Resim işlenirken bir hata meydana geldi: {e}")


    def process_image(self, image_path):
        original_image = Image.open(image_path)
        original_image = original_image.resize((224, 224), Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=original_image)
        self.panel.imgtk = imgtk
        self.panel.configure(image=imgtk)

        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (224, 224))
        image = np.array(image) / 255.0

        # Predictions
        age_pred = age_model.predict(np.array([image]))
        gender_pred = gender_model.predict(np.array([image]))
        predicted_age = int(np.round(age_pred[0][0]))
        predicted_gender = 'Female' if int(np.round(gender_pred[0][0])) == 1 else 'Male'

        # Display predictions
        self.result_label.config(text=f"Predicted Age: {predicted_age}, Predicted Gender: {predicted_gender}")

# Main Program
if __name__ == "__main__":
    app = AgeGenderApp()
    app.mainloop()
