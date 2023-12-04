# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:00:04 2023

@author: Ernest George
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    
    import pyodbc
    import pandas as pd

    server = '192.168.40.16'
    database = 'zhao.filippo'
    username = 'zhao.filippo'
    password = 'xxx123##'
    driver= '{SQL Server}' # controllare che il driver ODBC sia installato sulla macchina in cui è in esecuzione l'interprete Python

              
    connectionString = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(connectionString) 

    sql_query = """
    select nome,monete_raccolte from Avasiloae.studente
    inner join Avasiloae.monete 
    on studente.id = monete.idstu
    inner join Avasiloae.appartiene
    on studente.id = appartiene.idstu
    inner join Avasiloae.Classi_virtuali
    on appartiene.idcv = Classi_virtuali.id
    where idv = 12 and idcv = 15
    order by monete_raccolte desc
    """ 
    
    df = pd.read_sql(sql_query, conn)
    
    import matplotlib.pyplot as plt
    import os
    
    fig,ax =plt.subplots(figsize=(4,6))
    ax.bar(df.nome, df.monete_raccolte)
    dir = "static/images"
    file_name = "graf.png"
    save_path = os.path.join(dir, file_name)
    plt.savefig(save_path, dpi = 150)
    
    return render_template('table.html', tabella = df.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)