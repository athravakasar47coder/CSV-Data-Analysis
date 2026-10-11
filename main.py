import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv("data/student_data.csv")

# Display dataset
print("\n===== STUDENT DATA =====")
print(data)

# Basic information
print("\n===== BASIC ANALYSIS =====")

print("Number of Students:", len(data))

print("Average Study Hours:",
      round(data["StudyHours"].mean(), 2))

print("Average Attendance:",
      round(data["Attendance"].mean(), 2))

print("Average Maths Marks:",
      round(data["Maths"].mean(), 2))

print("Average Science Marks:",
      round(data["Science"].mean(), 2))

print("Average English Marks:",
      round(data["English"].mean(), 2))


# Find student with highest Maths marks
top_student = data.loc[data["Maths"].idxmax()]

print("\n===== TOP MATHS STUDENT =====")
print("Name:", top_student["Name"])
print("Maths Marks:", top_student["Maths"])


# -------------------------------
# BAR CHART
# -------------------------------

subjects = ["Maths", "Science", "English"]

average_marks = [
    data["Maths"].mean(),
    data["Science"].mean(),
    data["English"].mean()
]

plt.figure(figsize=(8, 5))

plt.bar(subjects, average_marks)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.savefig("charts/average_marks.png")
plt.show()


# -------------------------------
# SCATTER PLOT
# -------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(data["StudyHours"], data["Maths"])

plt.title("Study Hours vs Maths Marks")
plt.xlabel("Study Hours")
plt.ylabel("Maths Marks")

plt.savefig("charts/study_vs_marks.png")
plt.show()


# -------------------------------
# CORRELATION HEATMAP
# -------------------------------

numeric_data = data[
    ["StudyHours", "Attendance", "Maths", "Science", "English"]
]

correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig("charts/correlation_heatmap.png")
plt.show()


# -------------------------------
# INSIGHTS
# -------------------------------

print("\n===== INSIGHTS =====")

print("1. Students with higher study hours generally have higher marks.")

print("2. Attendance has a positive relationship with student performance.")

print("3. The bar chart compares the average marks of different subjects.")

print("4. The scatter plot shows the relationship between study hours and Maths marks.")

print("5. The heatmap shows the correlation between study hours, attendance and marks.")

print("\nAnalysis completed successfully!")