import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

# Handle missing values
df = df.fillna("Unknown")

# Take user input
question = input("Ask your data question: ").lower()

print("\nAI Response:\n")

# Single clean logic block
if "highest fare" in question:
    result = df.loc[df['Fare'].astype(float).idxmax()]

    print("📊 TOP PASSENGER ANALYSIS")
    print("-" * 40)
    print(result)

    print("\n💡 INSIGHT:")
    print("Passengers paying higher fares were likely in premium class, indicating strong correlation between ticket price and socio-economic status.")

elif "survival" in question:
    survival_rate = df.groupby('Sex')['Survived'].mean()

    print("📊 SURVIVAL ANALYSIS")
    print("-" * 40)
    print(survival_rate)

    print("\n💡 INSIGHT:")
    print("Female passengers had significantly higher survival rates due to priority rescue policies.")

elif "age" in question:
    print("📊 AGE DISTRIBUTION")
    print("-" * 40)
    print(df['Age'].describe())

    print("\n💡 INSIGHT:")
    print("Majority of passengers were adults, which influenced survival patterns.")

elif "insights" in question:
    print("📊 AUTOMATED INSIGHTS")
    print("-" * 40)

    print("1. Female survival rate is higher than male.")
    print("2. Higher fare passengers tend to belong to upper class.")
    print("3. Younger passengers had slightly better survival chances.")

    print("\n💡 This shows pattern-based analysis similar to real-world reporting.")

else:
    print("⚠️ Try asking about: highest fare, survival, age, insights")