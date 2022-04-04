def create_data(obj, num_rows, num_cols):
    id = -1
    data = np.zeros((num_rows * num_cols, 3))
    for j in range(num_cols):
        for i in range(num_rows):
            id += 1            
            data[id][0] = i+1
            data[id][1] = j+1
            data[id][2] = obj.iloc[id,0]    
    df = pd.DataFrame(data)
    df.columns = ['X1', 'X2', 'y']
    return df
