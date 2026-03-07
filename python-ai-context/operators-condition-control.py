# accuracy
# correct_predictions = 850
# total_preditcions = 1000
# accuracy = (correct_predictions/total_preditcions)*100
# print(f"Model's Accuracy: {accuracy}%")

# target_accuracy=0.90
# current_accuracy=0.87

# if current_accuracy>= target_accuracy:
#     print("Model meets requirements")
# else:
#     print(f"Need {target_accuracy-current_accuracy:.2%}")

#choosing model based on the task
task_type="text_generation"
dataset_size = 50000

if task_type == "classification" and dataset_size < 10000:
    model = "Logistic Regression"
    print("Using simple model for small classification task")
elif task_type == "classification" and dataset_size >= 10000:
    model = "Neural network"
    print("using deep learning for large classification task")
elif task_type == "text_generation":
    model="GPT-based Transformer"
    print("Using generative model for test generation")
else:
    model="Custom model"
    print("Building Custom Architechure")

print(f"Selected model:{model}")



