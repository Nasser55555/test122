import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:    @localhost:5432/nasser")

df = pd.read_csv("new_data.csv")

df.to_sql("health_data_cleaned", engine, if_exists="replace", index=False)

with engine.connect() as conn:
    # Répartition par genre
    result = conn.execute(text("SELECT gender, COUNT(*) FROM health_data_cleaned GROUP BY gender"))
    for row in result:
        print(row)

    # Répartition par tabagisme
    result = conn.execute(text("SELECT smoking, COUNT(*) FROM health_data_cleaned GROUP BY smoking"))
    for row in result:
        print(row)

    # Moyenne de l'IMC par genre
    result = conn.execute(text("SELECT gender, ROUND(AVG(bmi)::numeric, 2) FROM health_data_cleaned GROUP BY gender"))
    for row in result:
        print(row)

    # IMC moyen par tranche d'âge
    result = conn.execute(text("""
        SELECT 
            CASE 
                WHEN age BETWEEN 18 AND 30 THEN '18-30'
                WHEN age BETWEEN 31 AND 50 THEN '31-50'
                ELSE '51+'
            END AS age_group,
            ROUND(AVG(bmi)::numeric, 2) AS avg_bmi FROM health_data_cleaned
        GROUP BY age_group
        ORDER BY age_group 
        """))
    for row in result:
        print(row)

    # Moyenne d'âge par catégorie de tabagisme
    result = conn.execute(text("SELECT smoking, ROUND(AVG(age)::numeric, 2) FROM health_data_cleaned GROUP BY smoking"))
    for row in result:
        print(row)