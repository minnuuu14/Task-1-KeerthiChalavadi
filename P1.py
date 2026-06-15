import pandas as pd
df = pd.read_excel("P1Dataset.xlsx")
print("\n DATASET LOADED ")
print("Shape:", df.shape)
print("\n DATASET INFO ")
print(df.info())
print("\n MISSING VALUES BEFORE CLEANING ")
print(df.isnull().sum())
duplicate_rows = df.duplicated().sum()
print("\n DUPLICATE ROWS ")
print(duplicate_rows)
#remove duplicates
df = df.drop_duplicates()
duplicate_order_ids = df["OrderID"].duplicated().sum()
print("\nDUPLICATE ORDER IDs ")
print(duplicate_order_ids)
text_columns = [
    "Product",
    "ShippingAddress",
    "PaymentMethod",
    "OrderStatus",
    "ReferralSource"
]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
print("\n DATE COLUMN VERIFIED ")
print(df["Date"].head())
print("\n MISSING VALUES AFTER CLEANING ")
print(df.isnull().sum())
print("\n DUPLICATE ROWS AFTER CLEANING ")
print(df.duplicated().sum())
print("\n DUPLICATE ORDER IDs AFTER CLEANING ")
print(df["OrderID"].duplicated().sum())
print("\n QUANTITY SUMMARY ")
print(df["Quantity"].describe())
print("\n UNIT PRICE SUMMARY ")
print(df["UnitPrice"].describe())
print("\n TOTAL PRICE SUMMARY ")
print(df["TotalPrice"].describe())
print("\n ORDER STATUS ")
print(df["OrderStatus"].unique())
print("\n PAYMENT METHODS ")
print(df["PaymentMethod"].unique())
print("\n REFERRAL SOURCES ")
print(df["ReferralSource"].unique())
output_file = "P1Dataset_Cleaned.xlsx"
df.to_excel(output_file, index=False)
print("\n")
print("DATA CLEANING COMPLETED")
print("Cleaned file saved as:")
print(output_file)