# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:52:20 2019

@author: OJO3
"""

import sqlite3

conn = sqlite3.connect("stocks.db")

c = conn.cursor()

# =============================================================================
# c.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
# 
# 
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100,35.14)")
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'RHAT', 50,35.25)")
# conn.commit()
# conn.close()
# =============================================================================

# =============================================================================
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'APPLE', 100,4.49)")
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'APPLE', 50,3.23)")
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'APPLE', 100,4.49)")
# c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'SEL', 'APPLE', 50,3.23)")
# conn.commit()
# =============================================================================

# =============================================================================
# symbol = "APPLE"
# c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
# for row in c:
#     print(row)
#     
# conn.close()
# =============================================================================
