def clean_data(data):
    data["age"] = data["age"].fillna(data["age"].dropna().median())
    data.loc[data["gender"] == "male", "gender"] = 0
    data.loc[data["gender"] == "female", "gender"] = 1