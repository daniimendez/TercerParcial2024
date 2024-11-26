import time 
import sqlite3 as sql 

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimiento creada")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("autoconocimiento")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE strategic_plan_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER,
    item_type TEXT NOT NULL, -- 'experience', 'growth', 'contribution'
    reference_id INTEGER,    -- ID de la experiencia, crecimiento o aporte
    start_date DATE,
    end_date DATE,
    budget DECIMAL(10,2),
    priority INTEGER,
    FOREIGN KEY (plan_id) REFERENCES strategic_plan(plan_id)
    );""")
    print("Tabla Creada")
    conn.commit()
    conn.close()
        
if __name__ == "__main__":
    createDB()
    createTable()