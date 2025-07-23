import sqlite3
from faker import Faker
import random
import time
import matplotlib.pyplot as plt
from tabulate import tabulate

# Our db name
DB_NAME = "test.db"

# Create a faker instance 
fake = Faker()

def setup_db(index=False):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    # Drop existing table if any
    cur.execute("DROP TABLE IF EXISTS users")

        # Create new users table
    cur.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT
        )
    """)

        # Insert 100,000 dummy users
    for _ in range(100_000):
        name = fake.name()
        age = random.randint(18, 90)
        email = fake.email()
        cur.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))

    # If index is requested, create it on the 'name' column
    if index:
        print("Creating index on name...")
        cur.execute("CREATE INDEX idx_name ON users(name)")

    con.commit()
    con.close()



# Executes a SELECT query for a specific name and measures how long it takes
def run_query(search_name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    start = time.perf_counter()  # Start timing
    cur.execute("SELECT * FROM users WHERE name = ?", (search_name,))
    rows = cur.fetchall()        # Fetch all results
    duration = time.perf_counter() - start  # End timing

    conn.close()
    return duration

# Use EXPLAIN QUERY PLAN to see whether the query used a table scan or an index
def explain_query_plan(search_name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("EXPLAIN QUERY PLAN SELECT * FROM users WHERE name = ?", (search_name,))
    plan = cur.fetchall()
    conn.close()
    return plan

# Plot a simple bar chart comparing query times
def plot_query_times(times):
    import matplotlib.pyplot as plt

    labels = ['No Index', 'With Index']
    values = [times['no_index'], times['with_index']]
    colors = ['red', 'green']

    fig, ax = plt.subplots()
    bars = ax.bar(labels, values, color=colors)

    # Add value labels above each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.4f}s",
            ha='center',
            va='bottom',
            fontsize=10
        )

    # Hide y-axis
    ax.get_yaxis().set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.title("Query Time Comparison (Index vs No Index)")
    plt.tight_layout()
    plt.show()

def main():
    test_name = 'Erik Krook' #we want non existing name to achive a full scan

    print("\n--- Test WITHOUT Index ---")
    setup_db(index=False)
    duration_no_index = run_query(test_name)
    plan_no_index = explain_query_plan(test_name)

    print(f"Query plan {plan_no_index}")

    print("\n--- Test WITH Index ---")
    setup_db(index=True)
    duration_index = run_query(test_name)
    plan_index = explain_query_plan(test_name)

    print(f"Query plan {plan_index}")

    print("\nPerformance comparison:")
    table = [["No Index", f"{duration_no_index:.6f} s"], ["With Index", f"{duration_index:.6f} s"]]
    print(tabulate(table, headers=["Index Type", "Query Time"], tablefmt="github"))

    times = {
        "no_index": duration_no_index,
        "with_index": duration_index
    }
    plot_query_times(times)

if __name__ == "__main__":
    main()

