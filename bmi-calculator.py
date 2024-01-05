import tkinter as tk

#Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100 #Convert height to metres
        bmi = weight / (height ** 2)
        result_label.config(text = f"Your BMI is: {bmi:.2f}", fg = "green")

        #Provide feedback based on BMI categories
        if bmi < 18.5:
            feedback_label.config(text = "Underweight\nThis may increase your risk of health problems\nPlease consult a doctor", fg = "blue")
        elif bmi < 25:
            feedback_label.config(text = "Normal weight\nGood job maintaining a healthy weight!", fg = "green")
        elif bmi < 30:
            feedback_label.config(text = "Overweight\nConsider adopting a healthier lifestyle to reduce your risk of chronic diseases", fg = "orange")
        else:
            feedback_label.config(text = "Obese\nThis significantly increases your risk of health problems\nSeek medical advice for a personalized weight management plan", fg = "red")

    except ValueError:
        result_label.config(text = "Please enter valid numbers for weight and height", fg = "red")
        feedback_label.config(text = "")
    
#Create the main window
root = tk.Tk()
root.title("BMI Calculator")

#Create and place widgets in the window
tk.Label(root, text = "Weight (in kg): ").grid(row = 0, column = 0, padx = 10, pady = 10)
weight_entry = tk.Entry(root)
weight_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

tk.Label(root, text = "Height (in cm): ").grid(row = 1, column = 0, padx = 10, pady = 10)
height_entry = tk.Entry(root)
height_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

calculate_button = tk.Button(root, text = "Calculate BMI", command = calculate_bmi)
calculate_button.grid(row = 2, column = 0, columnspan = 2, pady = 10)

result_label = tk.Label(root, text = "", fg = "black")
result_label.grid(row = 3, column = 0, columnspan = 2, pady = 10)

feedback_label = tk.Label(root, text = "", fg = "black")
feedback_label.grid(row = 4, column = 0, columnspan = 2, pady = 10)

#Start the main event loop
root.mainloop()
