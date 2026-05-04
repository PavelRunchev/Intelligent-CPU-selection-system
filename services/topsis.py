from topsisx.topsis import topsis

def topsis_method(data):
    criteria = data[['cpuMark', 'price', 'cores']]

    weights = [0.5, 0.3, 0.2]
    impacts = ['+', '-', '+']

    result = topsis(criteria, weights, impacts)

    data['topsis_score'] = result['Topsis_Score'].round(2)
    data = data.sort_values(by='topsis_score', ascending=False)
    return data.to_dict(orient='records')




