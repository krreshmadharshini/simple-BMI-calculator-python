import tkinter as tk

class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Weight (in kg): ").grid(row=0, column=0, padx=10, pady=10)
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Height (in cm): ").grid(row=1, column=0, padx=10, pady=10)
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.root, text="", fg="black")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.feedback_label = tk.Label(self.root, text="", fg="black")
        self.feedback_label.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100  # Convert height to meters
            bmi = weight / (height ** 2)
            self.result_label.config(text=f"Your BMI is: {bmi:.2f}", fg="green")

            feedback_generator = BMI_FeedbackGenerator()
            feedback_message, text_color = feedback_generator.get_feedback(bmi)

            self.feedback_label.config(text = feedback_message, fg = text_color)

        except ValueError:
            self.result_label.config(text="Please enter valid numbers for weight and height", fg="red")
            self.feedback_label.config(text="")

class BMI_FeedbackGenerator:
    def get_feedback(self, bmi):
        if bmi < 18.5:
            return "Underweight\nThis may increase your risk of health problems\nPlease consult a doctor", "blue"
        elif bmi < 25:
            return "Normal weight\nGood job maintaining a healthy weight!", "green"
        elif bmi < 30:
            return "Overweight\nConsider adopting a healthier lifestyle to reduce your risk of chronic diseases", "orange"
        else:
            return "Obese\nThis significantly increases your risk of health problems\nSeek medical advice for a personalized weight management plan", "red"

if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()
