# import re
# import matplotlib.pyplot as plt
#
#
# def extract_data_from_log(log_file):
#     epochs = []
#     accuracies = []
#     positives = []
#     accuracy_05 = []
#     with open(log_file, 'r') as file:
#         for line in file:
#             epoch_match = re.search(r'Train Phase, Epoch: (\d+)', line)
#             if epoch_match:
#                 epochs.append(int(epoch_match.group(1)))
#             accuracy_match = re.search(r'AUC: ([0-9.]+)', line)
#             if accuracy_match:
#                 accuracies.append(float(accuracy_match.group(1)))
#             positive_match = re.search(r'Positive accuracy: ([0-9.]+)', line)
#             if positive_match:
#                 positives.append(float(positive_match.group(1)))
#             accuracy_05_match = re.search(r'Accuracy@0.5: ([0-9.]+)', line)
#             if accuracy_05_match:
#                 accuracy_05.append(float(accuracy_05_match.group(1)))
#     return epochs, accuracies, positives, accuracy_05
#
#
# def plot_data(epochs, accuracies, positives, accuracy_05):
#     plt.plot(epochs, accuracies, marker='o', label='AUC')
#     plt.plot(epochs, positives, marker='x', label='Positive accuracy')
#     plt.plot(epochs, accuracy_05, marker='s', label='Accuracy@0.5')
#     plt.xlabel('Epoch')
#     plt.ylabel('Value')
#     plt.title('Metrics over epochs')
#     plt.grid(True)
#     plt.legend()
#     plt.show()
#
#
# # اسم الملف
# log_file = 'C:/Users/anastasia/Desktop/log___main__.log'
#
# # استخراج البيانات
# epochs, accuracies, accuracy_05, positives = extract_data_from_log(log_file)
#
# # رسم البيانات
# plot_data(epochs, accuracies, accuracy_05, positives)
""" الكود الي جوا التقييم الاول لحاله """
#
# import re
# import matplotlib.pyplot as plt
#
#
# def extract_data_from_log(log_file):
#
#     epochs = []
#     accuracies = []
#     with open(log_file, 'r') as file:
#         for line in file:
#             epoch_match = re.search(r'Train Phase, Epoch: (\d+)', line)
#             if epoch_match:
#                 epochs.append(int(epoch_match.group(1)))
#             accuracy_match = re.search(r'AUC: ([0-9.]+)', line)
#             if accuracy_match:
#                 accuracies.append(float(accuracy_match.group(1)))
#     return epochs, accuracies
#
#
# def plot_data(epochs, accuracies):
#     plt.plot(epochs, accuracies, marker='o')
#     plt.xlabel('Epoch')
#     plt.ylabel('AUC')
#     plt.title('Accuracy over epochs')
#     plt.grid(True)
#     plt.show()
#
#
# # اسم الملف
# log_file = 'C:/Users/anastasia/Desktop/log___main__.log'
#
# # استخراج البيانات
# epochs, accuracies = extract_data_from_log(log_file)
#
# # رسم البيانات
# plot_data(epochs, accuracies)
#


import re
import matplotlib.pyplot as plt


def extract_data_from_log(log_file):
    epochs = []
    loss_tr = []
    loss_va = []
    positives = []
    with open(log_file, 'r') as file:
        for line in file:
            epoch_match = re.search(r'Train Phase, Epoch: (\d+)', line)
            if epoch_match:
                epochs.append(int(epoch_match.group(1)))
            loss_tr_match = re.search(r'Train Loss \(clf_loss\): ([0-9.]+)', line)
            if loss_tr_match:
                loss_tr.append(float(loss_tr_match.group(1)))
            loss_va_match = re.search(r'Valid Loss \(clf_loss\): ([0-9.]+)', line)
            if loss_va_match:
                loss_va.append(float(loss_va_match.group(1)))
            positive_match = re.search(r'Positive loss: ([0-9.]+)', line)
            if positive_match:
                positives.append(float(positive_match.group(1)))


    return epochs, loss_tr, loss_va, positives


def plot_data(epochs, loss_tr, loss_va, positives):
    plt.plot(epochs, loss_tr, marker='o', label='Train Loss')
    plt.plot(epochs, loss_va, marker='x', label='Valid Loss')
    plt.plot(epochs, positives, marker='s', label='Positive loss')
    plt.xlabel('Epoch')
    plt.ylabel('Value')
    plt.title('Metrics over epochs')
    plt.grid(True)
    plt.legend()
    plt.show()


# اسم الملف
log_file = 'C:/Users/anastasia/Desktop/log___main__.log'

# استخراج البيانات
epochs, loss_tr, loss_va, positives = extract_data_from_log(log_file)

# رسم البيانات
plot_data(epochs, loss_tr, loss_va, positives)

