def load_values(connection, table, column_names_tuple, values_tuple):
    cursor = connection.cursor()
    insert_w_param = f"""INSERT INTO {table}
                      ({", ".join(column_names_tuple)}) 
                      VALUES ({("?," * len(values_tuple))[:-1]})"""
    cursor.execute(insert_w_param, values_tuple)
    connection.commit()
    connection.close()


def read_values(conection, table, column_value, value, desired_values_columns_tuple):
    cursor = conection.cursor()
    des_col = ", ".join(desired_values_columns_tuple)
    consult = (
        f"SELECT {des_col} "
        f"FROM {table} "
        f"WHERE {column_value} = ?"
    )
    cursor.execute(consult, (value,))
    # DEVUELVE COMO TUPPLE!!!!!!!!!!!!!
    return cursor.fetchone()
    
